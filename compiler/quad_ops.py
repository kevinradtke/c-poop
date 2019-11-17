import sys
import ops_table

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

    def goto(self, quad):
        print('goto', quad)

    def print(self, quad):
        print('print', quad)

    def equal(self, quad):
        print('equal', quad)

    def gotof(self, quad):
        print('gotof', quad)

    def exp(self, op, quad):
        print('exp', op, quad)
