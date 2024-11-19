
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND ASSIGN BOOLEAN BOOL_TYPE COMA COMMENT DECREMENT_VAR DIVIDE DIVIDE_ASSIGN DO DOC_COMMENT DOS_PUNTOS DOT DOUBLE DOUBLE_TYPE ELSE EQUALITY FOR GREATER_EQ_THAN GREATER_THAN IF IMPORT INCREMENT_VAR INEQUALITY INT INT_TYPE LBRACKETS LESS_EQ_THAN LESS_THAN LIST LKEY LPAREN MAP MINUS MINUS_ASSIGN MODULO MODULO_ASSIGN NOT OR PLUS PLUS_ASSIGN PRINT RBRACKETS READLINESYNC RETURN RKEY RPAREN SEMICOLON SET STDIN STRING STRING_TYPE TIMES TIMES_ASSIGN VARIABLE VAR_TYPE VOID WHILEprograma : sentencias\n                | sentencias programasentencias : asignar_variable\n                  | cambiar_variable\n                  | impresion\n                  | condicional\n                  | funcion\n                  | retorno\n                  | while\n                  | do_while\n                  | for\n                  | importfuncion : tipo_dato VARIABLE LPAREN parametros RPAREN LKEY programa RKEY\n                | tipo_dato VARIABLE LPAREN RPAREN LKEY programa RKEYasignar_variable : tipo_dato VARIABLE asignador expresion SEMICOLON\n                    | tipo_dato VARIABLE SEMICOLONcambiar_variable : VARIABLE modificador SEMICOLON\n                        | VARIABLE asignador expresion SEMICOLONmodificador : INCREMENT_VAR\n                    | DECREMENT_VARasignador : ASSIGN\n                | PLUS_ASSIGN\n                | MINUS_ASSIGN\n                | TIMES_ASSIGN\n                | DIVIDE_ASSIGN\n                | MODULO_ASSIGNexpresion : operacion\n                    | comparacion\n                    | list\n                    | diccionario\n                    | set\n                    | inputretorno : RETURN SEMICOLON\n                | RETURN operacion SEMICOLONimport : IMPORT STRING SEMICOLONimpresion : PRINT LPAREN operacion RPAREN SEMICOLON\n                 | PRINT LPAREN comparacion_logica RPAREN SEMICOLON\n                 | PRINT LPAREN RPAREN SEMICOLONinput : STDIN DOT READLINESYNC LPAREN RPARENelemento : INT\n            | VARIABLE\n            | DOUBLE\n            | STRING\n            | BOOLEANcomparacion : operacion comparador operacioncomparacion_logica : comparacion\n                          | comparacion operador_logico comparacion_logicaoperador_logico : AND\n                        | OR\n                        | NOTcomparador : EQUALITY\n                    | INEQUALITY\n                    | GREATER_THAN\n                    | LESS_THAN\n                    | GREATER_EQ_THAN\n                    | LESS_EQ_THANoperacion : elemento\n                | elemento operador operacionoperador : PLUS\n                | MINUS\n                | TIMES\n                | DIVIDE\n                | MODULOlist : LBRACKETS element_list RBRACKETS\n            | LBRACKETS RBRACKETSelement_list : elemento\n                    | elemento COMA element_listtipo_dato : VOID \n             | VAR_TYPE\n             | INT_TYPE\n             | STRING_TYPE\n             | DOUBLE_TYPE\n             | BOOL_TYPE\n             | LIST LESS_THAN tipo_coleccion GREATER_THAN\n             | MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THAN\n             | SET LESS_THAN tipo_coleccion GREATER_THANtipo_coleccion : INT_TYPE\n             | STRING_TYPE\n             | DOUBLE_TYPE\n             | BOOL_TYPEinstruccion_for : asignar_variable comparacion_logica SEMICOLON VARIABLE asignador expresion\n                        | asignar_variable comparacion_logica SEMICOLON VARIABLE modificadorfor : FOR LPAREN instruccion_for RPAREN LKEY programa RKEYwhile : WHILE LPAREN comparacion_logica RPAREN LKEY programa RKEYdo_while : DO LKEY programa RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLONdiccionario : LKEY key_element_list RKEY\n                    | LKEY RKEYset : LKEY element_list RKEY\n            | LESS_THAN tipo_coleccion GREATER_THAN LKEY RKEYkey_element : elemento DOS_PUNTOS elementokey_element_list : key_element\n                        | key_element COMA key_element_listcondicional : IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else\n                    | IF LPAREN comparacion_logica RPAREN LKEY programa RKEYbloques_else : ELSE IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else\n                    | ELSE LKEY programa RKEYparametros : tipo_dato VARIABLE\n                  | tipo_dato VARIABLE COMA parametros'
    
_lr_action_items = {'VARIABLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,17,22,23,24,25,26,27,34,37,38,39,40,41,42,43,44,45,53,54,60,61,63,71,72,81,82,83,84,85,86,87,91,92,93,102,105,106,107,108,109,110,111,112,124,126,127,128,129,137,139,140,143,146,149,150,153,154,156,157,159,160,163,173,176,179,182,183,185,186,188,189,194,195,196,199,201,204,],[14,14,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,32,49,-68,-69,-70,-71,-72,-73,49,-21,-22,-23,-24,-25,-26,49,49,-33,49,14,49,-16,-17,49,49,-34,49,-59,-60,-61,-62,-63,49,136,-35,141,-18,49,-51,-52,-53,-54,-55,-56,-38,49,-48,-49,-50,-74,-76,-15,14,49,49,49,-36,-37,14,14,14,175,14,49,-75,-14,-94,-84,-83,49,-13,-93,14,-85,49,-96,14,-95,]),'PRINT':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[15,15,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,15,-16,-17,-34,-35,-18,-38,-15,15,-36,-37,15,15,15,15,-14,-94,-84,-83,-13,-93,15,-85,-96,15,-95,]),'IF':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,190,194,195,199,201,204,],[16,16,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,16,-16,-17,-34,-35,-18,-38,-15,16,-36,-37,16,16,16,16,-14,-94,-84,-83,-13,-93,193,16,-85,-96,16,-95,]),'RETURN':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[17,17,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,17,-16,-17,-34,-35,-18,-38,-15,17,-36,-37,17,17,17,17,-14,-94,-84,-83,-13,-93,17,-85,-96,17,-95,]),'WHILE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,133,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[18,18,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,18,-16,-17,-34,-35,-18,-38,158,-15,18,-36,-37,18,18,18,18,-14,-94,-84,-83,-13,-93,18,-85,-96,18,-95,]),'DO':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[19,19,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,19,-16,-17,-34,-35,-18,-38,-15,19,-36,-37,19,19,19,19,-14,-94,-84,-83,-13,-93,19,-85,-96,19,-95,]),'FOR':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[20,20,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,20,-16,-17,-34,-35,-18,-38,-15,20,-36,-37,20,20,20,20,-14,-94,-84,-83,-13,-93,20,-85,-96,20,-95,]),'IMPORT':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,61,63,81,93,105,124,140,143,153,154,156,157,159,163,179,182,183,185,188,189,194,195,199,201,204,],[21,21,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,21,-16,-17,-34,-35,-18,-38,-15,21,-36,-37,21,21,21,21,-14,-94,-84,-83,-13,-93,21,-85,-96,21,-95,]),'VOID':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,61,62,63,81,93,105,124,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[22,22,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,22,22,-16,22,-17,-34,-35,-18,-38,-15,22,-36,-37,22,22,22,22,22,-14,-94,-84,-83,-13,-93,22,-85,-96,22,-95,]),'VAR_TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,61,62,63,81,93,105,124,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[23,23,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,23,23,-16,23,-17,-34,-35,-18,-38,-15,23,-36,-37,23,23,23,23,23,-14,-94,-84,-83,-13,-93,23,-85,-96,23,-95,]),'INT_TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,57,58,59,61,62,63,73,81,93,105,124,138,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[24,24,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,24,24,95,95,95,-16,24,-17,95,-34,-35,-18,-38,95,-15,24,-36,-37,24,24,24,24,24,-14,-94,-84,-83,-13,-93,24,-85,-96,24,-95,]),'STRING_TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,57,58,59,61,62,63,73,81,93,105,124,138,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[25,25,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,25,25,96,96,96,-16,25,-17,96,-34,-35,-18,-38,96,-15,25,-36,-37,25,25,25,25,25,-14,-94,-84,-83,-13,-93,25,-85,-96,25,-95,]),'DOUBLE_TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,57,58,59,61,62,63,73,81,93,105,124,138,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[26,26,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,26,26,97,97,97,-16,26,-17,97,-34,-35,-18,-38,97,-15,26,-36,-37,26,26,26,26,26,-14,-94,-84,-83,-13,-93,26,-85,-96,26,-95,]),'BOOL_TYPE':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,57,58,59,61,62,63,73,81,93,105,124,138,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[27,27,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,27,27,98,98,98,-16,27,-17,98,-34,-35,-18,-38,98,-15,27,-36,-37,27,27,27,27,27,-14,-94,-84,-83,-13,-93,27,-85,-96,27,-95,]),'LIST':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,61,62,63,81,93,105,124,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[28,28,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,28,28,-16,28,-17,-34,-35,-18,-38,-15,28,-36,-37,28,28,28,28,28,-14,-94,-84,-83,-13,-93,28,-85,-96,28,-95,]),'MAP':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,61,62,63,81,93,105,124,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[29,29,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,29,29,-16,29,-17,-34,-35,-18,-38,-15,29,-36,-37,29,29,29,29,29,-14,-94,-84,-83,-13,-93,29,-85,-96,29,-95,]),'SET':([0,2,3,4,5,6,7,8,9,10,11,12,45,54,55,61,62,63,81,93,105,124,140,143,153,154,156,157,159,162,163,179,182,183,185,188,189,194,195,199,201,204,],[30,30,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-33,30,30,-16,30,-17,-34,-35,-18,-38,-15,30,-36,-37,30,30,30,30,30,-14,-94,-84,-83,-13,-93,30,-85,-96,30,-95,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,31,45,61,63,81,93,105,124,140,153,154,179,182,183,185,188,189,195,199,204,],[0,-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-33,-16,-17,-34,-35,-18,-38,-15,-36,-37,-14,-94,-84,-83,-13,-93,-85,-96,-95,]),'RKEY':([2,3,4,5,6,7,8,9,10,11,12,31,45,48,49,50,51,52,61,63,72,81,89,93,105,115,116,118,119,120,124,140,153,154,164,165,166,168,169,171,172,174,178,179,182,183,185,188,189,195,197,199,202,204,],[-1,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-2,-33,-40,-41,-42,-43,-44,-16,-17,117,-34,133,-35,-18,-66,147,148,-91,-66,-38,-15,-36,-37,179,-67,-92,-90,180,182,183,185,188,-14,-94,-84,-83,-13,-93,-85,199,-96,203,-95,]),'INCREMENT_VAR':([14,175,],[35,35,]),'DECREMENT_VAR':([14,175,],[36,36,]),'ASSIGN':([14,32,136,175,],[37,37,37,37,]),'PLUS_ASSIGN':([14,32,136,175,],[38,38,38,38,]),'MINUS_ASSIGN':([14,32,136,175,],[39,39,39,39,]),'TIMES_ASSIGN':([14,32,136,175,],[40,40,40,40,]),'DIVIDE_ASSIGN':([14,32,136,175,],[41,41,41,41,]),'MODULO_ASSIGN':([14,32,136,175,],[42,42,42,42,]),'LPAREN':([15,16,18,20,32,152,158,193,],[43,44,53,55,62,170,173,196,]),'SEMICOLON':([17,32,33,35,36,46,47,48,49,50,51,52,56,64,65,66,67,68,69,70,76,78,101,114,117,123,125,131,135,136,144,145,147,148,155,180,181,191,],[45,61,63,-19,-20,81,-57,-40,-41,-42,-43,-44,93,105,-27,-28,-29,-30,-31,-32,124,-46,140,-65,-87,153,154,-58,160,61,-45,-64,-86,-88,-47,-89,-39,195,]),'INT':([17,34,37,38,39,40,41,42,43,44,53,60,61,71,72,82,83,84,85,86,87,91,106,107,108,109,110,111,112,126,127,128,129,140,146,149,150,173,186,196,],[48,48,-21,-22,-23,-24,-25,-26,48,48,48,48,-16,48,48,48,-59,-60,-61,-62,-63,48,48,-51,-52,-53,-54,-55,-56,48,-48,-49,-50,-15,48,48,48,48,48,48,]),'DOUBLE':([17,34,37,38,39,40,41,42,43,44,53,60,61,71,72,82,83,84,85,86,87,91,106,107,108,109,110,111,112,126,127,128,129,140,146,149,150,173,186,196,],[50,50,-21,-22,-23,-24,-25,-26,50,50,50,50,-16,50,50,50,-59,-60,-61,-62,-63,50,50,-51,-52,-53,-54,-55,-56,50,-48,-49,-50,-15,50,50,50,50,50,50,]),'STRING':([17,21,34,37,38,39,40,41,42,43,44,53,60,61,71,72,82,83,84,85,86,87,91,106,107,108,109,110,111,112,126,127,128,129,140,146,149,150,173,186,196,],[51,56,51,-21,-22,-23,-24,-25,-26,51,51,51,51,-16,51,51,51,-59,-60,-61,-62,-63,51,51,-51,-52,-53,-54,-55,-56,51,-48,-49,-50,-15,51,51,51,51,51,51,]),'BOOLEAN':([17,34,37,38,39,40,41,42,43,44,53,60,61,71,72,82,83,84,85,86,87,91,106,107,108,109,110,111,112,126,127,128,129,140,146,149,150,173,186,196,],[52,52,-21,-22,-23,-24,-25,-26,52,52,52,52,-16,52,52,52,-59,-60,-61,-62,-63,52,52,-51,-52,-53,-54,-55,-56,52,-48,-49,-50,-15,52,52,52,52,52,52,]),'LKEY':([19,34,37,38,39,40,41,42,60,104,130,132,134,142,151,186,190,200,],[54,72,-21,-22,-23,-24,-25,-26,72,143,156,157,159,163,169,72,194,201,]),'LESS_THAN':([28,29,30,34,37,38,39,40,41,42,47,48,49,50,51,52,60,65,75,80,131,186,],[57,58,59,73,-21,-22,-23,-24,-25,-26,-57,-40,-41,-42,-43,-44,73,110,110,110,-58,73,]),'LBRACKETS':([34,37,38,39,40,41,42,60,186,],[71,-21,-22,-23,-24,-25,-26,71,71,]),'STDIN':([34,37,38,39,40,41,42,60,186,],[74,-21,-22,-23,-24,-25,-26,74,74,]),'RPAREN':([35,36,43,47,48,49,50,51,52,62,65,66,67,68,69,70,75,77,78,79,88,90,103,114,117,131,141,144,145,147,148,155,170,177,180,181,184,187,192,198,],[-19,-20,76,-57,-40,-41,-42,-43,-44,104,-27,-28,-29,-30,-31,-32,123,125,-46,130,132,134,142,-65,-87,-58,-97,-45,-64,-86,-88,-47,181,-98,-89,-39,191,-82,-81,200,]),'EQUALITY':([47,48,49,50,51,52,65,75,80,131,],[-57,-40,-41,-42,-43,-44,107,107,107,-58,]),'INEQUALITY':([47,48,49,50,51,52,65,75,80,131,],[-57,-40,-41,-42,-43,-44,108,108,108,-58,]),'GREATER_THAN':([47,48,49,50,51,52,65,75,80,94,95,96,97,98,100,121,131,161,],[-57,-40,-41,-42,-43,-44,109,109,109,137,-77,-78,-79,-80,139,151,-58,176,]),'GREATER_EQ_THAN':([47,48,49,50,51,52,65,75,80,131,],[-57,-40,-41,-42,-43,-44,111,111,111,-58,]),'LESS_EQ_THAN':([47,48,49,50,51,52,65,75,80,131,],[-57,-40,-41,-42,-43,-44,112,112,112,-58,]),'AND':([47,48,49,50,51,52,78,131,144,],[-57,-40,-41,-42,-43,-44,127,-58,-45,]),'OR':([47,48,49,50,51,52,78,131,144,],[-57,-40,-41,-42,-43,-44,128,-58,-45,]),'NOT':([47,48,49,50,51,52,78,131,144,],[-57,-40,-41,-42,-43,-44,129,-58,-45,]),'PLUS':([47,48,49,50,51,52,],[83,-40,-41,-42,-43,-44,]),'MINUS':([47,48,49,50,51,52,],[84,-40,-41,-42,-43,-44,]),'TIMES':([47,48,49,50,51,52,],[85,-40,-41,-42,-43,-44,]),'DIVIDE':([47,48,49,50,51,52,],[86,-40,-41,-42,-43,-44,]),'MODULO':([47,48,49,50,51,52,],[87,-40,-41,-42,-43,-44,]),'COMA':([48,49,50,51,52,95,96,97,98,99,115,119,120,141,168,],[-40,-41,-42,-43,-44,-77,-78,-79,-80,138,146,149,146,162,-90,]),'RBRACKETS':([48,49,50,51,52,71,113,115,165,],[-40,-41,-42,-43,-44,114,145,-66,-67,]),'DOS_PUNTOS':([48,49,50,51,52,120,167,],[-40,-41,-42,-43,-44,150,150,]),'DOT':([74,],[122,]),'READLINESYNC':([122,],[152,]),'ELSE':([182,203,],[190,190,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,2,54,143,156,157,159,163,194,201,],[1,31,89,164,171,172,174,178,197,202,]),'sentencias':([0,2,54,143,156,157,159,163,194,201,],[2,2,2,2,2,2,2,2,2,2,]),'asignar_variable':([0,2,54,55,143,156,157,159,163,194,201,],[3,3,3,91,3,3,3,3,3,3,3,]),'cambiar_variable':([0,2,54,143,156,157,159,163,194,201,],[4,4,4,4,4,4,4,4,4,4,]),'impresion':([0,2,54,143,156,157,159,163,194,201,],[5,5,5,5,5,5,5,5,5,5,]),'condicional':([0,2,54,143,156,157,159,163,194,201,],[6,6,6,6,6,6,6,6,6,6,]),'funcion':([0,2,54,143,156,157,159,163,194,201,],[7,7,7,7,7,7,7,7,7,7,]),'retorno':([0,2,54,143,156,157,159,163,194,201,],[8,8,8,8,8,8,8,8,8,8,]),'while':([0,2,54,143,156,157,159,163,194,201,],[9,9,9,9,9,9,9,9,9,9,]),'do_while':([0,2,54,143,156,157,159,163,194,201,],[10,10,10,10,10,10,10,10,10,10,]),'for':([0,2,54,143,156,157,159,163,194,201,],[11,11,11,11,11,11,11,11,11,11,]),'import':([0,2,54,143,156,157,159,163,194,201,],[12,12,12,12,12,12,12,12,12,12,]),'tipo_dato':([0,2,54,55,62,143,156,157,159,162,163,194,201,],[13,13,13,92,102,13,13,13,13,102,13,13,13,]),'modificador':([14,175,],[33,187,]),'asignador':([14,32,136,175,],[34,60,60,186,]),'operacion':([17,34,43,44,53,60,82,91,106,126,173,186,196,],[46,65,75,80,80,65,131,80,144,80,80,65,80,]),'elemento':([17,34,43,44,53,60,71,72,82,91,106,126,146,149,150,173,186,196,],[47,47,47,47,47,47,115,120,47,47,47,47,115,167,168,47,47,47,]),'expresion':([34,60,186,],[64,101,192,]),'comparacion':([34,43,44,53,60,91,126,173,186,196,],[66,78,78,78,66,78,78,78,66,78,]),'list':([34,60,186,],[67,67,67,]),'diccionario':([34,60,186,],[68,68,68,]),'set':([34,60,186,],[69,69,69,]),'input':([34,60,186,],[70,70,70,]),'comparacion_logica':([43,44,53,91,126,173,196,],[77,79,88,135,155,184,198,]),'operador':([47,],[82,]),'instruccion_for':([55,],[90,]),'tipo_coleccion':([57,58,59,73,138,],[94,99,100,121,161,]),'parametros':([62,162,],[103,177,]),'comparador':([65,75,80,],[106,106,106,]),'element_list':([71,72,146,],[113,118,165,]),'key_element_list':([72,149,],[116,166,]),'key_element':([72,149,],[119,119,]),'operador_logico':([78,],[126,]),'bloques_else':([182,203,],[189,204,]),}

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
  ('sentencias -> do_while','sentencias',1,'p_sentencias','analizador_sintactico.py',17),
  ('sentencias -> for','sentencias',1,'p_sentencias','analizador_sintactico.py',18),
  ('sentencias -> import','sentencias',1,'p_sentencias','analizador_sintactico.py',19),
  ('funcion -> tipo_dato VARIABLE LPAREN parametros RPAREN LKEY programa RKEY','funcion',8,'p_funcion','analizador_sintactico.py',23),
  ('funcion -> tipo_dato VARIABLE LPAREN RPAREN LKEY programa RKEY','funcion',7,'p_funcion','analizador_sintactico.py',24),
  ('asignar_variable -> tipo_dato VARIABLE asignador expresion SEMICOLON','asignar_variable',5,'p_asignar_variable','analizador_sintactico.py',28),
  ('asignar_variable -> tipo_dato VARIABLE SEMICOLON','asignar_variable',3,'p_asignar_variable','analizador_sintactico.py',29),
  ('cambiar_variable -> VARIABLE modificador SEMICOLON','cambiar_variable',3,'p_cambiar_variable','analizador_sintactico.py',33),
  ('cambiar_variable -> VARIABLE asignador expresion SEMICOLON','cambiar_variable',4,'p_cambiar_variable','analizador_sintactico.py',34),
  ('modificador -> INCREMENT_VAR','modificador',1,'p_modificador','analizador_sintactico.py',38),
  ('modificador -> DECREMENT_VAR','modificador',1,'p_modificador','analizador_sintactico.py',39),
  ('asignador -> ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',42),
  ('asignador -> PLUS_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',43),
  ('asignador -> MINUS_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',44),
  ('asignador -> TIMES_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',45),
  ('asignador -> DIVIDE_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',46),
  ('asignador -> MODULO_ASSIGN','asignador',1,'p_asignador','analizador_sintactico.py',47),
  ('expresion -> operacion','expresion',1,'p_expresion','analizador_sintactico.py',50),
  ('expresion -> comparacion','expresion',1,'p_expresion','analizador_sintactico.py',51),
  ('expresion -> list','expresion',1,'p_expresion','analizador_sintactico.py',52),
  ('expresion -> diccionario','expresion',1,'p_expresion','analizador_sintactico.py',53),
  ('expresion -> set','expresion',1,'p_expresion','analizador_sintactico.py',54),
  ('expresion -> input','expresion',1,'p_expresion','analizador_sintactico.py',55),
  ('retorno -> RETURN SEMICOLON','retorno',2,'p_retorno','analizador_sintactico.py',58),
  ('retorno -> RETURN operacion SEMICOLON','retorno',3,'p_retorno','analizador_sintactico.py',59),
  ('import -> IMPORT STRING SEMICOLON','import',3,'p_import','analizador_sintactico.py',63),
  ('impresion -> PRINT LPAREN operacion RPAREN SEMICOLON','impresion',5,'p_impresion','analizador_sintactico.py',67),
  ('impresion -> PRINT LPAREN comparacion_logica RPAREN SEMICOLON','impresion',5,'p_impresion','analizador_sintactico.py',68),
  ('impresion -> PRINT LPAREN RPAREN SEMICOLON','impresion',4,'p_impresion','analizador_sintactico.py',69),
  ('input -> STDIN DOT READLINESYNC LPAREN RPAREN','input',5,'p_input','analizador_sintactico.py',73),
  ('elemento -> INT','elemento',1,'p_elemento','analizador_sintactico.py',77),
  ('elemento -> VARIABLE','elemento',1,'p_elemento','analizador_sintactico.py',78),
  ('elemento -> DOUBLE','elemento',1,'p_elemento','analizador_sintactico.py',79),
  ('elemento -> STRING','elemento',1,'p_elemento','analizador_sintactico.py',80),
  ('elemento -> BOOLEAN','elemento',1,'p_elemento','analizador_sintactico.py',81),
  ('comparacion -> operacion comparador operacion','comparacion',3,'p_comparacion','analizador_sintactico.py',84),
  ('comparacion_logica -> comparacion','comparacion_logica',1,'p_comparacion_logica','analizador_sintactico.py',87),
  ('comparacion_logica -> comparacion operador_logico comparacion_logica','comparacion_logica',3,'p_comparacion_logica','analizador_sintactico.py',88),
  ('operador_logico -> AND','operador_logico',1,'p_operador_logico','analizador_sintactico.py',91),
  ('operador_logico -> OR','operador_logico',1,'p_operador_logico','analizador_sintactico.py',92),
  ('operador_logico -> NOT','operador_logico',1,'p_operador_logico','analizador_sintactico.py',93),
  ('comparador -> EQUALITY','comparador',1,'p_comparador','analizador_sintactico.py',96),
  ('comparador -> INEQUALITY','comparador',1,'p_comparador','analizador_sintactico.py',97),
  ('comparador -> GREATER_THAN','comparador',1,'p_comparador','analizador_sintactico.py',98),
  ('comparador -> LESS_THAN','comparador',1,'p_comparador','analizador_sintactico.py',99),
  ('comparador -> GREATER_EQ_THAN','comparador',1,'p_comparador','analizador_sintactico.py',100),
  ('comparador -> LESS_EQ_THAN','comparador',1,'p_comparador','analizador_sintactico.py',101),
  ('operacion -> elemento','operacion',1,'p_operacion','analizador_sintactico.py',104),
  ('operacion -> elemento operador operacion','operacion',3,'p_operacion','analizador_sintactico.py',105),
  ('operador -> PLUS','operador',1,'p_operador','analizador_sintactico.py',108),
  ('operador -> MINUS','operador',1,'p_operador','analizador_sintactico.py',109),
  ('operador -> TIMES','operador',1,'p_operador','analizador_sintactico.py',110),
  ('operador -> DIVIDE','operador',1,'p_operador','analizador_sintactico.py',111),
  ('operador -> MODULO','operador',1,'p_operador','analizador_sintactico.py',112),
  ('list -> LBRACKETS element_list RBRACKETS','list',3,'p_list','analizador_sintactico.py',115),
  ('list -> LBRACKETS RBRACKETS','list',2,'p_list','analizador_sintactico.py',116),
  ('element_list -> elemento','element_list',1,'p_element_list','analizador_sintactico.py',120),
  ('element_list -> elemento COMA element_list','element_list',3,'p_element_list','analizador_sintactico.py',121),
  ('tipo_dato -> VOID','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',124),
  ('tipo_dato -> VAR_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',125),
  ('tipo_dato -> INT_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',126),
  ('tipo_dato -> STRING_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',127),
  ('tipo_dato -> DOUBLE_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',128),
  ('tipo_dato -> BOOL_TYPE','tipo_dato',1,'p_tipo_dato','analizador_sintactico.py',129),
  ('tipo_dato -> LIST LESS_THAN tipo_coleccion GREATER_THAN','tipo_dato',4,'p_tipo_dato','analizador_sintactico.py',130),
  ('tipo_dato -> MAP LESS_THAN tipo_coleccion COMA tipo_coleccion GREATER_THAN','tipo_dato',6,'p_tipo_dato','analizador_sintactico.py',131),
  ('tipo_dato -> SET LESS_THAN tipo_coleccion GREATER_THAN','tipo_dato',4,'p_tipo_dato','analizador_sintactico.py',132),
  ('tipo_coleccion -> INT_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',135),
  ('tipo_coleccion -> STRING_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',136),
  ('tipo_coleccion -> DOUBLE_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',137),
  ('tipo_coleccion -> BOOL_TYPE','tipo_coleccion',1,'p_tipo_coleccion','analizador_sintactico.py',138),
  ('instruccion_for -> asignar_variable comparacion_logica SEMICOLON VARIABLE asignador expresion','instruccion_for',6,'p_instruccion_for','analizador_sintactico.py',141),
  ('instruccion_for -> asignar_variable comparacion_logica SEMICOLON VARIABLE modificador','instruccion_for',5,'p_instruccion_for','analizador_sintactico.py',142),
  ('for -> FOR LPAREN instruccion_for RPAREN LKEY programa RKEY','for',7,'p_for','analizador_sintactico.py',145),
  ('while -> WHILE LPAREN comparacion_logica RPAREN LKEY programa RKEY','while',7,'p_while','analizador_sintactico.py',149),
  ('do_while -> DO LKEY programa RKEY WHILE LPAREN comparacion_logica RPAREN SEMICOLON','do_while',9,'p_do_while','analizador_sintactico.py',153),
  ('diccionario -> LKEY key_element_list RKEY','diccionario',3,'p_diccionario','analizador_sintactico.py',157),
  ('diccionario -> LKEY RKEY','diccionario',2,'p_diccionario','analizador_sintactico.py',158),
  ('set -> LKEY element_list RKEY','set',3,'p_set','analizador_sintactico.py',162),
  ('set -> LESS_THAN tipo_coleccion GREATER_THAN LKEY RKEY','set',5,'p_set','analizador_sintactico.py',163),
  ('key_element -> elemento DOS_PUNTOS elemento','key_element',3,'p_key_element','analizador_sintactico.py',167),
  ('key_element_list -> key_element','key_element_list',1,'p_key_element_list','analizador_sintactico.py',170),
  ('key_element_list -> key_element COMA key_element_list','key_element_list',3,'p_key_element_list','analizador_sintactico.py',171),
  ('condicional -> IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else','condicional',8,'p_condicional','analizador_sintactico.py',174),
  ('condicional -> IF LPAREN comparacion_logica RPAREN LKEY programa RKEY','condicional',7,'p_condicional','analizador_sintactico.py',175),
  ('bloques_else -> ELSE IF LPAREN comparacion_logica RPAREN LKEY programa RKEY bloques_else','bloques_else',9,'p_bloques_else','analizador_sintactico.py',179),
  ('bloques_else -> ELSE LKEY programa RKEY','bloques_else',4,'p_bloques_else','analizador_sintactico.py',180),
  ('parametros -> tipo_dato VARIABLE','parametros',2,'p_parametros','analizador_sintactico.py',183),
  ('parametros -> tipo_dato VARIABLE COMA parametros','parametros',4,'p_parametros','analizador_sintactico.py',184),
]
