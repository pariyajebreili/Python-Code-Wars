# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python
'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.

'''

# 1
def get_count(sentence):
    return(sentence.count('a'))+sentence.count('e')+sentence.count('i')+sentence.count('o')+sentence.count('u')+sentence.count('A')+sentence.count('E')+sentence.count('I')+sentence.count('O')+sentence.count('U')


# 2
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")