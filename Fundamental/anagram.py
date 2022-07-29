# https://www.codewars.com/kata/523a86aa4230ebb5420001e1/train/python

# 1
def check(s1, s2):
	if(sorted(s1)== sorted(s2)):
		return s2


def anagrams(word, words):
      result = []
      for i in words:
            if(check(word, i)==i):
                  result.append(i)
      return result


# 2

def anagrams(word, words): return [item for item in words if sorted(item)==sorted(word)]

