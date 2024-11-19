import ply.yacc as yacc
from analizador_lexico import tokens

def p_programa(p):
    '''programa : sentencias
                | sentencias programa'''
    pass

def p_sentencias(p):
    '''sentencias : asignar_variable
                  | cambiar_variable
                  | impresion
                  | condicional
                  | funcion
                  | retorno
                  | while'''
    pass

def p_asignar_variable(p):
    '''asignar_variable : tipo_dato VARIABLE asignador expresion SEMICOLON
                    | tipo_dato VARIABLE SEMICOLON'''
    print("Asignación válida")

def p_cambiar_variable(p):
    '''cambiar_variable : VARIABLE INCREMENT_VAR SEMICOLON
                        | VARIABLE DECREMENT_VAR SEMICOLON
                        | VARIABLE asignador expresion SEMICOLON'''

def p_asignador(p):
    '''asignador : ASSIGN
                | PLUS_ASSIGN
                | MINUS_ASSIGN
                | TIMES_ASSIGN
                | DIVIDE_ASSIGN
                | MODULO_ASSIGN'''

def p_expresion(p):
    '''expresion : operacion
                    | comparacion
                    | list
                    | diccionario
                    | input'''

def p_retorno(p):
    '''retorno : RETURN SEMICOLON
                | RETURN operacion SEMICOLON'''

def p_impresion(p):
    '''impresion : PRINT LPAREN operacion RPAREN SEMICOLON
                 | PRINT LPAREN comparacion_logica RPAREN SEMICOLON
                 | PRINT LPAREN RPAREN SEMICOLON'''
    print("Impresión válida")

def p_input(p):
    '''input : STDIN DOT READLINESYNC LPAREN RPAREN'''
    print(f"Input valido")

def p_elemento(p):
    '''elemento : INT
            | VARIABLE
            | DOUBLE
            | STRING
            | BOOLEAN'''

def p_comparacion(p):
    '''comparacion : operacion comparador operacion'''

def p_comparacion_logica(p):
    '''comparacion_logica : comparacion
                          | comparacion operador_logico comparacion_logica'''

def p_operador_logico(p):
    '''operador_logico : AND
                        | OR
                        | NOT'''

def p_comparador(p):
    '''comparador : EQUALITY
                    | INEQUALITY
                    | GREATER_THAN
                    | LESS_THAN
                    | GREATER_EQ_THAN
                    | LESS_EQ_THAN'''

def p_operacion(p):
    '''operacion : elemento
                | elemento operador operacion'''
    
def p_operador(p):
    '''operador : PLUS
                | MINUS
                | TIMES
                | DIVIDE
                | MODULO'''

def p_list(t):
    '''list : LBRACKETS element_list RBRACKETS
            | LBRACKETS RBRACKETS'''
    print("Estructura de datos: Lista válida")

def p_element_list(t):
    '''element_list : elemento
                    | elemento COMA element_list'''

def p_tipo_dato(t):
    '''tipo_dato : VAR_TYPE
             | INT_TYPE
             | STRING_TYPE
             | DOUBLE_TYPE
             | BOOL_TYPE
             | LIST LESS_THAN tipo_coleccion GREATER_THAN
             | MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THAN'''

def p_tipo_coleccion(t):
    '''tipo_coleccion : INT_TYPE
             | STRING_TYPE
             | DOUBLE_TYPE
             | BOOL_TYPE'''

def p_while(p):
    '''while : WHILE LPAREN comparacion_logica RPAREN LKEY programa RKEY
                | DO LKEY programa RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLON'''
    print("Estructura de control: while válida")

def p_diccionario(p):
    '''diccionario : LKEY key_element_list RKEY'''

def p_key_element(p):
    '''key_element : elemento DOS_PUNTOS elemento'''

def p_key_element_list(p):
    '''key_element_list : key_element
                        | key_element COMA key_element_list'''

def p_condicional(p):
    '''condicional : IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else
                    | IF LPAREN comparacion_logica RPAREN LKEY programa RKEY'''
    print("Estructura de control: if else válida")

def p_bloques_else(p):
    '''bloques_else : ELSE IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else
                    | ELSE LKEY programa RKEY'''
    
def p_funcion(p):
    '''funcion : VOID VARIABLE LPAREN parametros RPAREN LKEY programa RKEY
                | VOID VARIABLE LPAREN RPAREN LKEY programa RKEY'''
    print("Función válida")

def p_parametros(p):
    '''parametros : tipo_dato VARIABLE
                  | tipo_dato VARIABLE COMA parametros'''

def p_error(t):
    if t:
        print(f"Error de sintaxis en el token '{t.value}' en la línea {t.lineno}")
    else:
        print("Error de sintaxis en la entrada")

parser = yacc.yacc(debug=True)
