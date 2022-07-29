# https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python


def get_sum(a,b):
      if a == b:
            return a
      if a < b:
            return sum(x for x in range(a,b+1))
      if a > b:
            return sum(x for x in range(b,a+1))

print(get_sum(0,-1))