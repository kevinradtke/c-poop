import ply.yacc as yacc
import lexer
import symbol_table
from symbol_table import Var
import sys
import code_generator
import utils

tokens = lexer.tokens


# --- GENERALES ---

def p_program(p):
    '''program : program_init main_dec
               | program_init vars main_dec
               | program_init funciones main_dec
               | program_init vars funciones main_dec'''

def p_program_init(p):
    '''program_init : PROGRAM ID SEMICOLON'''
    code_generator.gen_quad('GOTO','','','')

def p_funciones(p):
    '''funciones : funcion
                 | funcion funciones'''


def p_main_dec(p):
    '''main_dec : main_init LPAREN RPAREN bloque
                | main_init LPAREN RPAREN LBRACE vars main_aux RBRACE'''
    code_generator.quadruples[0][4] = code_generator.quad_pos()
    symbol_table.func_table['main']['pos'] = code_generator.quad_pos()

def p_main_aux(p):
    '''main_aux : estatuto
                | estatuto main_aux'''

def p_main_init(p):
    '''main_init : MAIN'''
    utils.context = 'main'
    symbol_table.insert_func('main')

def p_vars(p):
    '''vars : VAR varAux1'''


def p_varAux1(p):
    '''varAux1 : tipo varAux2 SEMICOLON
               | tipo varAux2 SEMICOLON varAux1'''
    for var in p[2]:
        if (utils.context == 'global'):
            symbol_table.insert_global_var(var['name'], p[1], var['value'])
        else:
            symbol_table.insert_local_var(utils.context, var['name'], p[1], var['value'])



def p_varAux2(p):
    '''varAux2 : ID
               | ID COMMA varAux2
               | ID EQUAL expresion
               | ID EQUAL expresion COMMA varAux2'''
    if (len(p) == 2):
        p[0] = [{'name': p[1], 'value': None}]
    elif (len(p) == 4):
        if (p[2] == ','):
            p[0] = [{'name': p[1], 'value': None}] + p[3]
        else:
            p[0] = [{'name': p[1], 'value': p[3].value}]
    else:
        p[0] = [{'name': p[1], 'value': p[3].value}] + p[5]


def p_tipo(p):
    '''tipo : INT
            | FLOAT
            | STRING
            | BOOL'''
    p[0] = p[1]


def p_bloque(p):
    '''bloque : LBRACE RBRACE
              | LBRACE bloqueAux RBRACE'''


def p_bloqueAux(p):
    '''bloqueAux : estatuto
                 | estatuto bloqueAux'''


def p_estatuto(p):
    '''estatuto : asignacion
                | condicion
                | escritura
                | loop
                | func_call'''


def p_asignacion(p):
    '''asignacion : ID EQUAL expresion SEMICOLON'''
    code_generator.gen_quad('=', p[3].value, '', p[1])

def p_escritura(p):
    '''escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON'''
    for exp in p[3]:
        code_generator.gen_quad('PRINT', '', '', exp.value)

def p_escrituraAux(p):
    '''escrituraAux : expresion
                    | expresion COMMA escrituraAux'''
    if (len(p)==2):
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

# --- NIVEL EXPRESION ---

def p_expresion(p):
    '''expresion : exp2
                 | and
                 | or'''
    p[0] = p[1]


def p_and(p):
    '''and : exp2 AND expresion'''
    p[0] = code_generator.gen_quad_exp('and', p[1], p[3])


def p_or(p):
    '''or : exp2 OR expresion'''
    p[0] = code_generator.gen_quad_exp('or', p[1], p[3])


# --- NIVEL EXP2 ---

def p_exp2(p):
    '''exp2 : exp3
            | lt
            | lte
            | gt
            | gte
            | eq
            | ne'''
    p[0] = p[1]


def p_lt(p):
    '''lt : exp3 LT exp3'''
    p[0] = code_generator.gen_quad_exp('<', p[1], p[3])


def p_lte(p):
    '''lte : exp3 LTE exp3'''
    p[0] = code_generator.gen_quad_exp('<=', p[1], p[3])


def p_gt(p):
    '''gt : exp3 GT exp3'''
    p[0] = code_generator.gen_quad_exp('>', p[1], p[3])


def p_gte(p):
    '''gte : exp3 GTE exp3'''
    p[0] = code_generator.gen_quad_exp('>=', p[1], p[3])


def p_eq(p):
    '''eq : exp3 EQUALEQUAL exp3'''
    p[0] = code_generator.gen_quad_exp('==', p[1], p[3])


def p_ne(p):
    '''ne : exp3 NOTEQUAL exp3'''
    p[0] = code_generator.gen_quad_exp('!=', p[1], p[3])


# --- NIVEL EXP3 ---

def p_exp3(p):
    '''exp3 : termino
            | addition
            | subtraction'''
    p[0] = p[1]


def p_addition(p):
    '''addition : termino PLUS exp3'''
    p[0] = code_generator.gen_quad_exp('+', p[1], p[3])


def p_subtraction(p):
    '''subtraction : termino MINUS exp3'''
    p[0] = code_generator.gen_quad_exp('-', p[1], p[3])


# --- NIVEL TERMINO ---

def p_termino(p):
    '''termino : factor
               | mult
               | div
               | floor_div'''
    p[0] = p[1]


def p_mult(p):
    '''mult : factor TIMES termino'''
    p[0] = code_generator.gen_quad_exp('*', p[1], p[3])


def p_div(p):
    '''div : factor DIVIDE termino'''
    p[0] = code_generator.gen_quad_exp('/', p[1], p[3])


def p_floor_div(p):
    '''floor_div : factor FLOOR_DIVIDE termino'''
    p[0] = code_generator.gen_quad_exp('//', p[1], p[3])


# --- NIVEL FACTOR ---

def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | factorAux'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_factorAux(p):
    '''factorAux : unary_plus
                 | unary_minus
                 | unary_not
                 | var_cte'''
    p[0] = p[1]


def p_unary_plus(p):
    '''unary_plus : PLUS var_cte'''
    p[0] = code_generator.gen_quad_exp('unary+', p[2], Var('',''))


def p_unary_minus(p):
    '''unary_minus : MINUS var_cte'''
    p[0] = code_generator.gen_quad_exp('unary-', p[2], Var('',''))


def p_unary_not(p):
    '''unary_not : NOT var_cte'''
    p[0] = code_generator.gen_quad_exp('unary!', p[2], Var('',''))


# --- VARIABLE DECLARATION ---

def p_var_cte(p):
    '''var_cte : id
               | cte_i
               | cte_f
               | cte_string
               | cte_bool
               | func_call_var
               '''
    p[0] = p[1]


def p_id(p):
    '''id : ID'''

    if (p[1] in symbol_table.func_table[utils.context]['vars']):
        var = symbol_table.func_table[utils.context]['vars'][p[1]]
        p[0] = Var(var['type'], p[1], var['addr'])
    elif (p[1] in symbol_table.func_table['global']['vars']):
        var = symbol_table.func_table['global']['vars'][p[1]]
        p[0] = Var(var['type'], p[1], var['addr'])
    else:
        print('ERROR: Variable with name `' + p[1] + '` does not exist!')
        sys.exit()


def p_cte_i(p):
    '''cte_i : CTE_I'''
    p[0] = Var('int', int(p[1]))
    symbol_table.insert_cte('int', int(p[1]))

def p_cte_f(p):
    '''cte_f : CTE_F'''
    p[0] = Var('float', float(p[1]))
    symbol_table.insert_cte('float', float(p[1]))


def p_cte_string(p):
    '''cte_string : CTE_STRING'''
    p[1] = p[1][1:-1]
    p[0] = Var('string', str(p[1]))
    symbol_table.insert_cte('string',(str(p[1])))


def p_cte_bool(p):
    '''cte_bool : CTE_BOOL'''
    p[0] = Var('bool', bool(p[1]))
    symbol_table.insert_cte('bool', bool(p[1]))


# --- CONTROL ---

def p_loop(p):
    '''loop : LOOP LPAREN expresion RPAREN bloque
            | LOOP CTE_I bloque'''


def p_condicion(p):
    '''condicion : IF if_expresion bloque SEMICOLON
                 | IF if_expresion bloque if_else bloque SEMICOLON'''
    code_generator.fill_gotof()


def p_if_expresion(p):
    '''if_expresion : LPAREN expresion RPAREN'''
    code_generator.gen_gotof(p[2])


def p_if_else(p):
    '''if_else : ELSE'''
    code_generator.gen_if_goto()

# --- FUNCIONES ---

def p_funcion(p):
    '''funcion : DEF tipo funcionAux RETURN expresion SEMICOLON RBRACE
               | DEF VOID funcionAux RBRACE'''
    symbol_table.func_table[p[3]]['type'] = p[2]
    symbol_table.func_table[p[3]]['pos'] = utils.func_start_pos


def p_funcionAux(p):
    '''funcionAux : dec_func end_of_dec_func
                  | dec_func end_of_dec_func funcionAux2'''
    p[0] = p[1]


def p_end_of_dec_func(p):
    '''end_of_dec_func : LBRACE
                       | LBRACE vars'''
    utils.func_start_pos = code_generator.quad_pos()


def p_funcionAux2(p):
    '''funcionAux2 : estatuto
                   | estatuto funcionAux2'''


def p_dec_func(p):
    '''dec_func : func_name LPAREN RPAREN
                | func_name LPAREN dec_func_aux RPAREN'''
    p[0] = p[1]
    utils.context = p[1]
    if (len(p) == 5):
        for var in p[3]:
            symbol_table.insert_local_var(p[1], var['name'], var['type'])


def p_func_name(p):
    '''func_name : ID'''
    p[0] = p[1]
    symbol_table.insert_func(p[1])


def p_dec_func_aux(p):
    '''dec_func_aux : tipo ID
                    | tipo ID COMMA dec_func_aux'''
    if (len(p) == 3):
        p[0] = [{'name': p[2], 'type': p[1]}]
    else:
        p[0] = [{'name': p[2], 'type': p[1]}] + p[4]


def p_func_call(p):
    '''func_call : ID LPAREN RPAREN SEMICOLON
                 | ID LPAREN func_call_aux RPAREN SEMICOLON'''

    # FIXME: should evaluate function and return a value
    p[0] = Var('string', 'fixme')


def p_func_call_var(p):
    '''func_call_var : ID LPAREN RPAREN
                 | ID LPAREN func_call_aux RPAREN'''
    p[0] = Var('string', 'fixme')

def p_func_call_aux(p):
    '''func_call_aux : expresion
                     | expresion COMMA func_call_aux'''


# --- ERRORS ---

def p_error(p):
    global success
    success = False
    print('Error de sintaxis en `%s`' % p.value)
    sys.exit()


# BUILDS PARSER
parser = yacc.yacc(debug=False, write_tables=False)
