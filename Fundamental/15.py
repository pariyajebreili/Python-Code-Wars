# https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

# 1
def is_triangle(a, b, c):
     if(a<0 or b<0 or c<0):
        return False
     else:
            if(a+b>c and a+c>b and b+c>a):
                  return True
            else:
                  return False


# 2
def is_triangle(a, b, c):
    return (a<b+c) and (b<a+c) and (c<a+b)


# 3
def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c