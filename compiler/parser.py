import ply.yacc as yacc
import lexer
import sys

tokens = lexer.tokens

success = True

def p_program(p):
    '''program : PROGRAM ID SEMICOLON main_dec bloque
               | PROGRAM ID SEMICOLON vars main_dec bloque
               | PROGRAM ID SEMICOLON funciones main_dec bloque
               | PROGRAM ID SEMICOLON vars funciones main_dec bloque'''


def p_funciones(p):
    '''funciones : funcion
                  | funcion funciones'''


def p_main_dec(p):
    '''main_dec : MAIN LPAREN RPAREN'''


def p_vars(p):
    '''vars : VAR varAux1'''


def p_varAux1(p):
    '''varAux1 : tipo varAux2 SEMICOLON
               | tipo varAux2 SEMICOLON varAux1'''


def p_varAux2(p):
    '''varAux2 : ID
               | ID COMMA varAux2
               | ID EQUAL expresion
               | ID EQUAL expresion COMMA varAux2'''


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


def p_condicion(p):
    '''condicion : IF LPAREN expresion RPAREN bloque SEMICOLON
                 | IF LPAREN expresion RPAREN bloque ELSE bloque SEMICOLON'''


def p_escritura(p):
    '''escritura : PRINT LPAREN escrituraAux RPAREN SEMICOLON'''


def p_escrituraAux(p):
    '''escrituraAux : expresion
                    | expresion COMMA escrituraAux'''


def p_expresion(p):
    '''expresion : exp2
                 | exp2 AND expresion
                 | exp2 OR expresion'''


def p_exp2(p):
    '''exp2 : exp3
            | exp3 LT exp3
            | exp3 LTE exp3
            | exp3 GT exp3
            | exp3 GTE exp3
            | exp3 EQUALEQUAL exp3
            | exp3 NOTEQUAL exp3'''


def p_exp3(p):
    '''exp3 : termino
            | termino PLUS exp3
            | termino MINUS exp3'''


def p_termino(p):
    '''termino : factor
               | factor TIMES termino
               | factor DIVIDE termino'''


def p_factor(p):
    '''factor : LPAREN expresion RPAREN
              | factorAux'''


def p_factorAux(p):
    '''factorAux : PLUS var_cte
                 | MINUS var_cte
                 | NOT var_cte
                 | var_cte'''


def p_var_cte(p):
    '''var_cte : ID
               | CTE_I
               | CTE_BOOL
               | CTE_F
               | CTE_STRING
               | func_call
               '''


def p_loop(p):
    '''loop : LOOP LPAREN expresion RPAREN bloque
            | LOOP CTE_I bloque'''


def p_funcion(p):
    '''funcion : DEF tipo funcionAux RETURN expresion SEMICOLON RBRACE
               | DEF VOID funcionAux RBRACE'''


def p_funcionAux(p):
    '''funcionAux : dec_func LBRACE
                  | dec_func LBRACE vars
                  | dec_func LBRACE funcionAux2
                  | dec_func LBRACE vars funcionAux2'''


def p_funcionAux2(p):
    '''funcionAux2 : estatuto
                   | estatuto funcionAux2'''


def p_dec_func(p):
    '''dec_func : ID LPAREN RPAREN
                | ID LPAREN dec_func_aux RPAREN'''


def p_dec_func_aux(p):
    '''dec_func_aux : tipo ID
                    | tipo ID COMMA dec_func_aux'''


def p_func_call(p):
    '''func_call : ID LPAREN RPAREN SEMICOLON
                 | ID LPAREN func_call_aux RPAREN SEMICOLON'''


def p_func_call_aux(p):
    '''func_call_aux : expresion
                     | expresion COMMA func_call_aux'''


def p_error(p):
    global success
    success = False
    print("Error de sintaxis en '%s'" % p.value)
    sys.exit()


parser = yacc.yacc()

archivo = "prueba1.txt"
f = open(archivo, 'r')
s = f.read()

parser.parse(s)

if success == True:
    print("Archivo aprobado")
    sys.exit()
else:
    print("Archivo no aprobado")
    sys.exit()
