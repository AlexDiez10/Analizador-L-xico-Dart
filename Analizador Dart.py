import ply.lex as lex
import os
from datetime import datetime

username = input("Ingrese el nombre de usuario de Git: ")
timestamp = datetime.now().strftime("%d%m%Y-%Hh%M")
log_filename = f"logs/lexico-{username}-{timestamp}.txt"

os.makedirs("logs", exist_ok=True)

with open(log_filename, "w") as log_file:

    reserved = {
        'print':'PRINT',
        'while': 'WHILE',
        'for': 'FOR',
        'if': 'IF',
        'else': 'ELSE',
        'switch': 'SWITCH',
        'case': 'CASE',
        'default': 'DEFAULT',
        'break': 'BREAK',
        'continue': 'CONTINUE',
        'return': 'RETURN',
        'true': 'TRUE',
        'false': 'FALSE',
        'null': 'NULL',
        'void': 'VOID',
        'int': 'INT_TYPE',
        'double': 'DOUBLE_TYPE',
        'String': 'STRING_TYPE',
        'bool': 'BOOL_TYPE',
        'var': 'VAR',
        'final': 'FINAL',
        'const': 'CONST',
        'enum': 'ENUM',
        'class': 'CLASS',
        'new': 'NEW',
        'static': 'STATIC',
        'import': 'IMPORT',
        'export': 'EXPORT',
        'this': 'THIS',
        'super': 'SUPER',
        'extends': 'EXTENDS',
        'implements': 'IMPLEMENTS',
        'with': 'WITH',
        'abstract': 'ABSTRACT',
        'async': 'ASYNC',
        'await': 'AWAIT',
        'required': 'REQUIRED',
        'get': 'GET',
        'set': 'SET',
        'late': 'LATE',
        'covariant': 'COVARIANT',
        'operator': 'OPERATOR',
        'try': 'TRY',
        'catch': 'CATCH',
        'finally': 'FINALLY',
        'throw': 'THROW',
        'rethrow': 'RETHROW',
        'is': 'IS', 
        'as': 'AS',
        'in': 'IN',
        'on': 'ON',
        'assert': 'ASSERT'
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
        'SEMICOLON',
        'ASSIGN',
        'PLUS_ASSIGN',
        'MINUS_ASSIGN',
        'TIMES_ASSIGN',
        'DIVIDE_ASSIGN',
        'MODULO_ASSIGN',
        'LSHIFT_ASSIGN',
        'RSHIFT_ASSIGN',
        'BITWISE_AND_ASSIGN',
        'BITWISE_OR_ASSIGN',
        'BITWISE_XOR_ASSIGN',
        'BITWISE_AND',
        'BITWISE_OR',
        'BITWISE_XOR',
        'BITWISE_NOT',
        'LSHIFT',
        'RSHIFT',
        'TERNARY_IF',
        'TERNARY_ELSE',
        'NULL_COALESCING',
        'NULL_COALESCING_ASSIGN'
    ) + tuple(reserved.values())


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
    t_EQUALITY = r'=='
    t_INEQUALITY = r'\!='
    t_INCREMENT_VAR = r'\+\+'
    t_DECREMENT_VAR = r'--'
    t_GREATER_THAN = r'\>'
    t_LESS_THAN = r'\<'
    t_GREATER_EQ_THAN = r'\>='
    t_LESS_EQ_THAN = r'\<='
    t_SEMICOLON = r'\;'

    t_ASSIGN = r'='
    t_PLUS_ASSIGN = r'\+='
    t_MINUS_ASSIGN = r'-='
    t_TIMES_ASSIGN = r'\*='
    t_DIVIDE_ASSIGN = r'/='
    t_MODULO_ASSIGN = r'%='
    t_LSHIFT_ASSIGN = r'<<='
    t_RSHIFT_ASSIGN = r'>>='
    t_BITWISE_AND_ASSIGN = r'&='
    t_BITWISE_OR_ASSIGN = r'\|='
    t_BITWISE_XOR_ASSIGN = r'\^='
    t_BITWISE_AND = r'&'
    t_BITWISE_OR = r'\|'
    t_BITWISE_XOR = r'\^'
    t_BITWISE_NOT = r'~'
    t_LSHIFT = r'<<'
    t_RSHIFT = r'>>'
    t_TERNARY_IF = r'\?'
    t_TERNARY_ELSE = r':'
    t_NULL_COALESCING = r'\?\?'
    t_NULL_COALESCING_ASSIGN = r'\?\?='

    def t_DOC_COMMENT(t):
        r'(///.*|/\*\*[\s\S]*?\*/)'
        t.lexer.lineno += t.value.count("\n")
        return t

    def t_COMMENT(t):
        r'//.*|/\*[\s\S]*?\*/'
        t.lexer.lineno += t.value.count("\n")
        return t

    def t_BOOLEAN(t):
        r'(True|False)'
        if(t.value == 'True'):
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

    def t_error(t):
        error_msg = f"Illegal character '{t.value[0]}' at line {t.lexer.lineno}\n"
        log_file.write(error_msg)
        print(error_msg)
        t.lexer.skip(1)

    lexer = lex.lex()

    data = '''
        const final int float String null && || != == += -=
        //HOLA
        /* 
        Hola 
        */
        ///hola
        ///xd
        a++
        b-- a
        > < >= <= ;
        void main() {
        print("Hello, World!");
    }
    '''

    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        log_entry = f"{tok.type} ({tok.value}) at line {tok.lineno}\n"
        log_file.write(log_entry)
        print(log_entry)