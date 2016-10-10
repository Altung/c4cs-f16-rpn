#!/usr/bin/env python3

import operator

operator = {
	'+':operator.add,
	'-':operator.sub,
	'*':operator.mul,
	'/':operator.truediv,
	'^':operator.pow
}

def calculate(myarg1):
	stack = list()
	for token in myarg1.split(' '):
		if token in ['-', '+', '*', '/', '^']:
			stack.append(int(token))
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = operator[token]
			result - function(arg1, arg2)
			stack.append(result)
        else:
            try:
                stack.append(float(token))
            except:
            	raise TypeError
 
    return stack.pop()

def main():
	while True:
		calculate(input("rpn calc> "))

if __name__ == '__main__': 
    main()