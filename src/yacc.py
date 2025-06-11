import ply.yacc as yacc
from lexer import tokens
# Definição das regras de expressões matemáticas

def p_expression_assignment(p):
    '''expression : ID IGUALATRIBUTO expression_math PONTO'''
    p[0] = ('assignment', p[1], p[3])

def p_expression_math_binop(p):
    '''expression_math : expression_math MAIS expression_math
                       | expression_math MENOS expression_math
                       | expression_math VEZES expression_math
                       | expression_math DIVIDIDO expression_math'''
    p[0] = (p[2], p[1], p[3])

def p_expression_math_operand(p):
    '''expression_math : ID
                       | NUMERO
                       | function_call
                       | ZERO'''
    p[0] = p[1]

# Definição das regras de funções

def p_function_definition(p):
    '''function_definition : INTEIRO FUNCAO LPAREN parameter_list RPAREN PONTO block'''
    p[0] = ('function_def', p[7])

def p_function_definitions(p):
    '''function_definitions : function_definition
                            | function_definitions function_definition'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_function_call(p):
    '''function_call : FUNCAO LPAREN argument_list RPAREN '''
    p[0] = ('function_call', p[1], p[3])

def p_argument_list(p):
    '''argument_list : expression_math
                     | argument_list VIRGULA expression_math
                     | empty'''
    if len(p) == 2:
        if p[1] is None:  # empty
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[1].append(p[3])
        p[0] = p[1]

def p_empty(p):
    '''empty :'''
    pass

def p_parameter_list(p):
    '''parameter_list : INTEIRO ID
                      | parameter_list VIRGULA INTEIRO ID
                      | empty'''
    if len(p) == 2:
        if p[1] is None:  # empty
            p[0] = []
        else:
            p[0] = []
    elif len(p) == 3:
        p[0] = [(p[1], p[2])]
    else:
        p[1].append((p[3], p[4]))
        p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement
                      | empty'''
    if len(p) == 2:
        if p[1] is None:  # empty
            p[0] = []
        else:
            p[0] = [p[1]]
    else:
        p[1].append(p[2])
        p[0] = p[1]

def p_statement(p):
    '''statement : expression
                 | variable_declaration
                 | loop
                 | if_statement
                 | comp
                 | elgio_assignment'''
    p[0] = p[1]

def p_variable_declaration(p):
    '''variable_declaration : INTEIRO ID PONTO'''
    p[0] = ('var_decl', p[2])

def p_elgio_assignment(p):
    '''elgio_assignment : ELGIO IGUALATRIBUTO elgio_expression PONTO'''
    p[0] = ('elgio', p[3])

def p_elgio_expression(p):
    '''elgio_expression : elgio_expression MAIS elgio_expression
                        | elgio_expression MENOS elgio_expression
                        | elgio_expression VEZES elgio_expression
                        | elgio_expression DIVIDIDO elgio_expression
                        | ID
                        | NUMERO
                        | ZERO'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = (p[2], p[1], p[3])

# Definição das regras de laços, condicionais e bloco principal

def p_conditional_expression(p):
    '''conditional_expression : ID MAIOR ID
                                | ID MENOR ID
                                | ID IGUAL ID
                                | ID DIFERENTE ID
                                | ID MAIOR NUMERO
                                | ID MENOR NUMERO
                                | ID IGUAL NUMERO
                                | ID DIFERENTE NUMERO
                                | NUMERO MAIOR ID
                                | NUMERO MENOR ID
                                | NUMERO IGUAL ID
                                | NUMERO DIFERENTE ID
                                | ID MAIOR ZERO
                                | ID MENOR ZERO
                                | ID IGUAL ZERO
                                | ID DIFERENTE ZERO
                                | ZERO MAIOR ID
                                | ZERO MENOR ID
                                | ZERO IGUAL ID
                                | ZERO DIFERENTE ID
                                | NUMERO MAIOR ZERO
                                | NUMERO MENOR ZERO
                                | NUMERO IGUAL ZERO
                                | NUMERO DIFERENTE ZERO
                                | ZERO MAIOR NUMERO
                                | ZERO MENOR NUMERO
                                | ZERO IGUAL NUMERO
                                | ZERO DIFERENTE NUMERO
                                | ZERO MAIOR ZERO'''
    p[0] = ('conditional', p[1], p[2], p[3])

def p_loop(p):
    '''loop : ENQUANTO conditional_expression block'''
    p[0] = ('loop', p[2], p[4])

def p_if_statement(p):
    '''if_statement : SE conditional_expression PONTO ENTAO PONTO block SENAO PONTO block
                    | SE conditional_expression PONTO ENTAO PONTO block'''
    if len(p) == 9:  # with SENAO
        p[0] = ('if', p[2], p[6], p[8])
    else:  # without SENAO
        p[0] = ('if', p[2], p[6], None)

def p_comp(p):
    '''comp : COMP  expression_math PONTO'''
    p[0] = ('comp', p[2])

def p_program(p):
    '''program : block
               | function_definitions block'''
    if len(p) == 2:
        p[0] = ('program', p[1])
    else:
        p[0] = ('program', p[1], p[2])

def p_block(p):
    '''block : INICIO PONTO statement_list FIM PONTO'''
    p[0] = ('block', p[3])

def p_error(p):
    if p:
        if hasattr(p, 'lineno') and p.lineno:
            print(f"Erro sintático na linha {p.lineno}: token inesperado '{p.value}'")
        else:
            print(f"Erro sintático: token inesperado '{p.value}'")
    else:
        print("Erro sintático: fim de arquivo inesperado")
    
parser = yacc.yacc(start='program', outputdir='../io')

