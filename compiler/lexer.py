import ply.lex as lex

reserved = {
    'program': 'PROGRAM',
    'var': 'VAR',
    'if': 'IF',
    'else': 'ELSE',
    'float': 'FLOAT',
    'int': 'INT',
    'string': 'STRING',
    'bool': 'BOOL',
    'void': 'VOID',
    'and': 'AND',
    'or': 'OR',
    'print': 'PRINT',
    'loop': 'LOOP',
    'def': 'DEF',
    'return': 'RETURN',
    'main': 'MAIN',
}

# List of tokens
tokens = [
    'ID',
    'CTE_I',
    'CTE_F',
    'CTE_STRING',
    'CTE_BOOL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'NOT',
    'EQUAL',
    'EQUALEQUAL',
    'NOTEQUAL',
    'LT',
    'LTE',
    'GT',
    'GTE',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'COMMA',
    'SEMICOLON',
    # 'COLON'
]

# Caracteres ignorados
t_ignore = ' \t\n'

# Arithmetic Operators
t_NOT = r'\!'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'

# Relational Operators
t_EQUAL = r'\='
t_EQUALEQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_LT = r'\<'
t_LTE = r'\<\='
t_GT = r'\>'
t_GTE = r'\>\='

# Symbols
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
# t_COLON = r'\:'

# Constants
t_CTE_I = r'[0-9]+'
t_CTE_F = r'[0-9]+\.[0-9]+'
t_CTE_STRING = r'\"([^\\\n]|(\\.))*?\"'
t_CTE_BOOL = r'(true|false)'

tokens = tokens + list(reserved.values())


def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_error(t):
    global success
    success = False
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)
    print("entre aqui")


# Construye el lexer
lex.lex()
