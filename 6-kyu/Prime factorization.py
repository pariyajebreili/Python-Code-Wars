# https://www.codewars.com/kata/534a0c100d03ad9772000539/train/python

'''
The prime factorization of a positive integer is a list of the integer's prime factors, together with their multiplicities; the process of determining these factors is called integer factorization. The fundamental theorem of arithmetic says that every positive integer has a single unique prime factorization.

The prime factorization of 24, for instance, is (2^3) * (3^1).

Write a class called PrimeFactorizer (inheriting directly from object) whose constructor accepts exactly 1 int and has a property factor containing a dictionary where the keys are prime numbers and the values are the multiplicities.

PrimeFactorizer(24).factor #should return { 2: 3, 3: 1 }

'''

class PrimeFactorizer:

    def __init__(self, num):
        self.factor = {}
        for i in range(2, num + 1):
            if (num < i):
                break
            while(num % i == 0):
                num /= i
                self.factor[i] = self.factor.get(i, 0) + 1


