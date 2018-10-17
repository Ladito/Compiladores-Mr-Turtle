#Gala Stefanía Ramos Islas a00817135
#Luis Adolfo Diaz Torres   A01280862

import ply.lex as lex
import re
import codecs
import os
import sys

reserved = ['PROGRAM','RIGHT','BACK','WIRTE','COORDINATE','ACTIVE',
			'MAIN','LEFT', 'STRAIGHT', 'COLOR','LIST','SIZE','DEACTIVE','RETURN',
			'FLOAT','INT','IF','STRING','WHILE','ELSE']

tokens = reserved+['ID', 'CTEI','CTEF','CTES','LPAR','RPAR','DOT','MINUS','ADD','ASSIGN',
					'EQUALTO','NOTEQUAL','GREATERTHAN','LESSTHAN','COMMA','SEMICOLON','DIVISION'
					'TIMES','LBRAK','RBRAK','GREATEREQUAL','LESSEQUAL','LKEY','RKEY']

t_ignore = '\t'
t_LPAR = r'\('
t_RPAR = r'\('
t_DOT = r'\.'
t_ADD = r'\+'
t_MINUS = r'\-'
t_ASSIGN = r'='
t_EQUALTO = r'=='
t_NOTEQUAL = r'!='
t_GREATERTHAN = r'>'
t_LESSTHAN = r'<'
t_TIMES = r'\*'
t_DIVISION = r'/'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_GREATEREQUAL = r'>='
t_LESSEQUAL = r'<='
t_LBRAK = r'['
t_RBRAK = r']'

def t_ID(t):
    r'[a-zA-Z][a-z-A-Z0-9]*'
    if t.value.upper() in reserved:
        t.value = t.value.upper()
        t.type = t.value
    return t

def t_CTEI(t):
	r'[0-9]+'
	return t

def t_CTES(t):
    r'" .*"'
    return t

def t_CTEF(t):
    r'[0-9]*\.[0-9]+'
    return t

def t_error(t):
    print "Ese caracter no es valido '%s'" % t.value[0]
    t.lexer.skip(1)


analizador = lex.lex()

while True:
    tok = analizador.token()
    if not tok : break
    print tok
