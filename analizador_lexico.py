import ply.lex as lex


reserved = {
    'print':'PRINT',
    'while': 'WHILE',
    'for': 'FOR',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'void': 'VOID',
    'int': 'INT_TYPE',
    'double': 'DOUBLE_TYPE',
    'String': 'STRING_TYPE',
    'bool': 'BOOL_TYPE',
    'var': 'VAR_TYPE',
    'import': 'IMPORT',
    'Set': 'SET',
    'List': 'LIST',
    'stdin': 'STDIN',
    'readLineSync': 'READLINESYNC',
    'do' : 'DO',
    'Map' : 'MAP'
}


# Lista de nombres de tokens
tokens = (
    'COMMENT',
    'DOC_COMMENT',
    'INT',
    'STRING',
    'DOUBLE',
    'BOOLEAN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MODULO',
    'LPAREN',
    'RPAREN',
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
    'INCREMENT_VAR',
    'DECREMENT_VAR',
    'GREATER_THAN',
    'LESS_THAN',
    'GREATER_EQ_THAN',
    'LESS_EQ_THAN',
    'SEMICOLON',
    'DOT',
    'NOT',
    'ASSIGN',
    'PLUS_ASSIGN',
    'MINUS_ASSIGN',
    'TIMES_ASSIGN',
    'DIVIDE_ASSIGN',
    'MODULO_ASSIGN',
    'DOS_PUNTOS'
) + tuple(reserved.values())


# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_MODULO = r'\%'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LKEY  = r'\{'
t_RKEY  = r'\}'
t_LBRACKETS = r'\['
t_RBRACKETS = r'\]'
t_COMA = r'\,'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_EQUALITY = r'=='
t_INEQUALITY = r'\!='
t_INCREMENT_VAR = r'\+\+'
t_DECREMENT_VAR = r'--'
t_GREATER_THAN = r'\>'
t_LESS_THAN = r'\<'
t_GREATER_EQ_THAN = r'\>='
t_LESS_EQ_THAN = r'\<='
t_SEMICOLON = r'\;'
t_DOS_PUNTOS = r'\:'
t_DOT = r'\.'
t_NOT = r'!'
t_ASSIGN = r'='
t_PLUS_ASSIGN = r'\+='
t_MINUS_ASSIGN = r'-='
t_TIMES_ASSIGN = r'\*='
t_DIVIDE_ASSIGN = r'/='
t_MODULO_ASSIGN = r'%='

def t_DOC_COMMENT(t):
    r'(\/\/\/.*|\/\*\*[\s\S]*?\*\/\*\/)'
    t.lexer.lineno += t.value.count("\n")
    pass

def t_COMMENT(t):
    r'\/\/.*|\/\*[\s\S]*?\*\/'
    t.lexer.lineno += t.value.count("\n")
    pass

def t_BOOLEAN(t):
    r'(true|false)'
    if(t.value == 'true'):
        t.value = True
        return t
    t.value = False
    return t

def t_STRING(t):
    r"(\".*\"|'.*')"
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def buscar_columna(input_data, token):
    line_start = input_data.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

def t_error(t):
    column = buscar_columna(t.lexer.lexdata, t)
    error_msg = f"Caracter ilegal '{t.value[0]}' en la línea {t.lineno}, columna {column}\n"
    print(error_msg)
    t.lexer.skip(1)
    return error_msg


lexer = lex.lex()
