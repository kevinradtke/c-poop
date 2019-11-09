from parser import parser
from test_log import test_log
import sys

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

# DEFAULT TEST
test_name = 'tests/test1.txt'

# TAKES TEST NAME FROM ARGS
if (len(sys.argv) > 1):
    test_name = 'tests/' + sys.argv[1] + '.txt'

compile(test_name)
