from lexer import lexer
import sys

file = ""
if len(sys.argv) > 1:
  file = sys.argv[1]
else:
  file = '../io/code.elgol'

with open(file, 'r') as f:
  code = f.read()

lexer.input(code)

with open('../io/code.tlelgol', 'a') as token_file:
  token_file.truncate(0)
  while True:
    tok = lexer.token()
    if not tok:
      break
    if tok.type == 'error':
      token_file.truncate(0)
      break

    # Write token to file
    token_file.write(f"<{tok.type}, {tok.lineno}, {tok.lexpos}>\n")
    print(f"Token: Tipo='{tok.type}', Valor='{tok.value}', Linha={tok.lineno}, Posição={tok.lexpos}")  # Print the token