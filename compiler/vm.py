import pprint
import virtual_memory

f = open('output.poop')
input_dict = eval(f.read())
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(input_dict)

virtual_memory.init_memory(input_dict)
