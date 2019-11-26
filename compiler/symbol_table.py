import memory_map
import sys

class Var:
    type = 'string'
    value = 'temp'
    addr = 0

    def __init__(self, t, v, a=0):
        self.type = t
        self.value = v
        self.addr = a


func_dir = {}
cte_dir = []

defaults = {
    'int': 0,
    'float': 0.0,
    'string': '',
    'bool': True
}

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
            'vars': {},
            'temps': {},
            'params': [],
            'end': 0
        }

def insert_local_var(func_name, var_name, type, value=None, exp_type=None):
    if (exp_type == None):
        exp_type = type
    if (type != exp_type):
        print('ERROR: Type mismatch! =>', type, '=', exp_type)
        sys.exit()
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
            addr = func_table[func_name][type][1]
            func_dir[func_name]['vars'][var_name] = {
                'type': type,
                'addr': addr,
                'value': value
            }
            func_table[func_name][type][1] += 1
            return Var(type, value, addr)
        else:
            print('ERROR: Stack overflow! => ' + func_name)
            sys.exit()

def insert_param(func_name, var_name, var_type):
    func_dir[func_name]['params'].append([var_name, var_type])

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
    addr = cte_table[type][1]
    if (addr <= cte_table[type][2]):
        cte_table[type][0].append([val, addr])
        cte_dir.append({'value': val, 'type': type, 'addr': addr})
        cte_table[type][1] += 1
        return addr
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

def insert_global_var(var_name, type, value=None, exp_type=None):
    if (exp_type == None):
        exp_type = type
    if (type != exp_type):
        print('ERROR: Type mismatch! =>', type, '=', exp_type)
        sys.exit()
    if var_name in func_dir['global']['vars'].keys():
        print(f'ERROR: variable with name `{var_name}` already declared globally')
        sys.exit()
    else:
        if (value == None):
            value = defaults[type]
        if (g_table[type][1] <= g_table[type][2]):
            g_table[type][0].append([var_name, value, g_table[type][1]])
            addr = g_table[type][1]
            func_dir['global']['vars'][var_name] = {
                'type': type,
                'addr': addr,
                'value': value
            }
            g_table[type][1] += 1
            return Var(type, value, addr)
        else:
            print('ERROR: Data segment overflow!')
            sys.exit()
