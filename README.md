##Compilers: Assignment 1: Lexical analyser and parser

**Author** : Muhummad Yunus Patel  
**Student#** : PTLMUH006  
**Date**  : 18-September-2015

###Description:
 This assignment required the creation of lexical and syntactic analyser modules for a made up language called ula (***U***nconventional ***La***nguage). The lexer and parser modules were written in python and made use of the PLY library (python wrapper for Lex and Yacc).

 The lexer tokenises the input program and passes the token stream to the parser. The parser then analyses the token stream to ensure that it conforms to the grammar describing the ula language. Any errors in either of these stages will cause the compilation process to stop and a suitable message to be displayed. The lexer and parser together make up the front-end of the compiler for the ula language.

###Usage:
 * See assignment spec pdf for usage instructions.
 * Ula sample programs provided as part of this repository.