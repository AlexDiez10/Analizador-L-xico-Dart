import ply.yacc as yacc
from analizador_lexico import tokens

def p_programa(p):
    '''programa : sentencias
                | sentencias programa'''
    pass

def p_sentencias(p):
    '''sentencias : list
                  | asignacion
                  | impresion
                  | comparacion_logica
                  | operacionAritmetica
                  | condicional
                  | definicion
                  | sentencias sentencias
                  | funcion_void
                  | declaracion'''
    pass
def p_asignacion(p):
    '''asignacion : datos VARIABLE ASSIGN operacionAritmetica SEMICOLON
                 | datos VARIABLE ASSIGN comparacion SEMICOLON'''
    print("Asignación válida")

def p_definicion(p):
    '''definicion : VARIABLE ASSIGN operacionAritmetica SEMICOLON
                 | VARIABLE ASSIGN comparacion SEMICOLON'''
    
def p_declaracion(p):
    '''declaracion : datos VARIABLE SEMICOLON'''
    print("Declaración válida")

def p_impresion(p):
    '''impresion : PRINT LPAREN operacionAritmetica RPAREN SEMICOLON
                 | PRINT LPAREN comparacion_logica RPAREN SEMICOLON
                 | PRINT LPAREN RPAREN SEMICOLON'''
    print("Impresión válida")
def p_valor(p):
    '''valor : INT
            | VARIABLE
            | DOUBLE
            | STRING'''

def p_valor_bol(p):
    '''valor : BOOLEAN'''

def p_comparacion(p):
    '''comparacion : valor comparador valor'''

def p_comparacion_logica(p):
    '''comparacion_logica : comparacion
                          | comparacion_logica AND comparacion_logica
                          | comparacion_logica OR comparacion_logica'''

def p_comparador(p):
    '''comparador : EQUALITY
                    | INEQUALITY
                    | GREATER_THAN
                    | LESS_THAN
                    | GREATER_EQ_THAN
                    | LESS_EQ_THAN'''

def p_operacionAritmetica(p):
    '''operacionAritmetica : valor
                           | valor operador operacionAritmetica'''
def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''

def p_list(t):
    '''list : listita VARIABLE ASSIGN LBRACKETS element_list RBRACKETS SEMICOLON
            | listita VARIABLE ASSIGN LBRACKETS RBRACKETS SEMICOLON
            | VAR VARIABLE ASSIGN LBRACKETS RBRACKETS SEMICOLON
            | VAR VARIABLE ASSIGN LBRACKETS element_list RBRACKETS SEMICOLON''' 
    print("Estructura de datos: Lista válida")

def p_listita(t):
    '''listita : LIST LESS_THAN datos GREATER_THAN '''

def p_element_list(t):
    '''element_list : element
                    | element_list COMA element'''

def p_element(t):
    '''element : INT
               | STRING
               | DOUBLE
               | BOOLEAN
               | LBRACKETS element_list RBRACKETS'''  

def p_datos(t):
    '''datos : INT_TYPE
             | STRING_TYPE
             | DOUBLE_TYPE
             | BOOL_TYPE
             | listita'''

def p_condicional(p):
    '''condicional : IF LPAREN comparacion RPAREN LKEY sentencias RKEY bloques_else'''
    print("Estructura de control: if else válida")

def p_bloques_else(p):
    '''bloques_else : ELSE IF LPAREN comparacion RPAREN LKEY sentencias RKEY bloques_else
                    | ELSE LKEY sentencias RKEY
                    | empty'''
    
def p_funcion_void(p):
    '''funcion_void : VOID VARIABLE LPAREN parametros RPAREN LKEY sentencias RKEY
                    | VOID VARIABLE LPAREN empty RPAREN LKEY sentencias RKEY'''
    print("Función void válida")

def p_parametros(p):
    '''parametros : datos VARIABLE 
                  | datos VARIABLE COMA parametros'''

def p_empty(p):
    '''empty : '''
    pass

def p_error(t):
    if t:
        print(f"Error de sintaxis en el token '{t.value}' en la línea {t.lineno}")
    else:
        print("Error de sintaxis en la entrada")

parser = yacc.yacc()