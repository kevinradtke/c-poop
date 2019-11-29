from symbol_table import Var
import symbol_table
import sys
from error_control import err

env = 'testing'
context = 'global'
func_stack = ['main']
cur_stack = 'main'
mode_params = False
goto_main = 0
func_start_pos = 0
success = True

def id_lookup(id):
    if (id in symbol_table.func_dir[context]['vars']):
        var = symbol_table.func_dir[context]['vars'][id]
    elif (id in symbol_table.func_dir['global']['vars']):
        var = symbol_table.func_dir['global']['vars'][id]
    else:
        err('Variable does not exist!', id)
    return Var(var['type'], id, var['addr'])
