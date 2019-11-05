
# DICTIONARIES

unary_plus_minus = {
    'int': {
        '': 'int'
    },
    'float': {
        '': 'float'
    },
    'string': {
        '': 'error'
    },
    'bool': {
        '': 'error'
    }
}

unary_not = {
    'int': {
        '': 'error'
    },
    'float': {
        '': 'error'
    },
    'string': {
        '': 'error'
    },
    'bool': {
        '': 'bool'
    }
}

comparison_dict = {
    'int': {
        'int': 'bool',
        'float': 'bool',
        'string': 'error',
        'bool': 'bool'
    },
    'float': {
        'int': 'bool',
        'float': 'bool',
        'string': 'error',
        'bool': 'bool'
    },
    'string': {
        'int': 'error',
        'float': 'error',
        'string': 'bool',
        'bool': 'error'
    },
    'bool': {
        'int': 'bool',
        'float': 'bool',
        'string': 'error',
        'bool': 'bool'
    }
}

equality_dict = {
    'int': {
        'int': 'bool',
        'float': 'bool',
        'string': 'bool',
        'bool': 'bool'
    },
    'float': {
        'int': 'bool',
        'float': 'bool',
        'string': 'bool',
        'bool': 'bool'
    },
    'string': {
        'int': 'bool',
        'float': 'bool',
        'string': 'bool',
        'bool': 'bool'
    },
    'bool': {
        'int': 'bool',
        'float': 'bool',
        'string': 'bool',
        'bool': 'bool'
    }
}

division_dict = {
    'int': {
        'int': 'int',
        'float': 'float',
        'string': 'error',
        'bool': 'error'
    },
    'float': {
        'int': 'float',
        'float': 'float',
        'string': 'error',
        'bool': 'error'
    },
    'string': {
        'int': 'error',
        'float': 'error',
        'string': 'error',
        'bool': 'error'
    },
    'bool': {
        'int': 'error',
        'float': 'error',
        'string': 'error',
        'bool': 'error'
    }
}


# SEMANTIC CUBE

cube = {

    # NIVEL FACTOR

    'unary+': unary_plus_minus,
    'unary-': unary_plus_minus,
    'unary!': unary_not,


    # NIVEL TERMINO

    '*': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'string',
            'bool': 'error'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'string': {
            'int': 'string',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        }
    },
    '/': division_dict,
    '//': division_dict,


    # NIVEL EXP3

    '+': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'string': {
            'int': 'error',
            'float': 'error',
            'string': 'string',
            'bool': 'error'
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        }
    },
    '-': {
        'int': {
            'int': 'int',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'float': {
            'int': 'float',
            'float': 'float',
            'string': 'error',
            'bool': 'error'
        },
        'string': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        },
        'bool': {
            'int': 'error',
            'float': 'error',
            'string': 'error',
            'bool': 'error'
        }
    },


    # NIVEL EXP2

    '>': comparison_dict,
    '>=': comparison_dict,
    '<': comparison_dict,
    '<=': comparison_dict,
    '==': equality_dict,
    '!=': equality_dict,


    # NIVEL EXPRESION

    'and': equality_dict,
    'or': equality_dict
}
