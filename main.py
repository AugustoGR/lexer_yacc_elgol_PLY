import ply.lex as lex
import re

reservedWords = (
  'elgio',
  'inteiro',
  'zero',
  'comp',
  'enquanto',
  'se'
  'entao',
  'senao',
  'inicio',
  'fim',
  'maior',
  'menor',
  'igual',
  'diferente'
)

tableSymbols: list[tuple[str, str, str]] = []
tokenList: list[str] = []

file = open('code-test.txt', 'r')

def read_lines_in_file():
  lineNumber: int = 0

  for line in file:
    line = line.strip()

    lineNumber += 1

    if line_is_empty_or_comment(line):
      continue
    
    # \s+: separa por espaços (remove os espaços).
    # (?<=[(),.]): divide depois de (, ), ,, ..
    # (?=[(),.]): divide antes de (, ), ,, ..
    tokens: list[str] = re.split(r'\s+|(?<=[(),.])|(?=[(),.])', line)
    tokens = [t for t in tokens if t.strip()]

    for token in tokens:
      
      # VERIFICAR SE É COMENTÁRIO
      if is_comment(token):
        break

      # VERIFICAR SE O TOKEN JÁ ESTÁ NA TABELA DE SÍMBOLOS. SE ESTIVER, ADICIONAR NA LISTA DE TOKENS
      matched = False
      for symbol in tableSymbols:
          if token == symbol[1]:
              matched = True
              break
      if matched:
          tokenList.append(f'<{symbol[2]},{symbol[0]},{lineNumber}>')
          continue

      # VERIFICAR SE O TOKEN É UMA PALAVRA RESERVADA
      if token in reservedWords:
        register_token(token, 'res', lineNumber)

      # VERIFICAR SE O TOKEN É UM IDENTIFICADOR
      elif re.match(r"^[A-Z][a-zA-Z]{2,}$", token):
        register_token(token, 'id', lineNumber)

      # VERIFICA SE O TOKEN É UMA FUNÇÃO
      elif re.match(r"^_[A-Z][a-z]+$", token):
        register_token(token, 'func', lineNumber)

      # VERIFICAR SE O TOKEN É UM NÚMERO
      elif re.match(r"^[1-9][0-9]*$", token):
        register_token(token, 'num', lineNumber)

      # VERIFICAR SE O TOKEN É UM OPERADOR OU PONTUAÇÃO
      elif re.match(r"^[(),.]$", token):
        register_token(token, 'op', lineNumber)

def line_is_empty_or_comment(line: str) -> bool:
  return len(line) == 0 or re.match(r'^\s*#', line)

def is_comment(token: str) -> bool:
  return re.match(r'^#', token)

def register_token(token: str, type: str, lineNumber: int) -> None:
  id: int = len(tableSymbols) + 1
  tokenList.append(f'<{type},{id},{lineNumber}>')
  tableSymbols.append((id, token, type))

read_lines_in_file()

print('.:TABELA DE SÍMBOLOS:.')
for symbol in tableSymbols:
    print(f'{symbol[0]} | {symbol[1]} | {symbol[2]}')
print('\n.:LISTA DE TOKENS:.')
for token in tokenList:
    print(token)