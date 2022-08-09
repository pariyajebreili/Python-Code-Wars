# https://www.codewars.com/kata/52e864d1ffb6ac25db00017f/train/python

'''
Construct a function that, when given a string containing an expression in infix notation, will return an identical expression in postfix notation.

The operators used will be +, -, *, /, and ^ with left-associativity of all operators but ^.

The precedence of the operators (most important to least) are : 1) parentheses, 2) exponentiation, 3) times/divide, 4) plus/minus.

The operands will be single-digit integers between 0 and 9, inclusive.

Parentheses may be included in the input, and are guaranteed to be in correct pairs.

to_postfix("2+7*5") # Should return "275*+"
to_postfix("3*3/(7+1)") # Should return "33*71+/"
to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
to_postfix("1^2^3") # Should return "123^^"
'''

LEFT  = lambda a,b: a>=b
RIGHT = lambda a,b: a>b
PREC  = {'+': 2, '-': 2, '*': 3, '/': 3, '^': 4, '(': 1, ')': 1}

OP_ASSOCIATION = {'+': LEFT, '-': LEFT, '*': LEFT, '/': LEFT, '^': RIGHT}


def to_postfix (infix):
    stack, output = [], []
    for c in infix:
        prec = PREC.get(c)
        
        if prec is None: output.append(c)
        elif c == '(':   stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append( stack.pop() )
            stack.pop()
        else:
            while stack and OP_ASSOCIATION[c](PREC[stack[-1]], prec):
                output.append( stack.pop() )
            stack.append(c)
            
    return ''.join(output + stack[::-1])