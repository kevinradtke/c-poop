import sys
from utils import env

def type_mismatch(op1, op='', op2=''):
    print('ERROR: Type mismatch! => ' + str(op1) + ' ' + op + ' ' + str(op2))
    if env == 'testing':
        sys.exit()
    else:
        output = open('ide_output.txt', 'w')
        output.write(str(value) + '\n')
        output.close()

def err(msg, id):
    print('ERROR:', msg, '=>', id)
    if env == 'testing':
        sys.exit()
    else:
        output = open('ide_output.txt', 'w')
        output.write(str(value) + '\n')
        output.close()
