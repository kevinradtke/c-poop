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
        quad = [op, op1.value, op2.value, 'temp' + str(temppos)]
        temppos += 1
        quadruples.append(quad)
        val = ops_table.ops[op](op1.value, op2.value)
        return Var(type, val)


def gen_quad2(op, op1):
    type = cube[op][op1.type]['']

    if (type == 'error'):
        type_mismatch(op1.value, op)
        sys.exit()
    else:
        quad = [op, op1.value, '', 'temp' + str(temppos)]
        temppos += 1
        quadruples.append(quad)
        val = ops_table.ops[op](op1.value)
        return Var(type, val)
