import memory_map
import sys

g_memory = {}
c_memory = {}
local_stack = []
jump_stack = []
MAX_STACK_CALLS = 10
func_dir = {}

def init_memory(input_dict):

    #Initialize constants
    ctes = input_dict['cte_dir']
    for cte in ctes:
        c_memory[cte['addr']] = cte['value']

    global func_dir
    func_dir = input_dict['func_dir']

    #Initialize globals
    globals = func_dir['global']['vars']
    for g in globals:
        g_memory[globals[g]['addr']] = globals[g]['value']

    #Initialize main func vars
    era('main')

    # display_memory()

def era(func_name):
    stack_frame = {}

    vars = func_dir[func_name]['vars']
    for v in vars:
        stack_frame[vars[v]['addr']] = vars[v]['value']

    if (len(local_stack) < MAX_STACK_CALLS):
        local_stack.append(stack_frame)
    else:
        print('ERROR: Stack overflow! => Stack frame calls exceeded')
        sys.exit()

def display_memory():

    # Prints globals
    for g_addr in g_memory:
        print(g_addr, g_memory[g_addr])

    # Prints constants
    for cte_addr in c_memory:
        print(cte_addr, c_memory[cte_addr])

    # Prints memory for current stack
    stack_size = len(local_stack)
    for var_addr in local_stack[stack_size-1]:
        print(var_addr, local_stack[stack_size-1][var_addr])

# MEMORY ACCESS

def set(addr, value):
    if (addr < 5000):
        g_memory[addr] = value
    elif (addr < 9000):
        c_memory[addr] = value
    else:
        stack_size = len(local_stack)
        local_stack[stack_size-1][addr] = value

def get(addr):
    if (addr < 5000):
        return g_memory[addr]
    elif (addr < 9000):
        return c_memory[addr]
    else:
        stack_size = len(local_stack)
        return local_stack[stack_size-1][addr]

def get_param(addr):
    if (addr < 5000):
        return g_memory[addr]
    elif (addr < 9000):
        return c_memory[addr]
    else:
        stack_size = len(local_stack)
        return local_stack[stack_size-1][addr]
