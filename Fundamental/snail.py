# https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python


# 1
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] 
    return out


# 2

def snail(array):
    res = []
    while len(array) > 1:
        res = res + array.pop(0)
        res = res + [row.pop(-1) for row in array]
        res = res + list(reversed(array.pop(-1)))
        res = res + [row.pop(0) for row in array[::-1]]
    return res if not array else res + array[0]

