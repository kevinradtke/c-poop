import sys
import ops_table
from ops_table import ops
import memory
import utils
from error_control import err

class QuadOps:

    pos = 0
    quadruples = []

    def __init__(self, quadruples):
        self.pos = 0
        self.quadruples = quadruples

    def execute(self):
        print('\nEXECUTION BEGIN\n')
        self.output = open('ide_output.txt', 'w')
        while (self.pos < len(self.quadruples) and utils.success):
            quad = self.quadruples[self.pos]
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
            err('Operation does not exist!', op)

    # QUADRUPLE FUNCTIONS

    def goto(self, quad):
        self.pos = quad[4]-2

    def print(self, quad):
        value = memory.get(quad[4])
        self.output.write(str(value) + '\n')
        print(value)

    def equal(self, quad):
        value = memory.get(quad[2])
        memory.set(quad[4], value)

    def gotof(self, quad):
        value = memory.get(quad[2])
        if (not value):
            self.pos = quad[4]-2

    def era(self, quad):
        utils.func_stack.append(quad[4])
        memory.era(quad[4])
        utils.mode_params = True

    def param(self, quad):
        val = memory.get(quad[2], True)
        memory.set(quad[4], val)

    def gosub(self, quad):
        memory.jump_stack.append(self.pos+1)
        self.pos = quad[4]-2
        utils.mode_params = False

    def exp(self, op, quad):
        mode_params = utils.mode_params
        op1 = memory.get(quad[2], mode_params)
        if (quad[3]):
            op2 = memory.get(quad[3], mode_params)
            value = ops[op](op1, op2)
        else:
            value = ops[op](op1)
        memory.set(quad[4], value, mode_params)

    def ret(self, quad):
        func = utils.func_stack[len(utils.func_stack)-1]
        val = memory.get(quad[2])
        memory.set(quad[4], val)
        self.pos = memory.func_dir[func]['end']-2

    def endproc(self, quad):
        memory.local_stack.pop()
        jump = memory.jump_stack.pop()
        utils.func_stack.pop()
        self.pos = jump-1

    def endprog(self, quad):
        print('\nEXECUTION COMPLETE\n')
