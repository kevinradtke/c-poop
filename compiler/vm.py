import memory
from quad_ops import QuadOps
from compiler import compile
import sys


def run():
    f = open('output.poop')
    input_dict = eval(f.read())
    memory.init_memory(input_dict)
    quadruples = input_dict['quadruples']
    QuadOps(quadruples)
    f.close()


def comp():
    compile(test_name)


def comp_and_run():
    comp()
    run()


# DEFAULT TEST
test_name = 'tests/test1.txt'

# TAKES TEST NAME FROM ARGS
if (len(sys.argv) == 2):
    test_name = 'tests/' + sys.argv[1] + '.txt'

# comp_and_run()
# comp()
# run()
