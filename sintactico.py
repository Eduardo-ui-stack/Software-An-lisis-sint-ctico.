import ply.yacc as yacc
from lexer import tokens

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_if(p):
    'expression : IF expression'
    print("Encontrado IF con expresión:", p[2])
    p[0] = p[2]

def p_expression_while(p):
    'expression : WHILE expression'
    print("Encontrado WHILE con expresión:", p[2])
    p[0] = p[2]

def p_error(p):
    print("Error de sintaxis")

parser = yacc.yacc()
