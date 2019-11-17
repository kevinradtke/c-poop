import sys
import ops_table
from ops_table import ops
import memory

class QuadOps:

    pos = 0

    def __init__(self, quadruples):
        while (self.pos < len(quadruples)):
            quad = quadruples[self.pos]
            op = quad[1].lower()

            if op in ops_table.ops:
                self.exp(op, quad)
            else:
                self.eval(op, quad)

            self.pos += 1

    def eval(self, op, quad):
        if op in dir(self):
            method = getattr(self, op)
            return method(quad)
        else:
            print('ERROR: Operation `' + op + '` does not exist!')
            sys.exit()


    # QUADRUPLE FUNCTIONS

    def goto(self, quad):
        self.pos = quad[4]-2

    def print(self, quad):
        value = memory.get(quad[4])
        print(value)

    def equal(self, quad):
        value = memory.get(quad[2])
        memory.set(quad[4], value)

    def gotof(self, quad):
        value = memory.get(quad[2])
        if (not value):
            self.pos = quad[4]-2

    def exp(self, op, quad):
        op1 = memory.get(quad[2])
        if (quad[3]):
            op2 = memory.get(quad[3])
            value = ops[op](op1, op2)
        else:
            value = ops[op](op1)
        memory.set(quad[4], value)
