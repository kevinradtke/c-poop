import pprint
from tabulate import tabulate
from termcolor import colored
import symbol_table
import code_generator

def print_title(title, color):
    print(colored('\n____ ' + title + ' ____', color))

def test_log(file):
    '''Prints stuff for testing'''

    print_title('Input: ' + file, 'green')

    print_title('Function Table', 'red')
    pp = pprint.PrettyPrinter(indent=2)
    pp.pprint(symbol_table.func_table)

    print_title('Quadruples', 'blue')
    quadruples = code_generator.quadruples
    print(tabulate(quadruples))
