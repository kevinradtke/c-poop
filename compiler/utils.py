from symbol_table import Var
import symbol_table

context = 'global'
func_start_pos = 0

def id_lookup(id):
    if (id in symbol_table.func_dir[context]['vars']):
        var = symbol_table.func_dir[context]['vars'][id]
    elif (id in symbol_table.func_dir['global']['vars']):
        var = symbol_table.func_dir['global']['vars'][id]
    else:
        print('ERROR: Variable with name `' + p[1] + '` does not exist!')
        sys.exit()
    return Var(var['type'], id, var['addr'])
