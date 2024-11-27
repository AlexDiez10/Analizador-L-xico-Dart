import ply.yacc as yacc
from analizador_lexico import tokens

def p_programa(p):
    '''programa : sentencias
                | sentencias programa'''
    pass

def p_sentencias(p):
    '''sentencias : asignar_variable
                  | funcion
                  | class
                  | import'''
    pass

def p_sentencias_funcion(p):
    '''sentencias_funcion : asignar_variable
                        | cambiar_variable
                        | impresion
                        | condicional
                        | retorno
                        | while
                        | do_while
                        | for
                        | for_each
                        | invocacion'''

def p_cuerpo_funcion(p):
    '''cuerpo_funcion : sentencias_funcion
                        | sentencias_funcion cuerpo_funcion'''

def p_sentencias_clase(p):
     '''sentencias_clase : asignar_variable
                        | cambiar_variable
                        | funcion
                        | constructor
                        | funcion_static'''

def p_cuerpo_clase(p):
    '''cuerpo_clase : sentencias_clase
                    | sentencias_clase cuerpo_clase'''

def p_invocacion(p):
    '''invocacion : VARIABLE LPAREN element_list RPAREN SEMICOLON
                | VARIABLE LPAREN RPAREN SEMICOLON
                | VARIABLE DOT VARIABLE LPAREN element_list RPAREN SEMICOLON
                | VARIABLE DOT VARIABLE LPAREN RPAREN SEMICOLON'''
    print('Invocacion valida')
    
def p_invocar(p):
    '''invocar : VARIABLE LPAREN element_list RPAREN
                | VARIABLE LPAREN RPAREN'''

def p_constructor(p):
    '''constructor : VARIABLE LPAREN atributo_list RPAREN SEMICOLON'''

def p_atributo_list(p):
    '''atributo_list : THIS DOT VARIABLE
                    | THIS DOT VARIABLE COMA atributo_list'''

def p_funcion(p): #Jesus Suarez
    '''funcion : tipo_dato VARIABLE LPAREN parametros RPAREN LKEY cuerpo_funcion RKEY
                | tipo_dato VARIABLE LPAREN RPAREN LKEY cuerpo_funcion RKEY'''
    print("Función válida")

def p_funcion_static(p): #Jesus Suarez
    '''funcion_static : STATIC tipo_dato VARIABLE LPAREN parametros RPAREN LKEY cuerpo_funcion RKEY
                | STATIC tipo_dato VARIABLE LPAREN RPAREN LKEY cuerpo_funcion RKEY'''
    print("Función estatica válida")

def p_variables(p):
    '''variables : VARIABLE
                 | variable_indexada'''

def p_asignar_variable(p):
    '''asignar_variable : tipo_dato variables asignador expresion SEMICOLON
                        | tipo_dato variables SEMICOLON
                        | FINAL_TYPE tipo_dato variables asignador expresion SEMICOLON
                        | FINAL_TYPE tipo_dato variables SEMICOLON '''
    print("Asignación válida")

def p_cambiar_variable(p):
    '''cambiar_variable : variables modificador SEMICOLON
                        | variables asignador expresion SEMICOLON'''
    print("Cambio de variable válido")

def p_modificador(p):
    '''modificador : INCREMENT_VAR
                    | DECREMENT_VAR'''

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
                    | set
                    | input
                    | invocar
                    | variable_indexada'''

def p_retorno(p):
    '''retorno : RETURN SEMICOLON
                | RETURN expresion SEMICOLON'''
    print("Retorno válido")

def p_variable_indexada(p):
    '''variable_indexada : VARIABLE LBRACKETS inmutables RBRACKETS'''
    print("Indexacion valida")

def p_import(p):
    '''import : IMPORT STRING SEMICOLON'''
    print("Import válido")

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
            | DOUBLE
            | STRING
            | BOOLEAN
            | get_variable'''

def p_get_variable(p):
    '''get_variable : VARIABLE
                    | VARIABLE DOT get_variable'''

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

def p_list(t): #Jesus Suarez
    '''list : LBRACKETS element_list RBRACKETS
            | LBRACKETS RBRACKETS'''
    print("Estructura de datos: Lista válida")

def p_element_list(t):
    '''element_list : elemento
                    | elemento COMA element_list'''

def p_tipo_dato(t):
    '''tipo_dato : VOID
             | VARIABLE 
             | FINAL_TYPE
             | CONST_TYPE
             | VAR_TYPE
             | INT_TYPE
             | STRING_TYPE
             | DOUBLE_TYPE
             | BOOL_TYPE
             | LIST LESS_THAN tipo_coleccion GREATER_THAN
             | MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THAN
             | SET LESS_THAN tipo_coleccion GREATER_THAN'''

def p_tipo_coleccion(t):
    '''tipo_coleccion : INT_TYPE
             | STRING_TYPE
             | DOUBLE_TYPE
             | FINAL_TYPE
             | CONST_TYPE
             | VAR_TYPE
             | BOOL_TYPE'''

def p_for(p): #Alejandro Diez
    '''for  : FOR LPAREN asignar_variable comparacion_logica SEMICOLON VARIABLE modificador RPAREN LKEY cuerpo_funcion RKEY
            | FOR LPAREN SEMICOLON comparacion_logica SEMICOLON VARIABLE modificador RPAREN LKEY cuerpo_funcion RKEY
            | FOR LPAREN SEMICOLON SEMICOLON VARIABLE modificador RPAREN LKEY cuerpo_funcion RKEY'''
    print("Estructura de control: for válida")

def p_for_each(p):
    '''for_each : FOR LPAREN tipo_dato VARIABLE IN VARIABLE RPAREN LKEY cuerpo_funcion RKEY
                | FOR LPAREN tipo_dato VARIABLE IN VARIABLE DOT VARIABLE RPAREN LKEY cuerpo_funcion RKEY
                | FOR LPAREN tipo_dato VARIABLE LPAREN specific_instance RPAREN IN VARIABLE RPAREN LKEY cuerpo_funcion RKEY'''
    print("Estructura de control: for each válida")
    
def p_specific_instance(p):
    '''specific_instance    : DOS_PUNTOS VARIABLE
                            | DOS_PUNTOS VARIABLE COMA specific_instance'''    

def p_while(p): #Luis Borja
    '''while : WHILE LPAREN comparacion_logica RPAREN LKEY cuerpo_funcion RKEY
              | WHILE LPAREN get_variable RPAREN LKEY cuerpo_funcion RKEY
              | WHILE LPAREN BOOLEAN RPAREN LKEY cuerpo_funcion RKEY'''
    print("Estructura de control: while válida")

def p_do_while(p): #Luis Borja
    '''do_while : DO LKEY cuerpo_funcion RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLON
                | DO LKEY cuerpo_funcion RKEY WHILE LPAREN get_variable RPAREN SEMICOLON
                | DO LKEY cuerpo_funcion RKEY WHILE LPAREN BOOLEAN RPAREN SEMICOLON'''
    print("Estructura de control: do while válida")

def p_inmutables(p):
    '''inmutables : STRING
             | INT
             | DOUBLE'''

def p_key_element(p):
    '''key_element : inmutables DOS_PUNTOS elemento'''

def p_key_element_list(p):
    '''key_element_list : key_element
                        | key_element COMA key_element_list'''

def p_diccionario(p): #Luis Borja
    '''diccionario : LKEY key_element_list RKEY
                    | LKEY RKEY
                    | DICT LPAREN RPAREN'''
    print("Estructura de datos: Diccionario válido")

def p_set(p):
    '''set : LKEY element_list RKEY
            | CONJUNTO LPAREN RPAREN'''
    print("Estructura de datos: Set válido")

def p_condicional(p): #Jesus Suarez
    '''condicional : IF LPAREN comparacion_logica RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | IF LPAREN comparacion_logica RPAREN LKEY cuerpo_funcion RKEY
                    | IF LPAREN get_variable RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | IF LPAREN get_variable RPAREN LKEY cuerpo_funcion RKEY
                    | IF LPAREN BOOLEAN RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | IF LPAREN BOOLEAN RPAREN LKEY cuerpo_funcion RKEY'''
    print("Estructura de control: if else válida")

def p_bloques_else(p):
    '''bloques_else : ELSE IF LPAREN comparacion_logica RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | ELSE IF LPAREN get_variable RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | ELSE IF LPAREN BOOLEAN RPAREN LKEY cuerpo_funcion RKEY bloques_else
                    | ELSE LKEY cuerpo_funcion RKEY'''
    
def p_parametros(p):
    '''parametros : tipo_dato VARIABLE
                  | tipo_dato VARIABLE COMA parametros'''

def p_class(p):
    '''class : CLASS VARIABLE LKEY cuerpo_clase RKEY'''
    print("Clase válida")

def p_error(t):
    if t:
        # Mostrar el token problemático
        error_message = f"\n[ERROR] Token inesperado: '{t.value}' en la línea {getattr(t, 'lineno', 'desconocida')}"
        
        # Intentar obtener contexto alrededor del error
        if hasattr(t.lexer, "lexdata"):
            start = max(t.lexpos - 20, 0)  # Obtener hasta 20 caracteres antes del error
            end = min(t.lexpos + 20, len(t.lexer.lexdata))  # Obtener hasta 20 caracteres después del error
            context = t.lexer.lexdata[start:end]
            pointer = ' ' * (t.lexpos - start) + '^'  # Marcar el token con '^'
            
            error_message += f"\nContexto:\n{context}\n{pointer}"
        
        print(error_message)
        
        # Ignorar el token problemático
        parser.errok()  # Resetea el estado de error del parser
        t.lexer.skip(1)  # Salta el token problemático

    else:
        print("\n[ERROR] Entrada incompleta o vacía: no se puede continuar el análisis.")


parser = yacc.yacc(debug=True)
