# https://www.codewars.com/kata/5711fc7c159cde6ac70003e2/train/python

'''
You are given an array of positive and negative integers and a number n and n > 1. The array may have elements that occurs more than once. Find all the combinations of n elements of the array that their sum are 0.

arr = [1, -1, 2, 3, -2]
n = 3
find_zero_sum_groups(arr, n) == [-2, -1, 3] # -2 - 1 + 3 = 0
The function should ouput every combination or group in increasing order.

We may have more than one group:

arr = [1, -1, 2, 3, -2, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]
In the case above the function should output a sorted 2D array.

The function will not give a group twice, or more, only once.

arr = [1, -1, 2, 3, -2, 4, 5, -3, -3, -1, 2, 1, 4, 5, -3 ]
n = 3
find_zero_sum_groups(arr, n) == [[-3, -2, 5], [-3, -1, 4], [-3, 1, 2], [-2, -1, 3]]
If there are no combinations with sum equals to 0, the function will output an alerting message.

arr = [1, 1, 2, 3]
n = 2
find_zero_sum_groups(arr, n) == "No combinations"
If the function receives an empty array will output an specific alert:

arr = []
n = 2
find_zero_sum_groups(arr, n) == "No elements to combine"

'''


# 1

from itertools import combinations
def find_zero_sum_groups(arr, n):
    combos = sorted(sorted(c) for c in combinations(set(arr), n) if sum(c) == 0)
    return combos if len(combos) > 1 else combos[0] if combos else "No combinations" if arr else "No elements to combine"














# from itertools import combinations
# from operator import itemgetter

# def find_zero_sum_groups(arr, n):
#         l = []
#         if arr == [] :
#                 return "No elements to combine"
#         else:
#                 for i in combinations(arr,n):
#                         for j in i:
#                                 if i.count(j) > 1:
#                                         break
#                                 else:
#                                         i=list(sorted(i))           
#                                         if sum(x for x in i) == 0:
#                                                 if i in l:
#                                                         pass
#                                                 else:
#                                                         l.append(i)
#                 if l == []:
#                         return "No combinations"
#                 else:     
#                         return (sorted(l, key=itemgetter(0)))

