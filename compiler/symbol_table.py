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


func_table = {
    'main': {
        'type': 'void',
        'pos': 0,
        'vars': {}
    },
}

# CONSTANTS

cte_limits = memory_map.CS

# Pos 0 => constant list
# Pos 1 => current position (starts at lower limit)
# Pos 2 => upper limit
cte_table = {
    'i' : [[], cte_limits.INT_MIN, cte_limits.INT_MAX],
    'f' : [[], cte_limits.FLOAT_MIN, cte_limits.FLOAT_MAX],
    's' : [[], cte_limits.STRING_MIN, cte_limits.STRING_MAX],
    'b' : [[], cte_limits.BOOL_MIN, cte_limits.BOOL_MAX]
}

def insert_cte(type, val):
    if (cte_table[type][1] <= cte_table[type][2]):
        cte_table[type][0].append([val, cte_table[type][1]])
        cte_table[type][1] += 1
    else:
        print('ERROR: Constant segment overflow!')
        sys.exit()

def insert_func(func_name, type='void', pos=0):
    if func_name in func_table.keys():
        print(f'ERROR: function with name {func_name} already declared')
        sys.exit()
    else:
        func_table[func_name] = {
            'type': type,
            'pos': pos,
            'vars': {}
        }

defaults = {
    'int': 0,
    'float': 0.0,
    'string': '',
    'bool': True
}

def insert_var(func_name, var_name, type, value=None):
    if var_name in func_table[func_name]['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` in function `{func_name}` already declared')
        sys.exit()
    elif var_name in func_table['main']['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` in function `{func_name}` already declared globally')
        sys.exit()
    else:
        if (value == None):
            value = defaults[type]
        func_table[func_name]['vars'][var_name] = {
            'type': type,
            'addr': 0,
            'value': value
        }
