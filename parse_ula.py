import ply.yacc as yacc
import lex_ula
import sys

lex_tokens = lex_ula.tokens
tokens = [t for t in lex_ula.tokens if t not in lex_ula.non_code]

def p_program_recursive(p):
	'''program	: program statement'''
	p[0] = p[1] + (p[2],)

def p_program_terminal(p):
	'''program	: statement'''
	p[0] = ("Program", p[1])

def p_statement_assignment(p):
	'''statement	: ID EQUALS expression'''
	p[0] = ("AssignStatement", (("ID," + p[1],), p[3]))

def p_expression_add(p):
	'''expression	: expression AT term'''
	p[0] = ("AddExpression", (p[1], p[3]))

def p_expression_sub(p):
	'''expression	: expression DOLLAR term'''
	p[0] = ("SubExpression", (p[1], p[3]))

def p_expression_term(p):
	'''expression	: term'''
	p[0] = p[1]

def p_term_mul(p):
	'''term	: term HASH factor'''
	p[0] = ("MulExpression", (p[1], p[3]))

def p_term_div(p):
	'''term	: term AMPERSAND factor'''
	p[0] = ("DivExpression", (p[1], p[3]))

def p_term(p):
	'''term	: factor'''
	p[0] = p[1]

def p_factor_brackets(p):
	'''factor	: LEFT_PARENTHESIS expression RIGHT_PARENTHESIS'''
	p[0] = p[2]

def p_factor_float(p):
	'''factor	: FLOAT_LITERAL'''
	p[0] = ("FloatExpression", ("FLOAT_LITERAL,"+p[1], ))

def p_factor_id(p):
	'''factor	: ID'''
	p[0] = ("IdentifierExpression", ("ID," + p[1],))

def p_error(p):
	print('Syntax error at: %s' % p.value)



def print_tree(tree, tabs):
	for subtree in tree:
		if isinstance(subtree, str):
			print(tabs + subtree)
		else:
			print_tree(subtree, tabs + '   ')


def main(in_file, out_file):
	yacc.yacc()

	in_data = in_file.read()
	out = yacc.parse(in_data)
	print(out , '\n\n')
	print_tree(out, '')


if __name__ == '__main__':
	filename = sys.argv[1]
	in_file = open(filename, 'r')

	filename_prefix = filename[:filename.index('.')]
	out_file = open(filename_prefix + '.myast.txt', 'w')
	
	main(in_file, out_file)

	out_file.close()