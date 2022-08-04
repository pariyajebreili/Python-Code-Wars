# https://www.codewars.com/kata/52774a314c2333f0a7000688/train/python
'''

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