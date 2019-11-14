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
    pp.pprint(symbol_table.func_dir)

    print_title('Quadruples Names', 'blue')
    quadruples = code_generator.quadruples
    print(tabulate(quadruples))

    print_title('Quadruples Addresses', 'blue')
    quadruples = code_generator.quadruples_addr
    print(tabulate(quadruples))

    print_title('Constant Table', 'yellow')
    constants = symbol_table.cte_dir
    print(tabulate(constants))
