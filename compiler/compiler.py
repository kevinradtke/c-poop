import pprint
from parser import parser
import symbol_table
import sys
import code_generator

def testLog():
    '''Prints stuff for testing'''

    print('\nFunction Table\n')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(symbol_table.func_table)

    print('\nQuadruples\n')
    quadruples = code_generator.quadruples
    for q in quadruples:
        print(q)


success = True

archivo = "tests/test1.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if success == True:
    print('Archivo aprobado')
    testLog()
    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
