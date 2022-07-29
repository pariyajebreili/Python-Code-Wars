# https://www.codewars.com/kata/57eadb7ecd143f4c9c0000a3/train/python


def abbrev_name(name):
    name = name.split(" ")
    first = name[0][0]
    second = name[1][0]
    first = (str(first).capitalize())
    second = (str(second).capitalize())
    return first + "." + second 


def abbrevName(name):
    return '.'.join(w[0] for w in name.split()).upper()