
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


def insert_func(func_name, type, pos):
    if func_name in func_table.keys():
        print(f'Error: function with name {func_name} already declared')
    else:
        func_table[func_name] = {
            'type': type,
            'pos': pos,
            'vars': {}
        }


def insert_var(func_name, var_name, type, addr, value):
    if var_name in func_table[func_name]['vars'].keys():
        print(
            f'Error: variable with name {var_name} in function {func_name} already declared')
    else:
        func_table[func_name]['vars'][var_name] = {
            'type': type,
            'addr': addr,
            'value': value
        }
