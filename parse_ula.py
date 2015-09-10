import ply.yacc as yacc
import lex_ula
import sys

tokens = [t for t in lex_ula.tokens if t not in lex_ula.non_code]

def p_program_recursive(p):
	'''program	: program statement'''
	p[0] = p[1] + (p[2],)

def p_program_terminal(p):
	'''program	: statement'''
	p[0] = ("Program", p[1])

def p_statement_assignment(p):
	'''statement	: ID EQUALS expression'''
	p[0] = ("AssignStatement", ("ID," + p[1],), p[3])

def p_expression_add(p):
	'''expression	: expression AT term'''
	p[0] = ("AddExpression", p[1], p[3])

def p_expression_sub(p):
	'''expression	: expression DOLLAR term'''
	p[0] = ("SubExpression", p[1], p[3])

def p_expression_term(p):
	'''expression	: term'''
	p[0] = p[1]

def p_term_mul(p):
	'''term	: term HASH factor'''
	p[0] = ("MulExpression", p[1], p[3])

def p_term_div(p):
	'''term	: term AMPERSAND factor'''
	p[0] = ("DivExpression", p[1], p[3])

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



yacc.yacc()

def print_tree(tree, tabs, out_file):
	for subtree in tree:
		if isinstance(subtree, str):
			out_file.write(tabs + subtree + '\n')
		else:
			print_tree(subtree, tabs + '\t', out_file)


def main(in_file, out_file):
	
	in_data = in_file.read()
	out = yacc.parse(in_data)

	print('Start')
	print_tree(out, '\t', sys.stdout)

	out_file.write('Start\n')
	print_tree(out, '\t', out_file)


if __name__ == '__main__':
	filename = sys.argv[1]
	in_file = open(filename, 'r')

	filename_prefix = filename[:filename.rfind('.')]
	out_file = open(filename_prefix + '.ast', 'w')
	
	main(in_file, out_file)

	out_file.close()