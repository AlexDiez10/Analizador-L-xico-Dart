# ------------------------------------------------------------
# calclex.py
#
# tokenizer for a simple expression evaluator for
# numbers and +,-,*,/
# ------------------------------------------------------------
import ply.lex as lex

reserved = {
    'if':'IF',
    'else':'Else',
    'while':'WHILE',
    'for':'FOR',
    'print': 'PRINT'
}

# List of token names.   This is always required
tokens = (
   'NUMBER',
   'FLOAT',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
    'MOD',
    'VARIABLE',
    'POINT',
    'LKEY',
    'RKEY',
    'COMA'
) + tuple(reserved.values())

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_MOD = r'\%'
t_POINT = r'\;'
t_LKEY  = r'\['
t_RKEY  = r'\]'
t_COMA = r'\,'

# A regular expression rule with some action code

def t_FLOAT(t):
    r'\d+\.?\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
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
    3 + 4 * 10 a % _134 while IF 1.4
  + -20 *2print(6.5 + 6);
  print(a);
  [1,2,4]
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)