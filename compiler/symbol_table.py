import memory_map
import sys

class Function:
    type = 'void'
    vars = {}
    pos = 0

    def __init__(self, t, v={}, a=0):
        self.type = t
        self.pos = p
        self.vars = v


class Var:
    type = 'string'
    value = 'temp'
    addr = 0

    def __init__(self, t, v, a=0):
        self.type = t
        self.value = v
        self.addr = a


func_dir = {
    'global': {
        'type': 'void',
        'pos': 0,
        'vars': {}
    },
}

cte_dir = []

# LOCAL VARS

l_limits = memory_map.SS

func_table = {}

def insert_func(func_name, type='void', pos=0):
    if func_name in func_dir.keys():
        print(f'ERROR: function with name {func_name} already declared')
        sys.exit()
    else:
        func_table[func_name] = {
            'int' : [[], l_limits.INT_MIN, l_limits.INT_MAX],
            'float' : [[], l_limits.FLOAT_MIN, l_limits.FLOAT_MAX],
            'string' : [[], l_limits.STRING_MIN, l_limits.STRING_MAX],
            'bool' : [[], l_limits.BOOL_MIN, l_limits.BOOL_MAX]
        }
        func_dir[func_name] = {
            'type': type,
            'pos': pos,
            'vars': {}
        }

def insert_local_var(func_name, var_name, type, value=None):
    if var_name in func_dir[func_name]['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` in function `{func_name}` already declared')
        sys.exit()
    elif var_name in func_dir['global']['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` in function `{func_name}` already declared globally')
        sys.exit()
    else:
        if (value == None):
            value = defaults[type]
        if (func_table[func_name][type][1] <= func_table[func_name][type][2]):
            func_table[func_name][type][0].append([var_name, value, func_table[func_name][type][1]])
            func_dir[func_name]['vars'][var_name] = {
                'type': type,
                'addr': func_table[func_name][type][1],
                'value': value
            }
            func_table[func_name][type][1] += 1
        else:
            print('ERROR: func_table segment overflow!')
            sys.exit()

defaults = {
    'int': 0,
    'float': 0.0,
    'string': '',
    'bool': True
}


# CONSTANTS

cte_limits = memory_map.CS

# Pos 0 => constant list
# Pos 1 => current position (starts at lower limit)
# Pos 2 => upper limit
cte_table = {
    'int' : [[], cte_limits.INT_MIN, cte_limits.INT_MAX],
    'float' : [[], cte_limits.FLOAT_MIN, cte_limits.FLOAT_MAX],
    'string' : [[], cte_limits.STRING_MIN, cte_limits.STRING_MAX],
    'bool' : [[], cte_limits.BOOL_MIN, cte_limits.BOOL_MAX]
}

def insert_cte(type, val):
    if (cte_table[type][1] <= cte_table[type][2]):
        cte_table[type][0].append([val, cte_table[type][1]])
        cte_dir.append({'val': val, 'type': type, 'addr': cte_table[type][1]})
        cte_table[type][1] += 1
    else:
        print('ERROR: Constant segment overflow!')
        sys.exit()


# GLOBAL VARS

g_limits = memory_map.DS

g_table = {
    'int' : [[], g_limits.INT_MIN, g_limits.INT_MAX],
    'float' : [[], g_limits.FLOAT_MIN, g_limits.FLOAT_MAX],
    'string' : [[], g_limits.STRING_MIN, g_limits.STRING_MAX],
    'bool' : [[], g_limits.BOOL_MIN, g_limits.BOOL_MAX]
}

def insert_global_var(var_name, type, value=None):
    if var_name in func_dir['global']['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` already declared globally')
        sys.exit()
    else:
        if (value == None):
            value = defaults[type]
        if (g_table[type][1] <= g_table[type][2]):
            g_table[type][0].append([var_name, value, g_table[type][1]])
            func_dir['global']['vars'][var_name] = {
                'type': type,
                'addr': g_table[type][1],
                'value': value
            }
            g_table[type][1] += 1
        else:
            print('ERROR: Data segment overflow!')
            sys.exit()
