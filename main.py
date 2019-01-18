#!/usr/bin/env python

import sys
from parser import *
from lexer import *
from error import *

if __name__ == '__main__':

    filename = sys.argv[1]
    text = open(filename).read()

    # Test for invalid use of comment.
    com_num = 0 # store the number of comments
    text = text.replace('\n\n', '\n')
    # Check if the number of /* and */ is the same
    if text.count('/*') != text.count('*/'):
        exit('Comment Error: num of "/*" and "*/" not match.')        
    else:
        # Try to match /* and */ in the program
        while text.find('/*') != -1:
            # If there are lonely */, raise error
            if text.find('*/') == -1:
                exit("Error! Invalid use of comment.")
            com_num  = com_num + 1
            text = text[:text.find('/*')] + text[text.find('*/')+3:]
    # If there are lonely /*, raise error
    if text.find('*/') != -1 or text.find('/*') != -1:
        exit("Error! Invalid use of comment.")

    # tokens = foo_lex(text)

    # print 'Tokens we get:' 
    # for token in tokens:
    #     print token

    text, check_result = error_check(text)

    tokens = foo_lex(text)

    print 'Tokens we get:' 
    for token in tokens:
        print token

    print 'Checking done'
    if check_result == 0:
        exit('Exit because of error detected.')

    print '----------------------------------------'
    print 'Output:'
    parse_result = foo_parse(tokens)
    if not parse_result:
        sys.stderr.write('Parse error!\n')
        sys.exit(1)
    ast = parse_result.value
    env = {}
    c_env = 0;
    ast.eval(env, c_env)
    print '----------------------------------------'

    print 'Final variable values:'
    for name in env:
        sys.stdout.write('%s: %s\n' % (name, env[name]))

    if check_result == 2:
        print '----------------------------------------'
        print 'Detected changed text while compiling, please remember to change the file.'