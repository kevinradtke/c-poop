import semantic_cube
import ops_table
from symbol_table import Var
import sys

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

def gen_quad_exp(op, op1, op2):
    type = cube[op][op1.type][op2.type]

    if (type == 'error'):
        type_mismatch(op1.value, op, op2.value)
        sys.exit()
    else:
        global temp_pos
        temp = 'temp' + str(temp_pos)
        gen_quad_name(op, op1.value, op2.value, temp)
        gen_quad_addr(op, op1.addr, op2.addr, temp)
        temp_pos += 1
        return Var(type, temp)

def gen_if_goto():
    gen_quad('GOTO', '', '', '')
    false = jump_stack.pop()
    jump_stack.append(quad_pos()-2)
    quadruples[false][4] = quad_pos()

def gen_gotof(exp):
    if (exp.type == 'bool'):
        jump_stack.append(quad_pos()-1)
        gen_quad('GOTOF', exp.value, '', '')
    else:
        type_mismatch('Received:', str(exp.value), '| Expected: bool')

def fill_gotof():
    end = jump_stack.pop()
    quadruples[end][4] = quad_pos()

def type_mismatch(op1, op='', op2=''):
    print('ERROR: Type mismatch! => ' + str(op1) + ' ' + op + ' ' + str(op2))
    sys.exit()
