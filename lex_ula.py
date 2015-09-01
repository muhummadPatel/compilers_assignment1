import ply.lex as lex
import sys

tokens = ['ID', 'FLOAT_LITERAL', 'AT', 'DOLLAR', 'HASH', 'AMPERSAND', 'EQUALS', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS', 'WHITESPACE', 'COMMENT']

t_ID = r'[a-zA-Z_][a-zA-Z0-9]*'
t_FLOAT_LITERAL = r'[+-]?[0-9]+(\.[0-9]+)?([eE][+-]?[0-9]+)?'
t_AT = r'\@'
t_DOLLAR = r'\$'
t_HASH = r'\#'
t_AMPERSAND = r'\&'
t_EQUALS = r'\='
t_LEFT_PARENTHESIS = r'\('
t_RIGHT_PARENTHESIS = r'\)'
t_WHITESPACE = r'\s+'
t_COMMENT = r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'   #r'(/\*(.|\s)*\*/)|(//.*)'

symbols = ['AT', 'DOLLAR', 'HASH', 'AMPERSAND', 'EQUALS', 'LEFT_PARENTHESIS', 'RIGHT_PARENTHESIS']
non_code = ['WHITESPACE', 'COMMENT']

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

def main(in_file, out_file):
	lex.lex()

	in_data = in_file.read()
	lex.input(in_data)
	while True:
		t = lex.token()
		if not t:
			break

		out_file.write(get_token_str(t) + '\n')

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Invalid number of arguments.'
		sys.exit(0)

	filename = sys.argv[1]
	in_file = open(filename, 'r')
	out_file = open(filename + '.mytkn.txt', 'w')
	
	main(in_file, out_file)

	out_file.close()