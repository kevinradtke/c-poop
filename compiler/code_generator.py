import semantic_cube
import ops_table
from symbol_table import Var

cube = semantic_cube.cube

quadruples = []
temppos = 1

def gen_quad(op, op1, op2):
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
