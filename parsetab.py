
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ABSTRACT AND AS ASSERT ASSIGN ASYNC AWAIT BOOLEAN BOOL_TYPE BREAK CASE CATCH CLASS COMA COMMENT CONST CONTINUE COVARIANT DECREMENT_VAR DEFAULT DIVIDE DIVIDE_ASSIGN DO DOC_COMMENT DOS_PUNTOS DOT DOUBLE DOUBLE_TYPE ELSE ENUM EQUALITY EXPORT EXTENDS FINAL FINALLY FOR GET GREATER_EQ_THAN GREATER_THAN IF IMPLEMENTS IMPORT IN INCREMENT_VAR INEQUALITY INT INT_TYPE IS LATE LBRACKETS LESS_EQ_THAN LESS_THAN LIST LKEY LPAREN MAP MINUS MINUS_ASSIGN MODULO MODULO_ASSIGN NEW NOT NULL ON OPERATOR OR PLUS PLUS_ASSIGN PRINT RBRACKETS READLINESYNC REQUIRED RETHROW RETURN RKEY RPAREN SEMICOLON SET STATIC STDIN STRING STRING_TYPE SUPER SWITCH THIS THROW TIMES TIMES_ASSIGN TRY VARIABLE VAR_TYPE VOID WHILE WITHprograma : sentencias\n                | sentencias programasentencias : asignar_variable\n                  | cambiar_variable\n                  | impresion\n                  | condicional\n                  | funcion\n                  | retorno\n                  | whileasignar_variable : tipo_dato VARIABLE asignador expresion SEMICOLON\n                    | tipo_dato VARIABLE SEMICOLONcambiar_variable : VARIABLE INCREMENT_VAR SEMICOLON\n                        | VARIABLE DECREMENT_VAR SEMICOLON\n                        | VARIABLE asignador expresion SEMICOLONasignador : ASSIGN\n                | PLUS_ASSIGN\n                | MINUS_ASSIGN\n                | TIMES_ASSIGN\n                | DIVIDE_ASSIGN\n                | MODULO_ASSIGNexpresion : operacion\n                    | comparacion\n                    | list\n                    | diccionario\n                    | inputretorno : RETURN SEMICOLON\n                | RETURN operacion SEMICOLONimpresion : PRINT LPAREN operacion RPAREN SEMICOLON\n                 | PRINT LPAREN comparacion_logica RPAREN SEMICOLON\n                 | PRINT LPAREN RPAREN SEMICOLONinput : STDIN DOT READLINESYNC LPAREN RPARENelemento : INT\n            | VARIABLE\n            | DOUBLE\n            | STRING\n            | BOOLEANcomparacion : operacion comparador operacioncomparacion_logica : comparacion\n                          | comparacion operador_logico comparacion_logicaoperador_logico : AND\n                        | OR\n                        | NOTcomparador : EQUALITY\n                    | INEQUALITY\n                    | GREATER_THAN\n                    | LESS_THAN\n                    | GREATER_EQ_THAN\n                    | LESS_EQ_THANoperacion : elemento\n                | elemento operador operacionoperador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODULOlist : LBRACKETS element_list RBRACKETS\n            | LBRACKETS RBRACKETSelement_list : elemento\n                    | elemento COMA element_listtipo_dato : VAR_TYPE\n             | INT_TYPE\n             | STRING_TYPE\n             | DOUBLE_TYPE\n             | BOOL_TYPE\n             | LIST LESS_THAN tipo_coleccion GREATER_THAN\n             | MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THANtipo_coleccion : INT_TYPE\n             | STRING_TYPE\n             | DOUBLE_TYPE\n             | BOOL_TYPEwhile : WHILE LPAREN comparacion_logica RPAREN LKEY programa RKEY\n                | DO LKEY programa RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLONdiccionario : LKEY key_element_list RKEYkey_element : elemento DOS_PUNTOS elementokey_element_list : key_element\n                        | key_element COMA key_element_listcondicional : IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else\n                    | IF LPAREN comparacion_logica RPAREN LKEY programa RKEYbloques_else : ELSE IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else\n                    | ELSE LKEY programa RKEYfuncion : VOID VARIABLE LPAREN parametros RPAREN LKEY programa RKEY\n                | VOID VARIABLE LPAREN RPAREN LKEY programa RKEYparametros : tipo_dato VARIABLE\n                  | tipo_dato VARIABLE COMA parametros'
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,7,8,9,10,14,15,18,19,20,21,22,29,30,31,32,33,34,35,36,37,39,47,48,51,52,53,54,61,62,71,72,73,74,75,76,77,87,88,89,90,91,92,93,94,103,105,106,107,108,112,116,118,121,123,124,126,127,129,131,133,141,145,146,148,150,152,154,156,159,160,161,164,166,169,],[11,11,-3,-4,-5,-6,-7,-8,-9,26,38,43,-60,-61,-62,-63,-64,43,-15,-16,-17,-18,-19,-20,43,43,-26,43,11,43,-11,-12,-13,43,43,-27,43,-51,-52,-53,-54,-55,-14,43,-43,-44,-45,-46,-47,-48,-30,43,-40,-41,-42,132,-65,-10,43,43,43,-28,-29,11,11,11,11,43,-66,-78,-82,-71,-77,-81,11,-72,43,-80,11,-79,]),'PRINT':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,118,126,127,129,131,133,141,148,150,152,154,156,159,160,164,166,169,],[12,12,-3,-4,-5,-6,-7,-8,-9,-26,12,-11,-12,-13,-27,-14,-30,-10,-28,-29,12,12,12,12,-78,-82,-71,-77,-81,12,-72,-80,12,-79,]),'IF':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,118,126,127,129,131,133,141,148,150,152,154,155,156,159,160,164,166,169,],[13,13,-3,-4,-5,-6,-7,-8,-9,-26,13,-11,-12,-13,-27,-14,-30,-10,-28,-29,13,13,13,13,-78,-82,-71,-77,158,-81,13,-72,-80,13,-79,]),'VOID':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,118,126,127,129,131,133,141,148,150,152,154,156,159,160,164,166,169,],[14,14,-3,-4,-5,-6,-7,-8,-9,-26,14,-11,-12,-13,-27,-14,-30,-10,-28,-29,14,14,14,14,-78,-82,-71,-77,-81,14,-72,-80,14,-79,]),'RETURN':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,118,126,127,129,131,133,141,148,150,152,154,156,159,160,164,166,169,],[15,15,-3,-4,-5,-6,-7,-8,-9,-26,15,-11,-12,-13,-27,-14,-30,-10,-28,-29,15,15,15,15,-78,-82,-71,-77,-81,15,-72,-80,15,-79,]),'WHILE':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,115,118,126,127,129,131,133,141,148,150,152,154,156,159,160,164,166,169,],[16,16,-3,-4,-5,-6,-7,-8,-9,-26,16,-11,-12,-13,-27,-14,-30,134,-10,-28,-29,16,16,16,16,-78,-82,-71,-77,-81,16,-72,-80,16,-79,]),'DO':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,71,87,103,118,126,127,129,131,133,141,148,150,152,154,156,159,160,164,166,169,],[17,17,-3,-4,-5,-6,-7,-8,-9,-26,17,-11,-12,-13,-27,-14,-30,-10,-28,-29,17,17,17,17,-78,-82,-71,-77,-81,17,-72,-80,17,-79,]),'VAR_TYPE':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,70,71,87,103,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[18,18,-3,-4,-5,-6,-7,-8,-9,-26,18,-11,-12,-13,18,-27,-14,-30,-10,-28,-29,18,18,18,18,18,-78,-82,-71,-77,-81,18,-72,-80,18,-79,]),'INT_TYPE':([0,2,3,4,5,6,7,8,9,39,48,49,50,52,53,54,70,71,87,103,117,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[19,19,-3,-4,-5,-6,-7,-8,-9,-26,19,81,81,-11,-12,-13,19,-27,-14,-30,81,-10,-28,-29,19,19,19,19,19,-78,-82,-71,-77,-81,19,-72,-80,19,-79,]),'STRING_TYPE':([0,2,3,4,5,6,7,8,9,39,48,49,50,52,53,54,70,71,87,103,117,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[20,20,-3,-4,-5,-6,-7,-8,-9,-26,20,82,82,-11,-12,-13,20,-27,-14,-30,82,-10,-28,-29,20,20,20,20,20,-78,-82,-71,-77,-81,20,-72,-80,20,-79,]),'DOUBLE_TYPE':([0,2,3,4,5,6,7,8,9,39,48,49,50,52,53,54,70,71,87,103,117,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[21,21,-3,-4,-5,-6,-7,-8,-9,-26,21,83,83,-11,-12,-13,21,-27,-14,-30,83,-10,-28,-29,21,21,21,21,21,-78,-82,-71,-77,-81,21,-72,-80,21,-79,]),'BOOL_TYPE':([0,2,3,4,5,6,7,8,9,39,48,49,50,52,53,54,70,71,87,103,117,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[22,22,-3,-4,-5,-6,-7,-8,-9,-26,22,84,84,-11,-12,-13,22,-27,-14,-30,84,-10,-28,-29,22,22,22,22,22,-78,-82,-71,-77,-81,22,-72,-80,22,-79,]),'LIST':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,70,71,87,103,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[23,23,-3,-4,-5,-6,-7,-8,-9,-26,23,-11,-12,-13,23,-27,-14,-30,-10,-28,-29,23,23,23,23,23,-78,-82,-71,-77,-81,23,-72,-80,23,-79,]),'MAP':([0,2,3,4,5,6,7,8,9,39,48,52,53,54,70,71,87,103,118,126,127,129,131,133,141,143,148,150,152,154,156,159,160,164,166,169,],[24,24,-3,-4,-5,-6,-7,-8,-9,-26,24,-11,-12,-13,24,-27,-14,-30,-10,-28,-29,24,24,24,24,24,-78,-82,-71,-77,-81,24,-72,-80,24,-79,]),'$end':([1,2,3,4,5,6,7,8,9,25,39,52,53,54,71,87,103,118,126,127,148,150,152,154,156,160,164,169,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-2,-26,-11,-12,-13,-27,-14,-30,-10,-28,-29,-78,-82,-71,-77,-81,-72,-80,-79,]),'RKEY':([2,3,4,5,6,7,8,9,25,39,42,43,44,45,46,52,53,54,71,79,87,98,99,103,118,126,127,137,138,140,142,144,148,149,150,152,154,156,160,162,164,167,169,],[-1,-3,-4,-5,-6,-7,-8,-9,-2,-26,-32,-33,-34,-35,-36,-11,-12,-13,-27,115,-14,122,-75,-30,-10,-28,-29,-76,-74,148,150,152,-78,156,-82,-71,-77,-81,-72,164,-80,168,-79,]),'INCREMENT_VAR':([11,],[27,]),'DECREMENT_VAR':([11,],[28,]),'ASSIGN':([11,26,],[30,30,]),'PLUS_ASSIGN':([11,26,],[31,31,]),'MINUS_ASSIGN':([11,26,],[32,32,]),'TIMES_ASSIGN':([11,26,],[33,33,]),'DIVIDE_ASSIGN':([11,26,],[34,34,]),'MODULO_ASSIGN':([11,26,],[35,35,]),'LPAREN':([12,13,16,38,125,134,158,],[36,37,47,70,139,145,161,]),'SEMICOLON':([15,26,27,28,40,41,42,43,44,45,46,55,56,57,58,59,60,65,86,96,102,104,113,119,120,122,147,157,],[39,52,53,54,71,-49,-32,-33,-34,-35,-36,87,-21,-22,-23,-24,-25,103,118,-57,126,127,-50,-37,-56,-73,-31,160,]),'INT':([15,29,30,31,32,33,34,35,36,37,47,51,61,62,72,73,74,75,76,77,88,89,90,91,92,93,94,105,106,107,108,121,123,124,145,161,],[42,42,-15,-16,-17,-18,-19,-20,42,42,42,42,42,42,42,-51,-52,-53,-54,-55,42,-43,-44,-45,-46,-47,-48,42,-40,-41,-42,42,42,42,42,42,]),'DOUBLE':([15,29,30,31,32,33,34,35,36,37,47,51,61,62,72,73,74,75,76,77,88,89,90,91,92,93,94,105,106,107,108,121,123,124,145,161,],[44,44,-15,-16,-17,-18,-19,-20,44,44,44,44,44,44,44,-51,-52,-53,-54,-55,44,-43,-44,-45,-46,-47,-48,44,-40,-41,-42,44,44,44,44,44,]),'STRING':([15,29,30,31,32,33,34,35,36,37,47,51,61,62,72,73,74,75,76,77,88,89,90,91,92,93,94,105,106,107,108,121,123,124,145,161,],[45,45,-15,-16,-17,-18,-19,-20,45,45,45,45,45,45,45,-51,-52,-53,-54,-55,45,-43,-44,-45,-46,-47,-48,45,-40,-41,-42,45,45,45,45,45,]),'BOOLEAN':([15,29,30,31,32,33,34,35,36,37,47,51,61,62,72,73,74,75,76,77,88,89,90,91,92,93,94,105,106,107,108,121,123,124,145,161,],[46,46,-15,-16,-17,-18,-19,-20,46,46,46,46,46,46,46,-51,-52,-53,-54,-55,46,-43,-44,-45,-46,-47,-48,46,-40,-41,-42,46,46,46,46,46,]),'LKEY':([17,29,30,31,32,33,34,35,51,109,111,114,130,155,165,],[48,62,-15,-16,-17,-18,-19,-20,62,129,131,133,141,159,166,]),'LESS_THAN':([23,24,41,42,43,44,45,46,56,64,69,113,],[49,50,-49,-32,-33,-34,-35,-36,92,92,92,-50,]),'LBRACKETS':([29,30,31,32,33,34,35,51,],[61,-15,-16,-17,-18,-19,-20,61,]),'STDIN':([29,30,31,32,33,34,35,51,],[63,-15,-16,-17,-18,-19,-20,63,]),'RPAREN':([36,41,42,43,44,45,46,64,66,67,68,70,78,110,113,119,128,132,139,151,153,163,],[65,-49,-32,-33,-34,-35,-36,102,104,-38,109,111,114,130,-50,-37,-39,-83,147,-84,157,165,]),'EQUALITY':([41,42,43,44,45,46,56,64,69,113,],[-49,-32,-33,-34,-35,-36,89,89,89,-50,]),'INEQUALITY':([41,42,43,44,45,46,56,64,69,113,],[-49,-32,-33,-34,-35,-36,90,90,90,-50,]),'GREATER_THAN':([41,42,43,44,45,46,56,64,69,80,81,82,83,84,113,135,],[-49,-32,-33,-34,-35,-36,91,91,91,116,-67,-68,-69,-70,-50,146,]),'GREATER_EQ_THAN':([41,42,43,44,45,46,56,64,69,113,],[-49,-32,-33,-34,-35,-36,93,93,93,-50,]),'LESS_EQ_THAN':([41,42,43,44,45,46,56,64,69,113,],[-49,-32,-33,-34,-35,-36,94,94,94,-50,]),'AND':([41,42,43,44,45,46,67,113,119,],[-49,-32,-33,-34,-35,-36,106,-50,-37,]),'OR':([41,42,43,44,45,46,67,113,119,],[-49,-32,-33,-34,-35,-36,107,-50,-37,]),'NOT':([41,42,43,44,45,46,67,113,119,],[-49,-32,-33,-34,-35,-36,108,-50,-37,]),'PLUS':([41,42,43,44,45,46,],[73,-32,-33,-34,-35,-36,]),'MINUS':([41,42,43,44,45,46,],[74,-32,-33,-34,-35,-36,]),'TIMES':([41,42,43,44,45,46,],[75,-32,-33,-34,-35,-36,]),'DIVIDE':([41,42,43,44,45,46,],[76,-32,-33,-34,-35,-36,]),'MODULO':([41,42,43,44,45,46,],[77,-32,-33,-34,-35,-36,]),'COMA':([42,43,44,45,46,81,82,83,84,85,97,99,132,138,],[-32,-33,-34,-35,-36,-67,-68,-69,-70,117,121,123,143,-74,]),'RBRACKETS':([42,43,44,45,46,61,95,97,136,],[-32,-33,-34,-35,-36,96,120,-58,-59,]),'DOS_PUNTOS':([42,43,44,45,46,100,],[-32,-33,-34,-35,-36,124,]),'DOT':([63,],[101,]),'READLINESYNC':([101,],[125,]),'ELSE':([148,168,],[155,155,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,48,129,131,133,141,159,166,],[1,25,79,140,142,144,149,162,167,]),'sentencias':([0,2,48,129,131,133,141,159,166,],[2,2,2,2,2,2,2,2,2,]),'asignar_variable':([0,2,48,129,131,133,141,159,166,],[3,3,3,3,3,3,3,3,3,]),'cambiar_variable':([0,2,48,129,131,133,141,159,166,],[4,4,4,4,4,4,4,4,4,]),'impresion':([0,2,48,129,131,133,141,159,166,],[5,5,5,5,5,5,5,5,5,]),'condicional':([0,2,48,129,131,133,141,159,166,],[6,6,6,6,6,6,6,6,6,]),'funcion':([0,2,48,129,131,133,141,159,166,],[7,7,7,7,7,7,7,7,7,]),'retorno':([0,2,48,129,131,133,141,159,166,],[8,8,8,8,8,8,8,8,8,]),'while':([0,2,48,129,131,133,141,159,166,],[9,9,9,9,9,9,9,9,9,]),'tipo_dato':([0,2,48,70,129,131,133,141,143,159,166,],[10,10,10,112,10,10,10,10,112,10,10,]),'asignador':([11,26,],[29,51,]),'operacion':([15,29,36,37,47,51,72,88,105,145,161,],[40,56,64,69,69,56,113,119,69,69,69,]),'elemento':([15,29,36,37,47,51,61,62,72,88,105,121,123,124,145,161,],[41,41,41,41,41,41,97,100,41,41,41,97,100,138,41,41,]),'expresion':([29,51,],[55,86,]),'comparacion':([29,36,37,47,51,105,145,161,],[57,67,67,67,57,67,67,67,]),'list':([29,51,],[58,58,]),'diccionario':([29,51,],[59,59,]),'input':([29,51,],[60,60,]),'comparacion_logica':([36,37,47,105,145,161,],[66,68,78,128,153,163,]),'operador':([41,],[72,]),'tipo_coleccion':([49,50,117,],[80,85,135,]),'comparador':([56,64,69,],[88,88,88,]),'element_list':([61,121,],[95,136,]),'key_element_list':([62,123,],[98,137,]),'key_element':([62,123,],[99,99,]),'operador_logico':([67,],[105,]),'parametros':([70,143,],[110,151,]),'bloques_else':([148,168,],[154,169,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> sentencias','programa',1,'p_programa','analizador_sintactico.py',5),
  ('programa -> sentencias programa','programa',2,'p_programa','analizador_sintactico.py',6),
  ('sentencias -> asignar_variable','sentencias',1,'p_sentencias','analizador_sintactico.py',10),
  ('sentencias -> cambiar_variable','sentencias',1,'p_sentencias','analizador_sintactico.py',11),
  ('sentencias -> impresion','sentencias',1,'p_sentencias','analizador_sintactico.py',12),
  ('sentencias -> condicional','sentencias',1,'p_sentencias','analizador_sintactico.py',13),
  ('sentencias -> funcion','sentencias',1,'p_sentencias','analizador_sintactico.py',14),
  ('sentencias -> retorno','sentencias',1,'p_sentencias','analizador_sintactico.py',15),
  ('sentencias -> while','sentencias',1,'p_sentencias','analizador_sintactico.py',16),
  ('asignar_variable -> tipo_dato VARIABLE asignador expresion SEMICOLON','asignar_variable',5,'p_asignar_variable','analizador_sintactico.py',20),
  ('asignar_variable -> tipo_dato VARIABLE SEMICOLON','asignar_variable',3,'p_asignar_variable','analizador_sintactico.py',21),
  ('cambiar_variable -> VARIABLE INCREMENT_VAR SEMICOLON','cambiar_variable',3,'p_cambiar_variable','analizador_sintactico.py',25),
  ('cambiar_variable -> VARIABLE DECREMENT_VAR SEMICOLON','cambiar_variable',3,'p_cambiar_variable','analizador_sintactico.py',26),
  ('cambiar_variable -> VARIABLE asignador expresion SEMICOLON','cambiar_variable',4,'p_cambiar_variable','analizador_sintactico.py',27),
  ('asignador -> ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',30),
  ('asignador -> PLUS_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',31),
  ('asignador -> MINUS_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',32),
  ('asignador -> TIMES_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',33),
  ('asignador -> DIVIDE_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',34),
  ('asignador -> MODULO_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',35),
  ('expresion -> operacion','expresion',1,'p_expresion','analizador_sintactico.py',38),
  ('expresion -> comparacion','expresion',1,'p_expresion','analizador_sintactico.py',39),
  ('expresion -> list','expresion',1,'p_expresion','analizador_sintactico.py',40),
  ('expresion -> diccionario','expresion',1,'p_expresion','analizador_sintactico.py',41),
  ('expresion -> input','expresion',1,'p_expresion','analizador_sintactico.py',42),
  ('retorno -> RETURN SEMICOLON','retorno',2,'p_retorno','analizador_sintactico.py',45),
  ('retorno -> RETURN operacion SEMICOLON','retorno',3,'p_retorno','analizador_sintactico.py',46),
  ('impresion -> PRINT LPAREN operacion RPAREN SEMICOLON','impresion',5,'p_impresion','analizador_sintactico.py',49),
  ('impresion -> PRINT LPAREN comparacion_logica RPAREN SEMICOLON','impresion',5,'p_impresion','analizador_sintactico.py',50),
  ('impresion -> PRINT LPAREN RPAREN SEMICOLON','impresion',4,'p_impresion','analizador_sintactico.py',51),
  ('input -> STDIN DOT READLINESYNC LPAREN RPAREN','input',5,'p_input','analizador_sintactico.py',55),
  ('elemento -> INT','elemento',1,'p_elemento','analizador_sintactico.py',59),
  ('elemento -> VARIABLE','elemento',1,'p_elemento','analizador_sintactico.py',60),
  ('elemento -> DOUBLE','elemento',1,'p_elemento','analizador_sintactico.py',61),
  ('elemento -> STRING','elemento',1,'p_elemento','analizador_sintactico.py',62),
  ('elemento -> BOOLEAN','elemento',1,'p_elemento','analizador_sintactico.py',63),
  ('comparacion -> operacion comparador operacion','comparacion',3,'p_comparacion','analizador_sintactico.py',66),
  ('comparacion_logica -> comparacion','comparacion_logica',1,'p_comparacion_logica','analizador_sintactico.py',69),
  ('comparacion_logica -> comparacion operador_logico comparacion_logica','comparacion_logica',3,'p_comparacion_logica','analizador_sintactico.py',70),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','analizador_sintactico.py',73),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','analizador_sintactico.py',74),
  ('operador_logico -> NOT','operador_logico',1,'p_operador_logico','analizador_sintactico.py',75),
  ('comparador -> EQUALITY','comparador',1,'p_comparador','analizador_sintactico.py',78),
  ('comparador -> INEQUALITY','comparador',1,'p_comparador','analizador_sintactico.py',79),
  ('comparador -> GREATER_THAN','comparador',1,'p_comparador','analizador_sintactico.py',80),
  ('comparador -> LESS_THAN','comparador',1,'p_comparador','analizador_sintactico.py',81),
  ('comparador -> GREATER_EQ_THAN','comparador',1,'p_comparador','analizador_sintactico.py',82),
  ('comparador -> LESS_EQ_THAN','comparador',1,'p_comparador','analizador_sintactico.py',83),
  ('operacion -> elemento','operacion',1,'p_operacion','analizador_sintactico.py',86),
  ('operacion -> elemento operador operacion','operacion',3,'p_operacion','analizador_sintactico.py',87),
  ('operador -> PLUS','operador',1,'p_operador','analizador_sintactico.py',90),
  ('operador -> MINUS','operador',1,'p_operador','analizador_sintactico.py',91),
  ('operador -> TIMES','operador',1,'p_operador','analizador_sintactico.py',92),
  ('operador -> DIVIDE','operador',1,'p_operador','analizador_sintactico.py',93),
  ('operador -> MODULO','operador',1,'p_operador','analizador_sintactico.py',94),
  ('list -> LBRACKETS element_list RBRACKETS','list',3,'p_list','analizador_sintactico.py',97),
  ('list -> LBRACKETS RBRACKETS','list',2,'p_list','analizador_sintactico.py',98),
  ('element_list -> elemento','element_list',1,'p_element_list','analizador_sintactico.py',102),
  ('element_list -> elemento COMA element_list','element_list',3,'p_element_list','analizador_sintactico.py',103),
  ('tipo_dato -> VAR_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',106),
  ('tipo_dato -> INT_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',107),
  ('tipo_dato -> STRING_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',108),
  ('tipo_dato -> DOUBLE_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',109),
  ('tipo_dato -> BOOL_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',110),
  ('tipo_dato -> LIST LESS_THAN tipo_coleccion GREATER_THAN','tipo_dato',4,'p_tipo_dato','analizador_sintactico.py',111),
  ('tipo_dato -> MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THAN','tipo_dato',6,'p_tipo_dato','analizador_sintactico.py',112),
  ('tipo_coleccion -> INT_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',115),
  ('tipo_coleccion -> STRING_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',116),
  ('tipo_coleccion -> DOUBLE_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',117),
  ('tipo_coleccion -> BOOL_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',118),
  ('while -> WHILE LPAREN comparacion_logica RPAREN LKEY programa RKEY','while',7,'p_while','analizador_sintactico.py',121),
  ('while -> DO LKEY programa RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLON','while',9,'p_while','analizador_sintactico.py',122),
  ('diccionario -> LKEY key_element_list RKEY','diccionario',3,'p_diccionario','analizador_sintactico.py',126),
  ('key_element -> elemento DOS_PUNTOS elemento','key_element',3,'p_key_element','analizador_sintactico.py',129),
  ('key_element_list -> key_element','key_element_list',1,'p_key_element_list','analizador_sintactico.py',132),
  ('key_element_list -> key_element COMA key_element_list','key_element_list',3,'p_key_element_list','analizador_sintactico.py',133),
  ('condicional -> IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else','condicional',8,'p_condicional','analizador_sintactico.py',136),
  ('condicional -> IF LPAREN comparacion_logica RPAREN LKEY programa RKEY','condicional',7,'p_condicional','analizador_sintactico.py',137),
  ('bloques_else -> ELSE IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else','bloques_else',9,'p_bloques_else','analizador_sintactico.py',141),
  ('bloques_else -> ELSE LKEY programa RKEY','bloques_else',4,'p_bloques_else','analizador_sintactico.py',142),
  ('funcion -> VOID VARIABLE LPAREN parametros RPAREN LKEY programa RKEY','funcion',8,'p_funcion','analizador_sintactico.py',145),
  ('funcion -> VOID VARIABLE LPAREN RPAREN LKEY programa RKEY','funcion',7,'p_funcion','analizador_sintactico.py',146),
  ('parametros -> tipo_dato VARIABLE','parametros',2,'p_parametros','analizador_sintactico.py',150),
  ('parametros -> tipo_dato VARIABLE COMA parametros','parametros',4,'p_parametros','analizador_sintactico.py',151),
]
