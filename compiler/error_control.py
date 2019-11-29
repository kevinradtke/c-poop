import sys
import utils

def type_mismatch(op1, op='', op2=''):
    error_output = 'ERROR: Type mismatch! => ' + str(op1) + ' ' + op + ' ' + str(op2)
    print(error_output)
    if utils.env == 'testing':
        sys.exit()
    else:
        utils.success = False
        output = open('ide_output.txt', 'w')
        output.write(error_output)
        output.close()

def err(msg, id):
    error_output = 'ERROR: ' + msg + ' => ' + id
    print(error_output)
    if utils.env == 'testing':
        sys.exit()
    else:
        utils.success = False
        output = open('ide_output.txt', 'w')
        output.write(error_output)
        output.close()
