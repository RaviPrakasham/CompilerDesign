from ply import lex
tokens=(
    'NUMBER',
    'KEYWORD',
    'OPERATOR',
    'IDENTIFIER',
    'STRING',    
)
t_KEYWORD=r'if|else|while|for|int|float|char|return'
t_OPERATOR=r'\+|-|\*|/|=|==|<|>|<=|>='
t_IDENTIFIER=r'[a-z A-Z_][a-z A-Z 0-9]*'
t_STRING=r'"([^"]*)"'
def t_Number(t):
    r'\d+'
    t.value=int(t.value)
    return t
def t_newline(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)
    t.ignore='\t'
def t_error(t):
    print(f"illegal character'{t.value[0]}")
    t.lexer.skip(1)
lexer=lex.lex()
data=input()
lexer.input(data)
for tok in lexer:
    print(tok)