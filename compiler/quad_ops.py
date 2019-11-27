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
        '''assigns the quadruples and starts pos in 0'''
        self.pos = 0
        self.quadruples = quadruples

    def execute(self):
        '''Executes all quadruples'''
        print('\nEXECUTION BEGIN\n')
        self.output = open('ide_output.txt', 'w')   # Opens IDE output terminal
        while (self.pos < len(self.quadruples) and utils.success):
            quad = self.quadruples[self.pos]
            op = quad[1].lower()
            if op in ops_table.ops: # if op is an expression (+, -, and, ...)
                self.exp(op, quad)
            else:
                self.eval(op, quad) # sends op to eval func

            self.pos += 1   # Update current quadruple position

    def eval(self, op, quad):
        '''Assings operation to quadruple'''
        if op in dir(self):     # Checks that function exists in class
            method = getattr(self, op)
            return method(quad) # Executes corresponding method
        else:
            err('Operation does not exist!', op)

    # QUADRUPLE FUNCTIONS

    def goto(self, quad):
        '''Changes current quadruple position'''
        self.pos = quad[4]-2

    def print(self, quad):
        '''Prints to terminal and IDE output'''
        value = memory.get(quad[4])
        self.output.write(str(value) + '\n')
        print(value)

    def equal(self, quad):
        '''Assigns value of an expression to a variable'''
        value = memory.get(quad[2])
        memory.set(quad[4], value)

    def gotof(self, quad):
        '''Evalates an expression to see if it is false it makes a jump'''
        value = memory.get(quad[2])
        if (not value):
            self.pos = quad[4]-2

    def era(self, quad):
        '''Expands current stack frame for function name'''
        utils.func_stack.append(quad[4])
        memory.era(quad[4])
        utils.mode_params = True
        '''Sets mode_params to true so sets and gets act
        upon previous stack frame (where params where setted)'''

    def param(self, quad):
        '''Set param to function'''
        val = memory.get(quad[2], True)
        memory.set(quad[4], val)

    def gosub(self, quad):
        '''Go to function'''
        memory.jump_stack.append(self.pos+1)
        self.pos = quad[4]-2
        utils.mode_params = False
        '''Sets mode params to false so sets and gets act
        upon current stack frame'''

    def exp(self, op, quad):
        '''Evaluates expression using ops table'''
        mode_params = utils.mode_params
        op1 = memory.get(quad[2], mode_params)
        if (quad[3]):   # If operation is binary
            op2 = memory.get(quad[3], mode_params)
            value = ops[op](op1, op2)
        else:           # If operation is unary
            value = ops[op](op1)
        memory.set(quad[4], value, mode_params)

    def ret(self, quad):
        '''Sets the return value to the global variable that stores returns'''
        func = utils.func_stack[len(utils.func_stack)-1]
        val = memory.get(quad[2])
        memory.set(quad[4], val)
        self.pos = memory.func_dir[func]['end']-2

    def endproc(self, quad):
        '''Pops current stack frame and goes to function that called it'''
        memory.local_stack.pop()        # Pops current stack frame
        jump = memory.jump_stack.pop()
        utils.func_stack.pop()
        self.pos = jump-1               # Returns to function call

    def endprog(self, quad):
        print('\nEXECUTION COMPLETE\n')
