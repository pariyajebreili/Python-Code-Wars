# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
'''
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
'''


# 1
def valid_parentheses(string):    
    count = 0
    string = ''.join(c for c in string if c=='(' or c== ')')
    for i in range(len(string)):
        if string[i] == "(":
            count += 1
        elif string[i] == ")":
            count -= 1
        if count < 0:
            return False
    return count == 0




# 2
def valid_parentheses(string):
    string = "".join(ch for ch in string if ch in "()")
    while "()" in string: string = string.replace("()", "")
    return not string


# valid_parentheses("((())()())")