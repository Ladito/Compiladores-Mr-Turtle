import ply.lex as lex
import re
import codecs
import os
import sys

#Valid Tokens
tokens = ['ID', 'CTEI','CTEF','CTES','LPAR','RPAR','DOT','MINUS','ADD','EQUALS','ASSIGN',
'EQUALTO','NOTEQUAL','GREATERTHAN','LESSTHAN','COMMA','SEMICOLON','DIVISION',
'TIMES','LBRAK','RBRAK','GREATEREQUAL','LESSEQUAL','LKEY','RKEY']

#Valid words specific for the program
reservedWords = {
	'program' : 'PROGRAM',
	'function' : 'FUNCTION',
	'right' : 'RIGHT',
	'back' : 'BACK',
	'write' : 'WRITE',
	'coordinate' : 'COORDINATE',
	'activate' : 'ACTIVATE',
	'main' : 'MAIN',
	'left' : 'LEFT',
	'straight' : 'STRAIGHT',
	'color' : 'COLOR',
	'list' : 'LIST',
	'size' : 'SIZE',
	'deactivate' : 'DEACTIVATE',
	'return' : 'RETURN',
	'float' : 'FLOAT',
	'int' : 'INT',
	'if' : 'IF',
	'else' : 'ELSE',
	'string' : 'STRING',
	'while' : 'WHILE'
}

#Join both tokens and reserved words
tokens += reservedWords.values()

#Valid operations for the programs
t_ignore = '\t\n'
t_DOT = r'\.'
t_ADD = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVISION = r'\/'
t_COMMA = r'\,'
t_SEMICOLON = r'\;'
t_EQUALS = r'\:'
t_ASSIGN = r'\='
t_EQUALTO = r'\=\='
t_NOTEQUAL = r'\!\='
t_GREATERTHAN = r'\>'
t_LESSTHAN = r'\<'
t_GREATEREQUAL = r'\>\='
t_LESSEQUAL = r'\<\='
t_LPAR = r'\('
t_RPAR = r'\('
t_LKEY = r'\{'
t_RKEY = r'\}'
t_LBRAK = r'\['
t_RBRAK = r'\]'

#Adding specifications of variables
def t_ID(t):
    r'[a-zA-Z][a-z-A-Z0-9]*'
    if t.value in reservedWords:
        t.type = reservedWords[t.value]
    return t

def t_CTEI(t):
	r'\d+'
	t.value = int(t.value)
	return t

def t_CTES(t):
    r'\"[a-zA-Z0-9_\.\(\)-\[\]]*\"'
    return t

def t_CTEF(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_error(t):
    print ("Unvalid caracter")
    t.lexer.skip(1)

#Creating lexer
analizador = lex.lex()

#def verTokens(entrada):
#    lexer.input(entrada)
#    token = lexer.token()
#    while (token is not None):
#        print(token)
#        token = lexer.token()
