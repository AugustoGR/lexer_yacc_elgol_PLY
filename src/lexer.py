import ply.lex as lex

reserved = {
  'elgio':      'ELGIO',
  'inteiro':   'INTEIRO',
  'zero':      'ZERO',
  'comp':      'COMP',
  'enquanto':  'ENQUANTO',
  'se':        'SE',
  'entao':     'ENTAO',
  'senao':     'SENAO',
  'inicio':    'INICIO',
  'fim':       'FIM',
  'maior':     'MAIOR',
  'menor':     'MENOR',
  'igual':     'IGUAL',
  'diferente': 'DIFERENTE'
}

tokens = [
  'NUMBER',
  'PLUS',
  'MINUS',
  'TIMES',
  'DIVIDE',
  'LPAREN',
  'RPAREN',
  'EQUALS',
  'ID',
  'FUNCTION',
  'DOT',
  'COMMA',
] + list(reserved.values())

t_PLUS    = r'\+'
t_EQUALS  = r'='
t_MINUS   = r'-'
t_TIMES   = r'x'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_DOT     = r'\.'
t_COMMA   = r','
t_ignore  = ' \t'

def t_NUMBER(t):
  r'[1-9]\d*'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[A-Z][a-zA-Z]{2,}'
  return t

def t_RESERVED(t):
  # eu tentei fazer isso lendo da lista de palavras reservadas mas não funcionou de geito nenhum
  r'\b(elgio|inteiro|zero|comp|enquanto|se|entao|senao|inicio|fim|maior|menor|igual|diferente)\b'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_FUNCTION(t):
  r'_[A-Z][a-zA-Z]{2,}'
  t.type = 'FUNCTION'
  return t

def t_COMMENT(t):
  r'\#.*'
  pass

def t_error(t):
  print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
  t.lexer.skip(len(t.value))
  return t

def t_newline(t):
  r'\n+'
  t.lexer.lineno += len(t.value)

lexer = lex.lex()