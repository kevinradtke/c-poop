import sys

class Segment:
    INT_MIN = 0
    INT_MAX = 999
    FLOAT_MIN = 1000
    FLOAT_MAX = 1999
    STRING_MIN = 2000
    STRING_MAX = 2999
    BOOL_MIN = 3000
    BOOL_MAX = 3999

    def __init__(self, base_dir):
        self.INT_MIN += base_dir
        self.INT_MAX += base_dir
        self.FLOAT_MIN += base_dir
        self.FLOAT_MAX += base_dir
        self.STRING_MIN += base_dir
        self.STRING_MAX += base_dir
        self.BOOL_MIN += base_dir
        self.BOOL_MAX += base_dir

# DATA SEGMENT
DS = Segment(1000)

# STACK SEGMENT
cur_ss_base = 5000
SS = {}

def era(func_name):
    global cur_ss_base
    if (cur_ss_base < SS_MAX):
        SS[func_name] = Segment(cur_ss_base)
        cur_ss_base += 4000
    else:
        print('ERROR: Stack overflow! => Function limits exceeded. (max 5)')
        sys.exit()

SS_MAX = 24999

# CTE SEGMENT
CS = Segment(25000)
