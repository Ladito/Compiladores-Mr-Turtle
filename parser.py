#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

import ply.yacc as yacc
import re
import codecs
import os
from analizador.py import tokens
from sys import stdin

def p_program(p):
	'''program : PROGRAM ID var1 MAIN func1'''
	print "program"

def p_var1(p):
	'''var1 : varOps var2'''
	print "var1"

def p_var2(p):
	'''var2 : var1'''
	print "var2"

def p_var2Empty(p):
	'''var2 : empty'''
	print "null"

def p_varOps1(p):
    '''varOps : variableD'''
    print "varOps"

def p_varOps2(p):
    '''varOps : assign'''
    print "varOps"

def p_func1(p):
	'''func1 : function func2'''
	print "func1"

def p_func2(p):
	'''func2 : ID func1'''
	print "func2"

def p_func2Empty(p):
	'''func2 : empty'''
	print "null"

def p_function(p):
    '''function : parameter LKEY com1 funct1 RKEY'''
    print "function"

def p_com1(p):
    '''com1 : command com2'''
    print "com1"

def p_com2(p):
    '''com2 : com1'''
    print "com2"

def p_com2Empty(p):
    '''com2 : empty'''
    print "null"

def p_funct1(p):
    '''funct1 : RETURN value SEMICOLON'''
    print "funct1"

def p_funct1Empty(p):
    '''funct1 : empty'''
    print "null"

def p_commandOp1(p):
	'''command : variableD'''
	print "command"

def p_commandOp2(p):
	'''command : assign'''
	print "command"

def p_commandOp3(p):
	'''command : instruction'''
	print "command"

def p_commandOp4(p):
	'''command : condition'''
	print "command"

def p_variableD(p):
    '''variableD : type id1 SEMICOLON'''
    print "variableD"

def p_id1(p):
    '''id1 : ID id2'''
    print "id1"

def p_id2(p):
    '''id2 : COMMA id1'''
    print "id2"

def p_id2Empty(p):
    '''id2 : empty'''
    print "null"

def p_typeOp1(p):
    '''type : INT'''
    print "type"

def p_typeOp2(p):
    '''type : FLOAT'''
    print "type"

def p_typeOp3(p):
    '''type : LIST LBRAK type1 RBRAK'''
    print "type"

def p_type1Op1(p):
    '''type1 : INT'''
    print "type1"

def p_type1Op2(p):
    '''type1 : FLOAT'''
    print "type1"

def p_type1Op3(p):
    '''type1 : STRING'''
    print "type1"

def p_assign(p):
    '''assign : ID ASSIGN value SEMICOLON'''
    print "assign"

def p_valueOp1(p):
    '''value : value2'''
    print "value"

def p_valueOp2(p):
    '''value : CTES'''
    print "value"

def p_value2(p):
    '''value2 : value2type operator'''
    print "value2"

def p_value2typeOp1(p):
    '''value2type : CTEI'''
    print "value2type"

def p_value2typeOp2(p):
    '''value2type : CTEF'''
    print "value2type"

def p_value2typeOp3(p):
    '''value2type : ID'''
    print "value2type"

def p_value2typeOp4(p):
    '''value2type : funcReturn'''
    print "value2type"

def p_operatorOp1(p):
    '''operator : ADD value2'''
    print "operator"

def p_operatorOp2(p):
    '''operator : MINUS value2'''
    print "operator"

def p_operatorOp3(p):
    '''operator : TIMES value2'''
    print "operator"

def p_operatorOp4(p):
    '''operator : DIVISION value2'''
    print "operator"

def p_operatorOp5(p):
    '''operator : empty'''
    print "null"

def p_funcReturn(p):
    ''' funcReturn : ID parameter'''
    print "funcReturn"

def p_parameter(p):
    ''' parameter : LPAR param1 RPAR'''
    print "parameter"

def p_param1(p):
    ''' param1 : value COMMA param2'''
    print "param1"

def p_param2(p):
    ''' param2 : param1'''
    print "param2"

def p_param2(p):
    ''' param2 : empty'''
    print "null"

def p_condition(p):
    '''condition : cond1 LPAR statement RPAR LKEY com1 RKEY'''
    print "condition"

def p_cond1Op1(p):
    '''cond1 : IF'''
    print "cond1"

def p_cond1Op2(p):
    '''cond1 : WHILE'''
    print "cond1"

def p_statement(p):
    '''statement : value stateOp'''
    print "statement"

def p_stateOp(p):
    '''stateOp : stateoperator value'''
    print "stateOp"

def p_stateOpEmpty(p):
    '''stateOp : empty'''
    print "null"

def p_stateoperatorOp1(p):
    '''stateoperator : EQUALTO'''
    print "stateoperator"

def p_stateoperatorOp2(p):
    '''stateoperator : NOTEQUAL'''
    print "stateoperator"

def p_stateoperatorOp3(p):
    '''stateoperator : LESSTHAN'''
    print "stateoperator"

def p_stateoperatorOp4(p):
    '''stateoperator : GREATERTHAN'''
    print "stateoperator"

def p_stateoperatorOp5(p):
    '''stateoperator : LESSEQUAL'''
    print "stateoperator"

def p_stateoperatorOp6(p):
    '''stateoperator : GREATEREQUAL'''
    print "stateoperator"

def p_instruction(p):
    '''instruction : instOp SEMICOLON'''
    print "instruction"

def p_instOp1(p):
    '''instOp : instBloque1'''
    print "instOp"

def p_instOp2(p):
    '''instOp : instBloque2'''
    print "instOp"

def p_instOp3(p):
    '''instOp : instBloque3'''
    print "instOp"

def p_instBloque1(p):
    '''instBloque1 : instFunc LPAR value RPAR'''
    print "instBloque1"

def p_instBloque2(p):
    '''instBloque2 : COORDINATE LPAR value COMMA value RPAR'''
    print "instBloque2"

def p_instBloque3(p):
    '''instBloque3 : instStatus LPAR RPAR'''
    print "instBloque3"

def p_instStatusOp1(p):
    '''instStatus : ACTIVE'''
    print "instStatus"

def p_instStatusOp2(p):
    '''instStatus : DEACTIVE'''
    print "instStatus"

def p_instFuncOp1(p):
    '''instFunc : LEFT'''
    print "instFunc"

def p_instFuncOp2(p):
    '''instFunc : RIGHT'''
    print "instFunc"

def p_instFuncOp3(p):
    '''instFunc : STRAIGHT'''
    print "instFunc"

def p_instFuncOp4(p):
    '''instFunc : BACK'''
    print "instFunc"

def p_instFuncOp5(p):
    '''instFunc : COLOR'''
    print "instFunc"

def p_instFuncOp6(p):
    '''instFunc : WRITE'''
    print "instFunc"

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error de sintaxis ", p


parser = yacc.yacc()
