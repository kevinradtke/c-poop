import operator

'''THIS IS AN OPERATOR DICTIONARY TO SIMPLIFY EVALUATION OF EXPRESSIONS'''

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '//': operator.floordiv,
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
    'unary+': operator.pos,
    'unary-': operator.neg,
    'unary!': operator.not_,
    'and': operator.and_,
    'or': operator.or_
}
