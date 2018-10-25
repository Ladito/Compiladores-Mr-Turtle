#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

import ply.yacc as yacc
import re
import codecs
import os
from lexer.py import tokens
from sys import stdin


dirProgram = {}
idProgram = ""
type = ""
idFunc = ""


def p_program(p):
	'''program : PROGRAM ID directFunc varD1 funcDec MAIN paramDeclare function'''

def p_directFunc(p):
	'''directFunc : '''
	global dirProgram
	global idProgram
	idProgram = [p-1]
	dirProgram[idProgram] = {'tipo' : 'void', 'varsTable':{}}

def p_varD1(p):
	'''varD1 : variableD varD2'''

def p_var2(p):
	'''varD2 : varD1
			 | '''

def p_funcDec(p):
	'''funcDec : functionDeclare funcDec2'''

def p_funcDec2(p):
	'''funcDec2 : funcDec
				| '''

def p_functionDeclare(p):
	'''functionDeclare : function ID funcId EQUALS typeS paramDeclare function'''

def p_funcId(p):
	'''funcId : '''
	global dirProgram
    global type
    idFunc = p[-1]
    #direction = set_dir_global(typo,1)
    dirProgram[nombrePrograma]['Vars'][idFunc] = {'Type': type, 'Scope': "global"}
    #setValueGlobal(direccion,None)

def p_function(p):
    '''function : LKEY com1 funct1 RKEY'''

def p_com1(p):
    '''com1 : command com2'''

def p_com2(p):
    '''com2 : com1
			| '''


def p_funct1(p):
    '''funct1 : RETURN exp
		      | '''


def p_paramDeclare(p):
	'''paramDeclare : LPAR paramD1 RPAR'''


def p_paramD1(p):
	'''paramD1 : typeS ID paramD2'''


def p_paramD2(p):
	'''paramD2 : COMMA paramD1'''


def p_parameter(p):
	'''parameter : LPAR paramOp1 RPAR'''


def p_paramOp1(p):
	'''paramOp1 : exp paramOp2'''


def p_paramOp2(p):
	'''paramOp2 : COMMA paramOp1
				| '''


def p_command(p):
	'''command : funcCall
			   | assign
			   | instruction
			   | condition'''


def p_variableD(p):
    '''variableD : type vardID1'''


def p_varID1(p):
    '''varID1 : ID vardID2'''


def p_varID2(p):
    '''varID2 : COMMA vardID1
			  | '''


def p_type(p):
    '''type : typeS
			| LIST typeS LBRAK CTEI RBRAK'''

def p_typeS(p):
	'''typeS : INT
			 | FLOAT'''
	global type
    type = p[1]

def p_assign(p):
    '''assign : ID assignOp value SEMICOLON'''


def p_assignOp(p):
	'''assignOp : ASSIGN
				| LBRAK exp RBRAK'''


def p_expresion(p):
	'''expresion : exp expresionOp'''


def p_expresionOp(p):
	'''expresionOp : eOperador exp
				   | '''


def p_eOperador(p):
    '''eOperador : EQUALTO
				 | NOTEQUAL
				 | LESSTHAN
				 | GREATERTHAN
				 | LESSEQUAL
				 | GREATEREQUAL'''

def p_exp(p):
    '''exp : termino expOp'''


def p_expOp(p):
    '''expOp : ADD exp
			 | MINUS exp
			 | '''


def p_termino(p):
    '''termino : factor termOp'''


def p_termOp(p):
    '''termOp : TIMES termino
			  | DIVISION termino
			  | '''


def p_factor(p):
	'''factor : LPAR funcCall RPAR
			  | factOp varCte'''


def p_factOp(p):
	'''factOp : ADD
			  | MINUS
			  | '''


def p_varCte(p):
	'''varCte : ID
			  | CTEI
			  | CTEF
			  | CTES
			  | funcCall'''


def p_funcCall(p):
    ''' funcCall : ID parameter'''


def p_condition(p):
    '''condition : condIf
				 | condWhile'''


def p_condIF(p):
    '''condIf : IF LPAR expresion RPAR LKEY condOp1 RKEY condElse'''


def p_condWhile(p):
    '''condWhile : WHILE LPAR expresion RPAR LKEY condOp1 RKEY'''


def p_condElse(p):
    '''condElse : ELSE LKEY condOp1 RKEY'''


def p_condOp1(p):
    '''condOp1 : command condOp2'''


#DUDAAAAA! porque de todos los commands func Call no tiene ninguna comma o ; para poner otro y aqui no se especifica tampoco
def p_condOp2(p):
    '''condOp2 : condOp1
			   | '''


def p_instruction(p):
    '''instruction : instOp SEMICOLON'''


def p_instOp(p):
    '''instOp : instBloque1
			  | instBloque2
			  | instBloque3'''


def p_instBloque1(p):
    '''instBloque1 : instFunc LPAR exp RPAR'''


def p_instBloque2(p):
    '''instBloque2 : COORDINATE LPAR exp COMMA exp RPAR'''


def p_instBloque3(p):
    '''instBloque3 : instStatus LPAR RPAR'''


def p_instStatusOp(p):
    '''instStatus : ACTIVATE
				  | DEACTIVATE'''


def p_instFunc(p):
    '''instFunc : LEFT
				| RIGHT
				| STRAIGHT
				| BACK
				| COLOR
				| WRITE'''

def p_error(p):



parser = yacc.yacc()
