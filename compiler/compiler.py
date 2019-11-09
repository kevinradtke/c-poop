from parser import parser
from test_log import test_log

def compile(file):

    success = True

    f = open(file, 'r')
    s = f.read()

    parser.parse(s)

    if success == True:
        print('Compiling successful!')
        test_log(file)
    else:
        print('Compile error')

test_name = 'tests/test1.txt'
compile(test_name)
