import ply.yacc as yacc
import lexer
import symbol_table
from symbol_table import Var
import sys
import code_generator
import utils
import pprint

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
    symbol_table.insert_func('global')

def p_funciones(p):
    '''funciones : funcion
                 | funcion funciones'''

def p_main_dec(p):
    '''main_dec : main_init LPAREN RPAREN bloque
                | main_init LPAREN RPAREN LBRACE vars main_aux RBRACE'''
    code_generator.gen_quad('ENDPROG', '', '', '')

def p_main_aux(p):
    '''main_aux : estatuto
                | estatuto main_aux'''

def p_main_init(p):
    '''main_init : MAIN'''
    utils.context = 'main'
    symbol_table.insert_func('main')
    code_generator.mod_quad(0, 4, code_generator.quad_pos())
    symbol_table.func_dir['main']['pos'] = code_generator.quad_pos()

def p_vars(p):
    '''vars : VAR varAux1'''

def p_varAux1(p):
    '''varAux1 : tipo varAux2 SEMICOLON
               | tipo varAux2 SEMICOLON varAux1'''
    for var in p[2]:
        if (utils.context == 'global'):
            symbol_table.insert_global_var(var['name'], p[1], var['value'], var['type'])
        else:
            symbol_table.insert_local_var(utils.context, var['name'], p[1], var['value'], var['type'])

def p_varAux2(p):
    '''varAux2 : ID
               | ID COMMA varAux2
               | ID EQUAL expresion
               | ID EQUAL expresion COMMA varAux2'''
    if (len(p) == 2):
        p[0] = [{'name': p[1], 'value': None, 'type': None}]
    elif (len(p) == 4):
        if (p[2] == ','):
            p[0] = [{'name': p[1], 'value': None, 'type': None}] + p[3]
        else:
            p[0] = [{'name': p[1], 'value': p[3].value, 'type': p[3].type}]
    else:
        p[0] = [{'name': p[1], 'value': p[3].value, 'type': p[3].type}] + p[5]

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
                | func_call
                | function_return'''

def p_asignacion(p):
    '''asignacion : ID EQUAL expresion SEMICOLON'''
    var = utils.id_lookup(p[1])
    code_generator.gen_quad_assig(var, p[3])

def p_escritura(p):
    '''escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON'''
    for exp in p[3]:
        code_generator.gen_quad_addr('PRINT', '', '', exp.addr)
        code_generator.gen_quad_name('PRINT', '', '', exp.value)

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
    '''factor : paren_exp
              | factor_aux'''
    p[0] = p[1]

def p_paren_exp(p):
    '''paren_exp : LPAREN expresion RPAREN'''
    p[0] = p[2]

def p_factor_aux(p):
    '''factor_aux : unary_plus
                  | unary_minus
                  | unary_not
                  | var_cte'''
    p[0] = p[1]

def p_unary_plus(p):
    '''unary_plus : PLUS var_cte
                  | PLUS paren_exp'''
    p[0] = code_generator.gen_quad_exp('unary+', p[2], Var('',''))

def p_unary_minus(p):
    '''unary_minus : MINUS var_cte
                   | MINUS paren_exp'''
    p[0] = code_generator.gen_quad_exp('unary-', p[2], Var('',''))

def p_unary_not(p):
    '''unary_not : NOT var_cte
                 | NOT paren_exp'''
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
    p[0] = utils.id_lookup(p[1])

def p_cte_i(p):
    '''cte_i : CTE_I'''
    addr = symbol_table.insert_cte('int', int(p[1]))
    p[0] = Var('int', int(p[1]), addr)

def p_cte_f(p):
    '''cte_f : CTE_F'''
    addr = symbol_table.insert_cte('float', float(p[1]))
    p[0] = Var('float', float(p[1]), addr)

def p_cte_string(p):
    '''cte_string : CTE_STRING'''
    p[1] = p[1][1:-1]
    addr = symbol_table.insert_cte('string', str(p[1]))
    p[0] = Var('string', str(p[1]), addr)

def p_cte_bool(p):
    '''cte_bool : CTE_BOOL'''
    addr = symbol_table.insert_cte('bool', bool(p[1]))
    p[0] = Var('bool', bool(p[1]), addr)


# --- CONTROL ---

def p_loop(p):
    '''loop : while
            | repeat'''

def p_repeat(p):
    '''repeat : repeat_exp bloque'''
    code_generator.fill_repeat()

def p_repeat_exp(p):
    '''repeat_exp : REPEAT cte_i'''
    code_generator.gen_repeat(p[2])

def p_while(p):
    '''while : while_begin while_exp bloque'''
    code_generator.fill_while()

def p_while_begin(p):
    '''while_begin : WHILE'''
    code_generator.init_while()

def p_while_exp(p):
    '''while_exp : LPAREN expresion RPAREN'''
    code_generator.gen_gotof(p[2])

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
    '''funcion : type_func RBRACE
               | void_func RBRACE'''
    symbol_table.func_dir[p[1]]['pos'] = utils.func_start_pos
    code_generator.gen_quad('ENDPROC', '', '', '')

def p_type_func(p):
    '''type_func : set_type funcionAux'''
    p[0] = p[1]

def p_set_type(p):
    '''set_type : DEF tipo dec_func'''
    symbol_table.func_dir[p[3]]['pos'] = code_generator.quad_pos()
    symbol_table.func_dir[p[3]]['type'] = p[2]
    symbol_table.insert_global_var(p[3], p[2])
    p[0] = p[3]

def p_void_func(p):
    '''void_func : set_void funcionAux'''
    p[0] = p[1]

def p_set_void(p):
    '''set_void : DEF VOID dec_func'''
    symbol_table.func_dir[p[3]]['pos'] = code_generator.quad_pos()
    p[0] = p[3]

def p_function_return(p):
    '''function_return : RETURN expresion SEMICOLON'''
    code_generator.gen_return(p[2])
    code_generator.gen_quad('ENDPROC', '', '', '')

def p_funcionAux(p):
    '''funcionAux : end_of_dec_func
                  | end_of_dec_func funcionAux2'''
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
            symbol_table.insert_param(p[1], var['name'], var['type'])

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
    '''func_call : func_call_var SEMICOLON'''
    p[0] = p[1]

def p_func_call_var(p):
    '''func_call_var : func_call_begin LPAREN RPAREN
                     | func_call_begin LPAREN func_call_aux RPAREN'''
    if (len(p) > 4):
        code_generator.fill_params(p[3])
    else:
        code_generator.fill_params([])
    jump = symbol_table.func_dir[p[1]]['pos']
    code_generator.gen_gosub(jump)
    if (symbol_table.func_dir[p[1]]['type'] == 'void'):
        p[0] = p[1]
    else:
        p[0] = utils.id_lookup(p[1])
        p[0] = code_generator.get_return(p[1])

def p_func_call_begin(p):
    '''func_call_begin : ID'''
    code_generator.gen_era(p[1])
    p[0] = p[1]

def p_func_call_aux(p):
    '''func_call_aux : expresion
                     | expresion COMMA func_call_aux'''
    if (len(p)==2):
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]


# --- ERRORS ---

def p_error(p):
    global success
    success = False
    print('Error de sintaxis en `%s`' % p.value)
    sys.exit()


# BUILDS PARSER
parser = yacc.yacc(debug=False, write_tables=False)
