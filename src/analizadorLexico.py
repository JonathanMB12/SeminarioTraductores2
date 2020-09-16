import ply.lex as lex
import re
import codecs
import os
import sys

reservadas = ['IF','WHILE','RETURN','ELSE','INT',
		'FLOAT'
		]

tokens = reservadas+['ID','ENTERO','REAL','ADICION','RESTA','MULTIPLICACION','DIVISION',
		'ASIGNACION','MAYORQUE','MENORQUE', 'MAYORIGUAL','MENORIGUAL','DIFERENTE','IGUAL','AND','OR','NOT',
		'LPARENT', 'RPARENT','COMA','PUNTOYCOMA',
		 'LKEY', 'RKEY'
		]

t_ignore = '\t '
t_ADICION = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_MENORQUE = r'<'
t_MENORIGUAL = r'<='
t_MAYORQUE = r'>'
t_MAYORIGUAL = r'>='
t_DIFERENTE = r'!='
t_IGUAL = r'=='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'
t_COMA = r','
t_PUNTOYCOMA = r';'
#t_PUNTO = r'\.'


def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*'
	if t.value.upper() in reservadas:
		t.value = t.value.upper()
		#reservadas.get(t.value,'ID')
		t.type = t.value

	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_space(t):
	r'\s'
	t.lexer.lineno +=len(t.value)

#dsfjksdlgjklsdgjsdgslxcvjlk-,.
def t_COMMENT(t):
	r'\#.*'
	pass

def t_REAL(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_ENTERO(t):
	r'\d+'
	t.value = int(t.value)
	return t



def t_error(t):
	print (" Caracter ilegal '%s'" % t.value[0])
	t.lexer.skip(1)

def buscarFicheros(directorio):
	ficheros = []
	numArchivo = ''
	respuesta = False
	cont = 1

	for base, dirs, files in os.walk(directorio):
		ficheros.append(files)

	for file in files:
		print (str(cont)+". "+file)
		cont = cont+1

	while respuesta == False:
		numArchivo = input('\nNumero del test: ')
		for file in files:
			if file == files[int(numArchivo)-1]:
				respuesta = True
				break

	print ("Haz escogido \"%s\" \n" %files[int(numArchivo)-1])

	return files[int(numArchivo)-1]

directorio = 'C:/Users/hp/Documents/Seminario Traductores 2/Practicas/Proyecto/1. Analizador Lexico Python/Compilador_PL0/analizador version 1/test/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, mode = "r", encoding = "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()

analizador.input(cadena)

while True:
	tok = analizador.token()
	if not tok : break
	print (tok)



	
