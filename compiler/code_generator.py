import semantic_cube
import ops_table
import symbol_table
from symbol_table import Var
import sys
import utils

cube = semantic_cube.cube

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
    func_dir = symbol_table.func_dir
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

def fill_gotof():
    end = jump_stack.pop()
    mod_quad(end, 4, quad_pos())

def type_mismatch(op1, op='', op2=''):
    print('ERROR: Type mismatch! => ' + str(op1) + ' ' + op + ' ' + str(op2))
    sys.exit()
