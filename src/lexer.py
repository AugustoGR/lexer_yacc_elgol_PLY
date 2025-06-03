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
  'NUMERO',
  'MAIS',
  'MENOS',
  'VEZES',
  'DIVIDIDO',
  'LPAREN',
  'RPAREN',
  'IGUALATRIBUTO',
  'ID',
  'FUNCAO',
  'PONTO',
  'VIRGULA',
] + list(reserved.values())

t_MAIS    = r'\+'
t_IGUALATRIBUTO   = r'='
t_MENOS   = r'-'
t_VEZES   = r'x'
t_DIVIDIDO  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_PONTO   = r'\.'
t_VIRGULA = r','
t_ignore  = ' \t'

def t_NUMERO(t):
  r'[1-9]\d*'
  t.value = int(t.value)
  return t

def t_ID(t):
  r'[A-Z][a-zA-Z]{2,}'
  return t

def t_RESERVADO(t):
  # eu tentei fazer isso lendo da lista de palavras reservadas mas não funcionou de geito nenhum
  r'\b(elgio|inteiro|zero|comp|enquanto|se|entao|senao|inicio|fim|maior|menor|igual|diferente)\b'
  t.type = reserved.get(t.value, 'ID')
  return t

def t_FUNCAO(t):
  r'_[A-Z][a-zA-Z]{2,}'
  t.type = 'FUNCAO'
  return t

def t_COMENTARIO(t):
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