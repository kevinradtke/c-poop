import semantic_cube
import ops_table
import symbol_table
from symbol_table import Var
import sys
import utils

cube = semantic_cube.cube
func_dir = symbol_table.func_dir

quadruples = []
quadruples_addr = []
jump_stack = []
temp_pos = 1

def quad_pos():
    return len(quadruples)+1

def gen_quad(q1, q2, q3, q4):
    quad = [quad_pos(), q1, q2, q3, q4]
    quadruples.append(quad)
    quadruples_addr.append(quad)

def gen_quad_name(q1, q2, q3, q4):
    quad = [quad_pos(), q1, q2, q3, q4]
    quadruples.append(quad)

def gen_quad_addr(q1, q2, q3, q4):
    quad = [quad_pos(), q1, q2, q3, q4]
    quadruples_addr.append(quad)

def mod_quad(row, col, val):
    quadruples[row][col] = val
    quadruples_addr[row][col] = val

def gen_quad_assig(var, exp):
    if (var.type != exp.type):
        type_mismatch(var.type, '=', exp.type)
        sys.exit()
    gen_quad_addr('EQUAL', exp.addr, '', var.addr)
    gen_quad_name('EQUAL', exp.value, '', var.value)

def gen_quad_exp(op, op1, op2):
    type = cube[op][op1.type][op2.type]

    if (type == 'error'):
        type_mismatch(op1.value, op, op2.value)
        sys.exit()
    else:
        global temp_pos
        temp = 'temp' + str(temp_pos)
        temp_addr = insert_temp(type, temp)
        gen_quad_addr(op, op1.addr, op2.addr, temp_addr)
        gen_quad_name(op, op1.value, op2.value, temp)
        temp_pos += 1
        return Var(type, temp, temp_addr)

def insert_temp(type, temp_name):
    func_table = symbol_table.func_table
    context = utils.context
    addr = func_table[context][type][2]
    if (addr >= func_table[context][type][1]):
        temp = [temp_name, addr]
        func_table[context][type][0].append(temp)
        func_table[context][type][2] = addr-1
        func_dir[context]['temps'][temp_name] = {
            'type': type,
            'addr': addr
        }
        return addr
    else:
        print('ERROR: Stack overflow! => ' + utils.context)
        sys.exit()

def gen_if_goto():
    gen_quad('GOTO', '', '', '')
    false = jump_stack.pop()
    jump_stack.append(quad_pos()-2)
    mod_quad(false, 4, quad_pos())

def gen_gotof(exp):
    if (exp.type == 'bool'):
        jump_stack.append(quad_pos()-1)
        gen_quad_addr('GOTOF', exp.addr, '', '')
        gen_quad_name('GOTOF', exp.value, '', '')
    else:
        type_mismatch('Received:', str(exp.value), '| Expected: bool')

def init_while():
    jump_stack.append(quad_pos())

def fill_while():
    false = jump_stack.pop()
    ret = jump_stack.pop()
    gen_quad('GOTO', '', '', ret)
    mod_quad(false, 4, quad_pos())

def gen_repeat(n):
    global temp_pos
    temp = 'temp' + str(temp_pos)
    temp_addr = insert_temp('int', temp)
    temp_var = Var('int', temp, temp_addr)
    temp_pos += 1
    gen_quad_assig(temp_var, n)
    jump_stack.append(quad_pos())
    zero_addr = symbol_table.insert_cte('int', 0)
    zero_var = Var('int', 0, zero_addr)
    res = gen_quad_exp('>', temp_var, zero_var)
    gen_gotof(res)

def fill_repeat():
    false = jump_stack.pop()
    ret = jump_stack.pop()
    counter = Var('int', quadruples[ret-2][4], quadruples_addr[ret-2][4])
    one_addr = symbol_table.insert_cte('int', 1)
    one_var = Var('int', 1, one_addr)
    res = gen_quad_exp('-', counter, one_var)
    gen_quad_assig(counter, res)
    gen_quad('GOTO', '', '', ret)
    mod_quad(false, 4, quad_pos())

def fill_gotof():
    end = jump_stack.pop()
    mod_quad(end, 4, quad_pos())

def fill_params(params):
    func = utils.cur_stack
    if (len(params) != len(func_dir[func]['params'])):
        print('ERROR: quantity of params not correct! =>', func)
        sys.exit()

    for i, param in enumerate(params):

        func_param = func_dir[func]['params'][i]
        if param.type == func_param[1]:
            addr = func_dir[func]['vars'][func_param[0]]['addr']
            gen_quad_addr('PARAM', param.addr, '', addr)
            gen_quad_name('PARAM', param.value, '', func_param[0])
        else:
            print('ERROR: Param type mismatch! =>', func)
            sys.exit()

def gen_era(id):
    if id in func_dir:
        utils.cur_stack = id
        gen_quad('ERA', '', '', id)
    else:
        print('ERROR: Function', id, 'does not exist!')
        sys.exit()

def gen_gosub(jump):
    gen_quad('GOSUB', '', '', jump)

def gen_return(exp):
    if (exp.type == func_dir[utils.context]['type']):
        addr = func_dir['global']['vars'][utils.context]['addr']
        gen_quad_addr('RET', exp.addr, '', addr)
        gen_quad_name('RET', exp.value, '', utils.context)
    else:
        type_mismatch('return', exp.type, 'in function: ' + utils.context)

def get_return(func_name):
    return_exp = utils.id_lookup(func_name)
    global temp_pos
    temp_name = 'temp' + str(temp_pos)
    temp_addr = insert_temp(return_exp.type, temp_name)
    temp_pos += 1
    temp_var = Var(return_exp.type, temp_name, temp_addr)
    gen_quad_assig(temp_var, return_exp)
    return temp_var

def type_mismatch(op1, op='', op2=''):
    print('ERROR: Type mismatch! => ' + str(op1) + ' ' + op + ' ' + str(op2))
    sys.exit()
