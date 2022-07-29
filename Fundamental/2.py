# https://www.codewars.com/kata/551b4501ac0447318f0009cd/train/python

def boolean_to_string1(b):
    return str(b)

def boolean_to_string2(b):
    return ('False', 'True')[b]
    
print(boolean_to_string2(bool(1)))