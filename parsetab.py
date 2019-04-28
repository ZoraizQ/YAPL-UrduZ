
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'uzleftDECINCleftORleftANDleftEENEnonassocLTGTGTELTEleftPLUSMINUSleftMULTIPLYDIVIDErightNOTAND CALL COMMA COMMENT DEC DIVIDE DO EACH EE ELIF ELSE EQUAL FALSE FLOAT FOR FUNCTION GT GTE IF IN INC INT LBRACE LBRACK LPAREN LT LTE MAKE MINUS MODULUS MULTIPLY NAME NE NOT OR PLUS POWER PRINT RBRACE RBRACK RETURN RPAREN SEMICOL SEP STRING THEN TO TRUE UNTIL WHILE\n    uz : line uz\n    \n    line : stmt SEMICOL\n    uz : error SEMICOL\n    \n    uz :\n     stmtblock : LBRACE stmtS RBRACE\n    stmtS : stmt SEMICOL stmtS\n    \n    stmtS :\n    exp : NAME LPAREN optargs RPARENoptargs : argsoptargs :args : exp COMMA args\n            | exp \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp MULTIPLY exp\n        | exp DIVIDE exp\n        | exp POWER exp\n        | exp MODULUS exp\n    \n    exp : exp AND exp\n        | exp OR exp\n        | exp GT exp\n        | exp LT exp\n        | exp GTE exp\n        | exp LTE exp\n        | exp EE exp\n        | exp NE exp\n    exp : NAME\n    exp : MINUS INT\n        | MINUS FLOAT\n        | INT\n        | FLOAT\n    \n    exp : DEC exp\n        | INC exp\n    \n    stmt : exp DEC\n         | exp INC\n    \n    exp : NOT exp\n    \n    exp : TRUE\n        | FALSE\n    exp : STRINGexp : LPAREN exp RPAREN\n    stmt : MAKE NAME\n    \n    stmt : MAKE NAME EQUAL exp\n    stmt : NAME EQUAL exp\n    stmt : IF exp THEN stmtblock\n    \n    elif : ELIF exp THEN stmtblock elif\n    \n    elif :\n    \n    stmt : FOR NAME EQUAL exp TO INT UNTIL\n    stmt : PRINT LPAREN exp RPARENstmt : RETURN exp'
    
_lr_action_items = {'error':([0,2,24,],[3,3,-2,]),'$end':([0,1,2,22,23,24,],[-4,0,-4,-1,-3,-2,]),'MAKE':([0,2,24,82,90,],[8,8,-2,8,8,]),'NAME':([0,2,6,7,8,10,11,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[9,9,42,42,44,42,48,42,42,42,-2,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,9,9,]),'IF':([0,2,24,82,90,],[10,10,-2,10,10,]),'FOR':([0,2,24,82,90,],[11,11,-2,11,11,]),'PRINT':([0,2,24,82,90,],[13,13,-2,13,13,]),'RETURN':([0,2,24,82,90,],[15,15,-2,15,15,]),'MINUS':([0,2,5,6,7,9,10,12,14,15,17,18,19,20,21,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,73,75,76,77,78,79,80,82,83,90,],[16,16,28,16,16,-27,16,-30,16,16,-31,16,-37,-38,-39,-2,16,16,16,16,16,16,16,16,16,16,16,16,16,16,28,-27,28,16,16,28,16,28,28,-28,-29,-36,-13,-14,-15,-16,28,28,28,28,28,28,28,28,28,28,16,28,28,16,28,-40,28,-8,16,16,28,16,]),'INT':([0,2,6,7,10,14,15,16,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,88,90,],[12,12,12,12,12,12,12,52,12,-2,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,91,12,]),'FLOAT':([0,2,6,7,10,14,15,16,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[17,17,17,17,17,17,17,53,17,-2,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'DEC':([0,2,5,6,7,9,10,12,14,15,17,18,19,20,21,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,75,77,79,80,82,90,],[6,6,25,6,6,-27,6,-30,6,6,-31,6,-37,-38,-39,-2,6,6,6,6,6,6,6,6,6,6,6,6,6,6,-32,-27,-33,6,6,6,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,6,6,-40,-8,6,6,6,]),'INC':([0,2,5,6,7,9,10,12,14,15,17,18,19,20,21,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,49,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,75,77,79,80,82,90,],[7,7,26,7,7,-27,7,-30,7,7,-31,7,-37,-38,-39,-2,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-32,-27,-33,7,7,7,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,7,7,-40,-8,7,7,7,]),'NOT':([0,2,6,7,10,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[18,18,18,18,18,18,18,18,-2,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'TRUE':([0,2,6,7,10,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[19,19,19,19,19,19,19,19,-2,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'FALSE':([0,2,6,7,10,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[20,20,20,20,20,20,20,20,-2,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'STRING':([0,2,6,7,10,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[21,21,21,21,21,21,21,21,-2,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'LPAREN':([0,2,6,7,9,10,13,14,15,18,24,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,45,46,49,69,75,80,82,90,],[14,14,14,14,46,14,49,14,14,14,-2,14,14,14,14,14,14,14,14,14,14,14,14,14,14,46,14,14,14,14,14,14,14,14,]),'SEMICOL':([3,4,12,17,19,20,21,25,26,41,42,43,44,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,77,78,79,81,84,87,89,93,],[23,24,-30,-31,-37,-38,-39,-34,-35,-32,-27,-33,-41,-49,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-43,-40,-42,-8,-44,-48,90,-5,-47,]),'PLUS':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[27,-27,-30,-31,-37,-38,-39,27,-27,27,27,27,27,-28,-29,-36,-13,-14,-15,-16,27,27,27,27,27,27,27,27,27,27,27,27,27,-40,27,-8,27,]),'MULTIPLY':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[29,-27,-30,-31,-37,-38,-39,29,-27,29,29,29,29,-28,-29,-36,29,29,-15,-16,29,29,29,29,29,29,29,29,29,29,29,29,29,-40,29,-8,29,]),'DIVIDE':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[30,-27,-30,-31,-37,-38,-39,30,-27,30,30,30,30,-28,-29,-36,30,30,-15,-16,30,30,30,30,30,30,30,30,30,30,30,30,30,-40,30,-8,30,]),'POWER':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[31,-27,-30,-31,-37,-38,-39,-32,-27,-33,31,31,31,-28,-29,-36,-13,-14,-15,-16,31,31,-19,-20,-21,-22,-23,-24,-25,-26,31,31,31,-40,31,-8,31,]),'MODULUS':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[32,-27,-30,-31,-37,-38,-39,-32,-27,-33,32,32,32,-28,-29,-36,-13,-14,-15,-16,32,32,-19,-20,-21,-22,-23,-24,-25,-26,32,32,32,-40,32,-8,32,]),'AND':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[33,-27,-30,-31,-37,-38,-39,33,-27,33,33,33,33,-28,-29,-36,-13,-14,-15,-16,33,33,-19,33,-21,-22,-23,-24,-25,-26,33,33,33,-40,33,-8,33,]),'OR':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[34,-27,-30,-31,-37,-38,-39,34,-27,34,34,34,34,-28,-29,-36,-13,-14,-15,-16,34,34,-19,-20,-21,-22,-23,-24,-25,-26,34,34,34,-40,34,-8,34,]),'GT':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[35,-27,-30,-31,-37,-38,-39,35,-27,35,35,35,35,-28,-29,-36,-13,-14,-15,-16,35,35,35,35,None,None,None,None,35,35,35,35,35,-40,35,-8,35,]),'LT':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[36,-27,-30,-31,-37,-38,-39,36,-27,36,36,36,36,-28,-29,-36,-13,-14,-15,-16,36,36,36,36,None,None,None,None,36,36,36,36,36,-40,36,-8,36,]),'GTE':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[37,-27,-30,-31,-37,-38,-39,37,-27,37,37,37,37,-28,-29,-36,-13,-14,-15,-16,37,37,37,37,None,None,None,None,37,37,37,37,37,-40,37,-8,37,]),'LTE':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[38,-27,-30,-31,-37,-38,-39,38,-27,38,38,38,38,-28,-29,-36,-13,-14,-15,-16,38,38,38,38,None,None,None,None,38,38,38,38,38,-40,38,-8,38,]),'EE':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[39,-27,-30,-31,-37,-38,-39,39,-27,39,39,39,39,-28,-29,-36,-13,-14,-15,-16,39,39,39,39,-21,-22,-23,-24,-25,-26,39,39,39,-40,39,-8,39,]),'NE':([5,9,12,17,19,20,21,41,42,43,47,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,77,78,79,83,],[40,-27,-30,-31,-37,-38,-39,40,-27,40,40,40,40,-28,-29,-36,-13,-14,-15,-16,40,40,40,40,-21,-22,-23,-24,-25,-26,40,40,40,-40,40,-8,40,]),'EQUAL':([9,44,48,],[45,69,75,]),'THEN':([12,17,19,20,21,41,42,43,47,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,79,],[-30,-31,-37,-38,-39,-32,-27,-33,74,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-40,-8,]),'RPAREN':([12,17,19,20,21,41,42,43,46,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,71,72,73,76,77,79,85,],[-30,-31,-37,-38,-39,-32,-27,-33,-10,77,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,79,-9,-12,84,-40,-8,-11,]),'COMMA':([12,17,19,20,21,41,42,43,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,73,77,79,],[-30,-31,-37,-38,-39,-32,-27,-33,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,80,-40,-8,]),'TO':([12,17,19,20,21,41,42,43,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,77,79,83,],[-30,-31,-37,-38,-39,-32,-27,-33,-28,-29,-36,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-26,-40,-8,88,]),'LBRACE':([74,],[82,]),'RBRACE':([82,86,90,92,],[-7,89,-7,-6,]),'UNTIL':([91,],[93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'uz':([0,2,],[1,22,]),'line':([0,2,],[2,2,]),'stmt':([0,2,82,90,],[4,4,87,87,]),'exp':([0,2,6,7,10,14,15,18,27,28,29,30,31,32,33,34,35,36,37,38,39,40,45,46,49,69,75,80,82,90,],[5,5,41,43,47,50,51,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,70,73,76,78,83,73,5,5,]),'optargs':([46,],[71,]),'args':([46,80,],[72,85,]),'stmtblock':([74,],[81,]),'stmtS':([82,90,],[86,92,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> uz","S'",1,None,None,None),
  ('uz -> line uz','uz',2,'p_uz','YAPLUZparser.py',43),
  ('line -> stmt SEMICOL','line',2,'p_line_stmt','YAPLUZparser.py',49),
  ('uz -> error SEMICOL','uz',2,'p_uz_stmt_error','YAPLUZparser.py',58),
  ('uz -> <empty>','uz',0,'p_uz_empty','YAPLUZparser.py',64),
  ('stmtblock -> LBRACE stmtS RBRACE','stmtblock',3,'p_stmt_block','YAPLUZparser.py',69),
  ('stmtS -> stmt SEMICOL stmtS','stmtS',3,'p_stmtS','YAPLUZparser.py',84),
  ('stmtS -> <empty>','stmtS',0,'p_stmtS_empty','YAPLUZparser.py',90),
  ('exp -> NAME LPAREN optargs RPAREN','exp',4,'p_exp_call','YAPLUZparser.py',101),
  ('optargs -> args','optargs',1,'p_optargs','YAPLUZparser.py',105),
  ('optargs -> <empty>','optargs',0,'p_optargs_empty','YAPLUZparser.py',109),
  ('args -> exp COMMA args','args',3,'p_args','YAPLUZparser.py',113),
  ('args -> exp','args',1,'p_args','YAPLUZparser.py',114),
  ('exp -> exp PLUS exp','exp',3,'p_exp_bin','YAPLUZparser.py',122),
  ('exp -> exp MINUS exp','exp',3,'p_exp_bin','YAPLUZparser.py',123),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_bin','YAPLUZparser.py',124),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_bin','YAPLUZparser.py',125),
  ('exp -> exp POWER exp','exp',3,'p_exp_bin','YAPLUZparser.py',126),
  ('exp -> exp MODULUS exp','exp',3,'p_exp_bin','YAPLUZparser.py',127),
  ('exp -> exp AND exp','exp',3,'p_exp_compare','YAPLUZparser.py',133),
  ('exp -> exp OR exp','exp',3,'p_exp_compare','YAPLUZparser.py',134),
  ('exp -> exp GT exp','exp',3,'p_exp_compare','YAPLUZparser.py',135),
  ('exp -> exp LT exp','exp',3,'p_exp_compare','YAPLUZparser.py',136),
  ('exp -> exp GTE exp','exp',3,'p_exp_compare','YAPLUZparser.py',137),
  ('exp -> exp LTE exp','exp',3,'p_exp_compare','YAPLUZparser.py',138),
  ('exp -> exp EE exp','exp',3,'p_exp_compare','YAPLUZparser.py',139),
  ('exp -> exp NE exp','exp',3,'p_exp_compare','YAPLUZparser.py',140),
  ('exp -> NAME','exp',1,'p_exp_name','YAPLUZparser.py',149),
  ('exp -> MINUS INT','exp',2,'p_exp_num','YAPLUZparser.py',154),
  ('exp -> MINUS FLOAT','exp',2,'p_exp_num','YAPLUZparser.py',155),
  ('exp -> INT','exp',1,'p_exp_num','YAPLUZparser.py',156),
  ('exp -> FLOAT','exp',1,'p_exp_num','YAPLUZparser.py',157),
  ('exp -> DEC exp','exp',2,'p_exp_leftincdec','YAPLUZparser.py',166),
  ('exp -> INC exp','exp',2,'p_exp_leftincdec','YAPLUZparser.py',167),
  ('stmt -> exp DEC','stmt',2,'p_stmt_rightincdec','YAPLUZparser.py',176),
  ('stmt -> exp INC','stmt',2,'p_stmt_rightincdec','YAPLUZparser.py',177),
  ('exp -> NOT exp','exp',2,'p_exp_not','YAPLUZparser.py',186),
  ('exp -> TRUE','exp',1,'p_exp_boolean','YAPLUZparser.py',192),
  ('exp -> FALSE','exp',1,'p_exp_boolean','YAPLUZparser.py',193),
  ('exp -> STRING','exp',1,'p_exp_string','YAPLUZparser.py',201),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp_group','YAPLUZparser.py',205),
  ('stmt -> MAKE NAME','stmt',2,'p_makevar','YAPLUZparser.py',211),
  ('stmt -> MAKE NAME EQUAL exp','stmt',4,'p_initvar','YAPLUZparser.py',217),
  ('stmt -> NAME EQUAL exp','stmt',3,'p_assignment','YAPLUZparser.py',222),
  ('stmt -> IF exp THEN stmtblock','stmt',4,'p_if','YAPLUZparser.py',227),
  ('elif -> ELIF exp THEN stmtblock elif','elif',5,'p_elif','YAPLUZparser.py',243),
  ('elif -> <empty>','elif',0,'p_stmt_empty','YAPLUZparser.py',249),
  ('stmt -> FOR NAME EQUAL exp TO INT UNTIL','stmt',7,'p_stmt_for','YAPLUZparser.py',257),
  ('stmt -> PRINT LPAREN exp RPAREN','stmt',4,'p_stmt_print','YAPLUZparser.py',263),
  ('stmt -> RETURN exp','stmt',2,'p_stmt_return','YAPLUZparser.py',277),
]
