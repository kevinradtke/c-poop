import symbol_table

context = 'main'
variable_array = []
param_array = []
func_start_pos = 0

def init_function():
    addVariablesToFunction()
    addParametersToFunction()


def changeContext(func_name):
    global context
    context = func_name


def addVariablesToFunction():
    global context
    global variable_array

    for type_arr in variable_array:
        for var_arr in type_arr[2]:
            symbol_table.insert_var(
                type_arr[0], var_arr['name'], type_arr[1], 'FIXME', var_arr['value'])
    variable_array = []


def addParametersToFunction():
    global param_array
    global context

    for param in param_array:
        symbol_table.insert_var(
            context, param['name'], param['type'], 'FIXME', None)
    param_array = []
