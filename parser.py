#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

import ply.yacc as yacc
import lexer as scanner
import re
import codecs
import os
from analizador.py import tokens
from sys import stdin

precedence = (
    ('left','ADD','MINUS'),
    ('left','TIMES','DIVISION'),
)

def p_program(p):
	'''program : PROGRAM ID varD1 funcDec MAIN paramDeclare function'''
	print "program"
	#p[0] = program(p[3],p[5], "program")

def p_varD1(p):
	'''varD1 : variableD varD2'''
	print "varD1"
	#p[0] = var1(p[1],p[2], "var1")

def p_var2(p):
	'''varD2 : varD1'''
	print "vard2"
	#p[0] = var2(p[1], "var2")

def p_varD2Empty(p):
	'''varD2 : empty'''
	print "null"
	#p[0] = NULL()

def p_funcDec(p):
	'''funcDec : functionDeclare funcDec2'''
	print "funcDec"
	#p[0] = program(p[3],p[5], "program")

def p_funcDec2(p):
	'''funcDec2 : funcDec'''
	print "funcDec2"
	#p[0] = program(p[3],p[5], "program")

def p_funcDec2Empty(p):
	'''funcDec2 : empty'''
	print "null"
	#p[0] = NULL()

def p_functionDeclare(p):
	'''functionDeclare : function ID EQUALS typeS paramDeclare function'''
	print "functionDeclare"

def p_function(p):
    '''function : LKEY com1 funct1 RKEY'''
    print "function"
	#p[0] = program(p[3],p[5], "program")

def p_com1(p):
    '''com1 : command com2'''
    print "com1"
	#p[0] = program(p[3],p[5], "program")

def p_com2(p):
    '''com2 : com1'''
    print "com2"
	#p[0] = program(p[3],p[5], "program")

def p_com2Empty(p):
    '''com2 : empty'''
    print "null"
	#p[0] = NULL()

def p_funct1(p):
    '''funct1 : RETURN exp'''
    print "funct1"
	#p[0] = program(p[3],p[5], "program")

def p_funct1Empty(p):
    '''funct1 : empty'''
    print "null"
	#p[0] = NULL()

def p_paramDeclare(p):
	'''paramDeclare : LPAR paramD1 RPAR'''
	print "paramDeclare"

def p_paramD1(p):
	'''paramD1 : typeS ID paramD2'''
	print "paramD1"

def p_paramD2(p):
	'''paramD2 : COMMA paramD1'''
	print "paramD2"

def p_parameter(p):
	'''parameter : LPAR paramOp1 RPAR'''
	print "parameter"

def p_paramOp1(p):
	'''paramOp1 : exp paramOp2'''
	print "paramOp1"

def p_paramOp2(p):
	'''paramOp2 : COMMA paramOp1'''
	print "paramOp2"

def p_paramOp2(p):
	'''paramOp2 : empty'''
	print "null"

def p_commandOp1(p):
	'''command : funcCall'''
	print "command"
	#p[0] = command(p[3],p[5], "command")

def p_commandOp2(p):
	'''command : assign'''
	print "command"
	#p[0] = command(p[3],p[5], "command")

def p_commandOp3(p):
	'''command : instruction'''
	print "command"
	#p[0] = command(p[3],p[5], "command")

def p_commandOp4(p):
	'''command : condition'''
	print "command"
	#p[0] = command(p[3],p[5], "command")

def p_variableD(p):
    '''variableD : type vardID1'''
    print "variableD"
	#p[0] = variableD(p[3],p[5], "variableD")

def p_varID1(p):
    '''varID1 : ID vardID2'''
    print "varID1"

def p_varID2(p):
    '''varID2 : COMMA vardID1'''
    print "varID2"

def p_varID2(p):
    '''varID2 : empty'''
    print "null"

def p_typeOp1(p):
    '''type : typeS'''
    print "type"
	#p[0] = type(p[3],p[5], "type")

def p_typeOp2(p):
    '''type : LIST typeVar LBRAK CTEI RBRAK'''
    print "type"
	#p[0] = type(p[3],p[5], "type")

def p_typeVarOp1(p):
	'''typeVar : INT'''
	print "typeVar"

def p_typeVarOp2(p):
	'''typeVar : FLOAT'''
	print "typeVar"

def p_typeSOp1(p):
	'''typeS : INT'''
	print "typeS"

def p_typeSOp2(p):
	'''typeS : FLOAT'''
	print "typeS"

def p_assign(p):
    '''assign : ID assignOp value SEMICOLON'''
    print "assign"
	#p[0] = assign(p[3],p[5], "assign")

def p_assignOp2(p):
	'''assignOp : LBRAK exp RBRAK'''
	print "assignOp"

def p_assignOp1(p):
	'''assignOp : ASSIGN'''
	print "assignOp"

def p_expresion(p):
	'''expresion : exp expresionOp'''
	print "expresion"

def p_expresionOp(p):
	'''expresionOp : eOperador exp'''
	print "expresionOp"

def p_expresionOp(p):
	'''expresionOp : empty'''
	print "null"

def p_eOperadorOp1(p):
    '''eOperador : EQUALTO'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_eOperadorOp2(p):
    '''eOperador : NOTEQUAL'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_eOperadorOp3(p):
    '''eOperador : LESSTHAN'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_eOperadorOp4(p):
    '''eOperador : GREATERTHAN'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_eOperadorOp5(p):
    '''eOperador : LESSEQUAL'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_eOperadorOp6(p):
    '''eOperador : GREATEREQUAL'''
    print "eOperador"
	#p[0] = program(p[3],p[5], "program")operator"

def p_exp(p):
    '''exp : termino expOp'''
    print "exp"

def p_expOp1(p):
    '''expOp : ADD exp'''
    print "expOp"

def p_expOp2(p):
    '''expOp : MINUS exp'''
    print "expOp"

def p_expOp(p):
    '''expOp : empty'''
    print "null"

def p_termino(p):
    '''termino : factor termOp'''
    print "termino"

def p_termOp1(p):
    '''termOp : TIMES termino'''
    print "termOp"

def p_termOp2(p):
    '''termOp : DIVISION termino'''
    print "termOp"

def p_termOp3(p):
    '''termOp : empty'''
    print "null"

def p_factorOp1(p):
	'''factor : LPAR funcCall RPAR'''
	print "factor"

def p_factorOp2(p):
	'''factor : factOp varCte'''
	print "factor"

def p_factOp1(p):
	'''factOp : ADD'''
	print "factOp"

def p_factOp2(p):
	'''factOp : MINUS'''
	print "factOp"

def p_factOp3(p):
	'''factOp : empty'''
	print "null"

def p_varCteOp1(p):
	'''varCte : ID'''
	print "varCte"

def p_varCteOp2(p):
	'''varCte : CTEI'''
	print "varCte"

def p_varCteOp3(p):
	'''varCte : CTEF'''
	print "varCte"

def p_varCteOp4(p):
	'''varCte : CTES'''
	print "varCte"

def p_varCteOp5(p):
	'''varCte : funcCall'''
	print "varCte"

def p_funcCall(p):
    ''' funcCall : ID parameter'''
    print "funcCall"
	#p[0] = funcReturn(p[3],p[5], "funcReturn")

def p_conditionOp1(p):
    '''condition : condIf'''
    print "condition"

def p_conditionOp2(p):
    '''condition : condWhile'''
    print "condition"

def p_condIF(p):
    '''condIf : IF LPAR expresion RPAR LKEY condOp1 RKEY condElse'''
    print "condIf"
	#p[0] = program(p[3],p[5], "program")tion"

def p_condWhile(p):
    '''condWhile : WHILE LPAR expresion RPAR LKEY condOp1 RKEY'''
    print "condWhile"
	#p[0] = program(p[3],p[5], "program")tion"

def p_condElse(p):
    '''condElse : ELSE LKEY condOp1 RKEY'''
    print "condElse"
	#p[0] = program(p[3],p[5], "program")tion"

def p_condOp1(p):
    '''condOp1 : command condOp2'''
    print "condOp1"

#DUDAAAAA! porque de todos los commands func Call no tiene ninguna comma o ; para poner otro y aqui no se especifica tampoco
def p_condOp2(p):
    '''condOp2 : condOp1'''
    print "condOp2"

def p_condOp2(p):
    '''condOp1 : empty'''
    print "null"

def p_instruction(p):
    '''instruction : instOp SEMICOLON'''
    print "instruction"
	#p[0] = program(p[3],p[5], "program")uction"

def p_instOp1(p):
    '''instOp : instBloque1'''
    print "instOp"
	#p[0] = program(p[3],p[5], "program")p"

def p_instOp2(p):
    '''instOp : instBloque2'''
    print "instOp"
	#p[0] = program(p[3],p[5], "program")p"

def p_instOp3(p):
    '''instOp : instBloque3'''
    print "instOp"
	#p[0] = program(p[3],p[5], "program")p"

def p_instBloque1(p):
    '''instBloque1 : instFunc LPAR exp RPAR'''
    print "instBloque1"
	#p[0] = program(p[3],p[5], "program")loque1"

def p_instBloque2(p):
    '''instBloque2 : COORDINATE LPAR exp COMMA exp RPAR'''
    print "instBloque2"
	#p[0] = program(p[3],p[5], "program")loque2"

def p_instBloque3(p):
    '''instBloque3 : instStatus LPAR RPAR'''
    print "instBloque3"
	#p[0] = program(p[3],p[5], "program")loque3"

def p_instStatusOp1(p):
    '''instStatus : ACTIVATE'''
    print "instStatus"
	#p[0] = program(p[3],p[5], "program")tatus"

def p_instStatusOp2(p):
    '''instStatus : DEACTIVATE'''
    print "instStatus"
	#p[0] = program(p[3],p[5], "program")tatus"

def p_instFuncOp1(p):
    '''instFunc : LEFT'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_instFuncOp2(p):
    '''instFunc : RIGHT'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_instFuncOp3(p):
    '''instFunc : STRAIGHT'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_instFuncOp4(p):
    '''instFunc : BACK'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_instFuncOp5(p):
    '''instFunc : COLOR'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_instFuncOp6(p):
    '''instFunc : WRITE'''
    print "instFunc"
	#p[0] = program(p[3],p[5], "program")unc"

def p_empty(p):
	'''empty :'''
	pass

def p_error(p):
	print "Error"
	#p[0] = program(p[3],p[5], "program") de sintaxis ", p


parser = yacc.yacc()
