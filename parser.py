#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

import ply.yacc as yacc
import re
import codecs
import os
from lexer.py import tokens
from sys import stdin


dirProgram = {}
nameProgram = ""


def p_program(p):
	'''program : PROGRAM ID directFunc varD1 funcDec MAIN paramDeclare function'''

def p_directFunc(p):
	'''directFunc : '''
	global dirProgram
	global nameProgram
	nameProgram = [p-1]
	dirProgram[nameProgram] = {'Tipo : void', 'varsTable':{}} 

def p_varD1(p):
	'''varD1 : variableD varD2'''


def p_var2(p):
	'''varD2 : varD1'''


def p_varD2Empty(p):
	'''varD2 : empty'''


def p_funcDec(p):
	'''funcDec : functionDeclare funcDec2'''


def p_funcDec2(p):
	'''funcDec2 : funcDec'''


def p_funcDec2Empty(p):
	'''funcDec2 : empty'''


def p_functionDeclare(p):
	'''functionDeclare : function ID EQUALS typeS paramDeclare function'''


def p_function(p):
    '''function : LKEY com1 funct1 RKEY'''


def p_com1(p):
    '''com1 : command com2'''


def p_com2(p):
    '''com2 : com1'''


def p_com2Empty(p):
    '''com2 : empty'''


def p_funct1(p):
    '''funct1 : RETURN exp'''


def p_funct1Empty(p):
    '''funct1 : empty'''


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
	'''paramOp2 : COMMA paramOp1'''


def p_paramOp2(p):
	'''paramOp2 : empty'''


def p_commandOp1(p):
	'''command : funcCall'''


def p_commandOp2(p):
	'''command : assign'''


def p_commandOp3(p):
	'''command : instruction'''


def p_commandOp4(p):
	'''command : condition'''


def p_variableD(p):
    '''variableD : type vardID1'''


def p_varID1(p):
    '''varID1 : ID vardID2'''


def p_varID2(p):
    '''varID2 : COMMA vardID1'''


def p_varID2(p):
    '''varID2 : empty'''


def p_typeOp1(p):
    '''type : typeS'''


def p_typeOp2(p):
    '''type : LIST typeVar LBRAK CTEI RBRAK'''


def p_typeVarOp1(p):
	'''typeVar : INT'''


def p_typeVarOp2(p):
	'''typeVar : FLOAT'''


def p_typeSOp1(p):
	'''typeS : INT'''


def p_typeSOp2(p):
	'''typeS : FLOAT'''


def p_assign(p):
    '''assign : ID assignOp value SEMICOLON'''


def p_assignOp2(p):
	'''assignOp : LBRAK exp RBRAK'''


def p_assignOp1(p):
	'''assignOp : ASSIGN'''


def p_expresion(p):
	'''expresion : exp expresionOp'''


def p_expresionOp(p):
	'''expresionOp : eOperador exp'''


def p_expresionOp(p):
	'''expresionOp : empty'''


def p_eOperadorOp1(p):
    '''eOperador : EQUALTO'''


def p_eOperadorOp2(p):
    '''eOperador : NOTEQUAL'''


def p_eOperadorOp3(p):
    '''eOperador : LESSTHAN'''


def p_eOperadorOp4(p):
    '''eOperador : GREATERTHAN'''


def p_eOperadorOp5(p):
    '''eOperador : LESSEQUAL'''


def p_eOperadorOp6(p):
    '''eOperador : GREATEREQUAL'''


def p_exp(p):
    '''exp : termino expOp'''


def p_expOp1(p):
    '''expOp : ADD exp'''


def p_expOp2(p):
    '''expOp : MINUS exp'''


def p_expOp(p):
    '''expOp : empty'''


def p_termino(p):
    '''termino : factor termOp'''


def p_termOp1(p):
    '''termOp : TIMES termino'''


def p_termOp2(p):
    '''termOp : DIVISION termino'''


def p_termOp3(p):
    '''termOp : empty'''


def p_factorOp1(p):
	'''factor : LPAR funcCall RPAR'''


def p_factorOp2(p):
	'''factor : factOp varCte'''


def p_factOp1(p):
	'''factOp : ADD'''


def p_factOp2(p):
	'''factOp : MINUS'''


def p_factOp3(p):
	'''factOp : empty'''


def p_varCteOp1(p):
	'''varCte : ID'''


def p_varCteOp2(p):
	'''varCte : CTEI'''


def p_varCteOp3(p):
	'''varCte : CTEF'''


def p_varCteOp4(p):
	'''varCte : CTES'''


def p_varCteOp5(p):
	'''varCte : funcCall'''


def p_funcCall(p):
    ''' funcCall : ID parameter'''


def p_conditionOp1(p):
    '''condition : condIf'''


def p_conditionOp2(p):
    '''condition : condWhile'''


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
    '''condOp2 : condOp1'''


def p_condOp2(p):
    '''condOp1 : empty'''


def p_instruction(p):
    '''instruction : instOp SEMICOLON'''


def p_instOp1(p):
    '''instOp : instBloque1'''


def p_instOp2(p):
    '''instOp : instBloque2'''


def p_instOp3(p):
    '''instOp : instBloque3'''


def p_instBloque1(p):
    '''instBloque1 : instFunc LPAR exp RPAR'''


def p_instBloque2(p):
    '''instBloque2 : COORDINATE LPAR exp COMMA exp RPAR'''


def p_instBloque3(p):
    '''instBloque3 : instStatus LPAR RPAR'''


def p_instStatusOp1(p):
    '''instStatus : ACTIVATE'''


def p_instStatusOp2(p):
    '''instStatus : DEACTIVATE'''


def p_instFuncOp1(p):
    '''instFunc : LEFT'''


def p_instFuncOp2(p):
    '''instFunc : RIGHT'''


def p_instFuncOp3(p):
    '''instFunc : STRAIGHT'''


def p_instFuncOp4(p):
    '''instFunc : BACK'''


def p_instFuncOp5(p):
    '''instFunc : COLOR'''


def p_instFuncOp6(p):
    '''instFunc : WRITE'''


def p_empty(p):
	'''empty :'''
	pass

def p_error(p):



parser = yacc.yacc()
