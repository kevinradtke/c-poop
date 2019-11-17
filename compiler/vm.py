import memory
from quad_ops import QuadOps

f = open('output.poop')
input_dict = eval(f.read())

memory.init_memory(input_dict)

quadruples = input_dict['quadruples']
quad_ops = QuadOps(quadruples)
