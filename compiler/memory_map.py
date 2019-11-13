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

# DATA SEGMENT (GLOBAL VARS)
DS = Segment(1000)

# STACK SEGMENT (LOCAL VARS)
SS = Segment(5000)

# CTE SEGMENT (CONSTANTS)
CS = Segment(9000)
