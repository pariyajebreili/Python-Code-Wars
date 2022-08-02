# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python
'''
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

'''

import string

# 1
def is_pangram(s):
    b = set()
    a = string.ascii_lowercase[:26]
    a = list(a)
    for i in s:
        if i.isalpha():
            b.add(i.lower())
    b = sorted(list(b))
    return a == b


# 2
def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


# 3
def is_pangram(s):
    return set(string.ascii_lowercase).issubset(s.lower())