# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python

'''
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

# 1
def solution(string, markers):
    newstring = string.split('\n')
    for i in range(len(newstring)):
        part = newstring[i]
        for marker in markers:
            index = part.find(marker)
            if index >= 0:
                part = part[:index].rstrip()
        newstring[i] = part
    return '\n'.join(newstring)



# 2
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)