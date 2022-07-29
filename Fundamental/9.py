# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

from gettext import find


def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i

seq = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
print(find_it(seq))