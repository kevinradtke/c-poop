import pprint
import parser
import symbol_table
import sys

success = True

archivo = "tests/test1.txt"
f = open(archivo, 'r')
s = f.read()

parser = parser.parser
parser.parse(s)

if success == True:
    print("Archivo aprobado")

    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(symbol_table.func_table)

    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
