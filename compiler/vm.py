import memory
from quad_ops import QuadOps
from compiler import compile
import sys
import utils

def run():
    '''Only executes compiled file'''
    f = open('output.poop')
    input_dict = eval(f.read())
    memory.init_memory(input_dict)
    quadruples = input_dict['quadruples']
    runner = QuadOps(quadruples)
    runner.execute()
    f.close()


def comp():
    '''Only compiles source code'''
    compile(test_name)


def comp_and_run():
    '''Compiles and executes'''
    comp()
    run()


def flask_comp_and_run(file_name):
    '''Compiles and executes for IDE'''
    utils.env = 'ide'
    utils.success = True
    compile(file_name)
    run()


# DEFAULT TEST
test_name = 'tests/test2.txt'

# TAKES TEST NAME FROM ARGS
if (len(sys.argv) == 2):
    test_name = 'tests/' + sys.argv[1] + '.txt'

# comp_and_run()
# comp()
# run()
