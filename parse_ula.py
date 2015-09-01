import ply.yacc as yacc
import lex_ula
import sys

lex_tokens = lex_ula.tokens
tokens = [t for t in lex_ula.tokens if t not in lex_ula.non_code]

def p_program(p):
	'''program	: statement
				| program statement'''

def p_statement(p):
	'''statement	: ID EQUALS expression'''

def p_expression(p):
	'''expression	: expression AT term
					| expression DOLLAR term
					| term'''

def p_term(p):
	'''term	: term HASH factor
			| term AMPERSAND factor
			| factor'''

def p_factor(p):
	'''factor	: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS
				| FLOAT_LITERAL
				| ID'''

def p_error(p):
	print('Syntax error at: %s' % p.value)



def main(in_file, out_file):
	yacc.yacc()

	in_data = in_file.read()
	out = yacc.parse(in_data)
	print(out)


if __name__ == '__main__':
	filename = sys.argv[1]
	in_file = open(filename, 'r')

	filename_prefix = filename[:filename.index('.')]
	out_file = open(filename_prefix + '.myast.txt', 'w')
	
	main(in_file, out_file)

	out_file.close()