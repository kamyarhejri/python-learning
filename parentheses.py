# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 12:34:23 2020

@author: kamyar

coding exercise: given any string input including parentheses in it, check if 
the parentheses are balanced. That means for each '(' in the string, there will 
be a ')' to their left.

I used python 3 to solve this problem
"""

def balanced(s):
    b = 0
    i = 0
    while (i < len(s)):
        if b>=0:
            if s[i] == "(":
                b += 1
                i += 1
            elif s[i] == ")":
                b -= 1
                i += 1
            else:
                i += 1
        else:
            return False
        
    if b == 0:
        return True
    else:
        return False

print(balanced("(b)as(()"))
            
            
    