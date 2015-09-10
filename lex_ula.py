import ply.lex as lex
import sys

tokens = ['ID', 'FLOAT_LITERAL', 'AT', 'DOLLAR', 'HASH', 'AMPERSAND', 'EQUALS', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'WHITESPACE', 'COMMENT']
symbols = ['AT', 'DOLLAR', 'HASH', 'AMPERSAND', 'EQUALS', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS']
non_code = ['COMMENT', 'WHITESPACE']

t_ID = r'[a-zA-Z_][a-zA-Z0-9]*'
t_FLOAT_LITERAL = r'[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
t_AT = r'\@'
t_DOLLAR = r'\$'
t_HASH = r'\#'
t_AMPERSAND = r'\&'
t_EQUALS = r'\='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'

def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'

    if __name__ == '__main__':
    	return t
    else:
    	pass

def t_WHITESPACE(t):
    r'\s+'

    if __name__ == '__main__':
    	return t
    else:
    	pass

# Error handling rule
def t_error(t):
    print('Illegal character: %s' % t.value[0])
    t.lexer.skip(1)    

def get_token_str(token):
	token_str = 'defaultTokenString'

	if token.type in symbols:
		token_str = token.value
	elif token.type in non_code:
		token_str = token.type
	else:
		token_str = token.type + ',' + token.value

	return token_str



lex.lex()

def main(in_file, out_file):
	in_data = in_file.read()
	lex.input(in_data)
	while True:
		t = lex.token()
		if not t:
			break

		token_str = get_token_str(t)
		out_file.write(token_str + '\n')
		print(token_str)

if __name__ == '__main__':
	filename = sys.argv[1]
	in_file = open(filename, 'r')

	filename_prefix = filename[:filename.index('.')]
	out_file = open(filename_prefix + '.tkn', 'w')
	
	main(in_file, out_file)

	out_file.close()