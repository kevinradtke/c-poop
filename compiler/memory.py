memory = []

def init_memory(input_dict):
    for i in range(9001):
        memory.append([i, None])
    memory[9000][1] = []

    #Initialize constants
    ctes = input_dict['cte_dir']
    for cte in ctes:
        memory[cte['addr']][1] = cte['value']

    func_dir = input_dict['func_dir']

    #Initialize globals
    globals = func_dir['global']['vars']
    for g in globals:
        memory[globals[g]['addr']][1] = globals[g]['value']

    #Initialize main func vars
    era(func_dir, 'main')

    display_memory()

def era(func_dir, func_name):
    stack_frame = []
    for i in range(9000, 13000):
        stack_frame.append([i, None])

    vars = func_dir[func_name]['vars']
    for v in vars:
        stack_frame[vars[v]['addr']-9000][1] = vars[v]['value']

    if (len(memory[9000]) < 100):
        memory[9000][1].append(stack_frame)
    else:
        print('ERROR: Stack overflow! => Stack frame calls exceeded')

def display_memory():
    # Prints constants and globals
    for i in range(9000):
        if (memory[i][1] != None):
            print(memory[i])

    # Prints memory for current stack
    stack_size = len(memory[9000][1])
    for var in memory[9000][1][stack_size-1]:
        if (var[1] != None):
            print(var)

# MEMORY ACCESS

def access(addr):
    if (addr < 9000):
        return memory[addr]
    else:
        stack_size = len(memory[9000][1])
        cur_stack = memory[9000][1][stack_size-1]
        return cur_stack[addr-9000]

def get(addr):
    space = access(addr)
    return space[1]

def set(addr, value):
    space = access(addr)
    space[1] = value
