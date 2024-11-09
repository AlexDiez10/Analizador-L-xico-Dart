# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex
from ply.ctokens import t_DECREMENT, t_INCREMENT, t_MODULO

reserved = {
    'print': 'PRINT'
}

bucles = {
    'while': 'WHILE',
    'for': 'FOR'
}

conditionals = {
    'if': 'IF',
    'else': 'Else',
    'else if' : 'ELSE_IF',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT'
}

type_variables = {
    'final': 'TYPEV_FINAL',
    'const': 'TYPEV_CONST',
    'String': 'TYPEV_VARIABLE',
    'int': 'TYPEV_INT',
    'double': 'TYPEV_DOUBLE',
    'bool': 'TYPEV_BOOLEAN',
    'var': 'TYPEV_VAR',
    'Object' : 'TYPEV_OBJECT',
    'late' : 'TYPEV_LATE',
    'List' : 'TYPEVLIST',
    'Map' : 'TYPEVMAP',
    'Set' : 'TYPEV_SET',
    'enum' : 'ENUM',
    'Queue' : 'QUEUE',
}

# List of token names.   This is always required
tokens = (
    'COMMENT',
    'INT',
    'STRING',
    'DOUBLE',
    'BOOLEAN',
    'NULL',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'LPAREN',
    'RPAREN',
    'MOD',
    'VARIABLE',
    'LKEY',
    'RKEY',
    'LBRACKETS',
    'RBRACKETS',
    'COMA',
    'AND',
    'OR',
    'EQUALITY',
    'INEQUALITY',
    'INCREMENT',
    'DECREMENT',
    'INCREMENT_VAR',
    'DECREMENT_VAR',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_EQ_THAN',
    'LESS_EQ_THAN',
    'SEMICOLON'
) + tuple(reserved.values()) + tuple(bucles.values()) + tuple(conditionals.values()) + tuple(type_variables.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MODULO = r'\%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD = r'\%'
t_LKEY  = r'\{'
t_RKEY  = r'\}'
t_LBRACKETS = r'\['
t_RBRACKETS = r'\]'
t_COMA = r'\,'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQUALITY = r'\=\='
t_INEQUALITY = r'\!\='
t_INCREMENT = r'\+\='
t_DECREMENT = r'\-\='
t_INCREMENT_VAR = r'\+\+'
t_DECREMENT_VAR = r'\-\-'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_EQ_THAN = r'\>\='
t_LESS_EQ_THAN = r'\<\='
t_SEMICOLON = r'\;'

# A regular expression rule with some action code

def t_COMMENT(t):
    r'(\/\/[a-zA-Z0-9 ]+ | \/\*[a-zA-Z0-9 ]+\*\/)'
    return t

def t_NULL(t):
    r'null'
    return t

def t_BOOLEAN(t):
    r'(True|False)'
    if(t.value == 'True'):
        t.value = True
        return t
    t.value = False
    return t

def t_STRING(t):
    r'\'[a-zA-Z0-9]+\''
    return t

def t_DOUBLE(t):
    r'\d+\.?\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-z_0-9]*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
    const final int float String null && || != == += -=
    //HOLA
    /* Hola */
    a++
    b-- a
    > < >= <= ;
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)