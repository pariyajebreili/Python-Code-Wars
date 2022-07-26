# https://www.codewars.com/kata/59474c656ff02b21e20000fc/train/python

'''
This is the second Kata in the Ciphers series. This series is meant to test our coding knowledge.

Ciphers #2 - The reversed Cipher
This is a lame method I use to write things such that my friends don't understand. It's still fairly readable if you think about it.

How this cipher works
First, you need to reverse the string. Then, the last character in the original string (the first character in the reversed string) needs to be moved to the back. Words will be separated by spaces, and punctuation marks can be counted as part of the word.

Example
encode("Hello World!"); // => "lleHo dlroW!"
This is because "Hello" reversed is "olleH" and "o" is moved to the back, and so on. The exclamation mark is considered to be part of the word "World".

'''

# 1
def encode(s):
    return ' '.join(i[-2::-1] + i[-1] for i in s.split())