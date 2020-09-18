# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:14:28 2020

@author: kamyar

finding the largest palindrome that is made from the product of two n-digit numbers
"""
import time
    
def LargestPal(n : int):
# assume we find two n digit numbers and their product is a palindrome:
# first  = 10^n - x
# second = 10^n - y
# palindrome = first * second -> palindrome = 10^2n - (y*10^n) - (x*10^n) + xy
# palindrome = 10^2n - (x+y)*10^n + xy -> palindrome = 10^n*(10^n - (x+y)) + xy
# palindrome = 10^n*(left) + right
# left = 10^n - (x+y)
# right = xy
# example: palindrome = ABCCBA -> ABCCBA = 10^6*(ABC) + CBA = ABC000 + CBA = ABCCBA
# left = 10^6 - (x+y) = ABC
# right = xy = CBA
# assume z = x+y, we keep z as low as possible to find the largest palindrome
# for largest palindrome made from the product of 2 7-digit numbers:
# z = x + y
# left = 10^7 - z
# right = xy = x(z-x) = -x^2 + xz -> x^2 - zx + right = 0
# now we have left, right, and one quadratic equation of x that can be easily
# solved using Math
# and always making sure that right is the same as backward of left (check example)
# in python 3 we check the above statement like this:   
# right = int(str(left[::-1]))
# left write the code in python 3 to understand better
  start_time = time.time()
  for z in range(2, 2*(9*10**(n-1)) - 1, 1):
    left = 10**n - z
    right = int(str(left)[::-1])
    
    # our quadratic equation -> x^2 - zx + right = 0
    # lets see if it has roots:
    # if b^2 - 4ac < 0, there are no roots for ax^2 + bx + c = 0
    root1 = 0 
    root2 = 0
    
    if (z**2)-(4*right) < 0:
        #no roots
        #lets increase z
        continue    
    else:
        #we have at least one root
        # if (z**2)-(4*right) = 0, we have one root
        # if (z**2)-(4*right) > 0, we have two roots
        # roots = (-b +- (b^2 - 4ac)^1/2)/2a
        root1 = (z + ((z**2)-(4*right))**0.5)/2
        root2 = (z - ((z**2)-(4*right))**0.5)/2
        # if one root (x) is integer, we can guarantee that y is also integer
        # because z is integer and z = x + y
        if root1.is_integer() or root2.is_integer():         
            result = []
            # palindrome = 10^n*(left) + right
            p = (10**n)*left + right
            # first  = 10^n - x
            first = 10**n - root1
            # second = 10^n - y -> second = 10^n - z + x 
            second = 10**n - z + root1
            result.append(p)
            result.append(first)
            result.append(second)
            print('My program took {} to run'.format(time.time() - start_time))
            return result
                
print(LargestPal(7))
