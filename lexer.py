import ply.lex as lex

# Lista de tokens
tokens = (
    'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'LPAREN', 'RPAREN',
    'IF', 'ELSE', 'WHILE'
)

# Palabras clave
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE'
}

# Reglas de tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Caracter ilegal: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()
