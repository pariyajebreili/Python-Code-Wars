# https://www.codewars.com/kata/59f7597716049833200001eb/train/python
'''
Consider the numbers 6969 and 9116. When you rotate them 180 degrees (upside down), these numbers remain the same. To clarify, if we write them down on a paper and turn the paper upside down, the numbers will be the same. Try it and see! Some numbers such as 2 or 5 don't yield numbers when rotated.

Given a range, return the count of upside down numbers within that range. For example, solve(0,10) = 3, because there are only 3 upside down numbers >= 0 and < 10. They are 0, 1, 8.
'''
# 1
def solve(a, b):
    count = 0
    none_rotatable = {"2","3","4","5","7"}
    for i in range(a,b):
        if (set(str(i)).issubset(none_rotatable)): continue
        else:
            count+=1 if str(i) == str(i)[::-1].translate(str.maketrans('2345679', 'XXXX9X6')) else 0
    return count



# 2
def solve(a, b):
    return sum(str(n) == str(n)[::-1].translate(str.maketrans('2345679', 'XXXX9X6')) for n in range(a, b))



# 3
def solve(a, b):
    count = 0
    rotatable = {"0","1","6","8","9"}
    for x in range(a,b):
        x = str(x)
        if not set(x).issubset(rotatable): continue
        rot_x = x[::-1].replace("6","-").replace("9","6").replace("-","9")
        if rot_x == x: count += 1
    return count
