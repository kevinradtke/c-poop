import semantic_cube
import ops_table
from symbol_table import Var

cube = semantic_cube.cube

quadruples = []
temppos = 1

def gen_quad_exp(op, op1, op2):
    type = cube[op][op1.type][op2.type]

    if (type == 'error'):
        type_mismatch(op1.value, op, op2.value)
        sys.exit()
    else:
        global temppos
        temp = 'temp' + str(temppos)
        quad = [op, op1.value, op2.value, temp]
        quadruples.append(quad)
        temppos += 1
        return Var(type, temp)

def gen_quad_2(op, val):
    quad = [op, '', '', val]
    quadruples.append(quad)

def gen_quad_3(op, val1, val2):
    quad = [op, val1, '', val2]
    quadruples.append(quad)
