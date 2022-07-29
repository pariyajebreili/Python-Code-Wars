# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

# 1
def xo(s):
    s = s.upper()
    xs = sum(1 for x in s if x == 'X')
    os = sum(1 for o in s if o == 'O')
    if xs == os:
      return True
    else:
      return False



# 2
def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')




# 3
from collections import Counter

def xo(s):
    d = Counter(s.lower())
    return d.get('x', 0) == d.get('o', 0) 
# 0 in get is a default value