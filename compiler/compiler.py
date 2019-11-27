from parser import parser
from test_log import test_log
import symbol_table
import code_generator
import sys


def gen_obj():
    '''Opens intermediate code file and stores relevant data'''
    obj_file = open('output.poop', 'w')
    output = {
        'func_dir': symbol_table.func_dir,
        'quadruples': code_generator.quadruples_addr,
        'cte_dir': symbol_table.cte_dir
    }
    obj_file.write(str(output))


def compile(file):
    '''Parses input file and compiles data'''
    success = True

    f = open(file, 'r')
    s = f.read()

    parser.parse(s)

    if success == True:
        print('Compiling successful!')
        gen_obj()
        test_log(file)
    else:
        print('Compile error')
