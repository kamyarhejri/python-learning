# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 13:38:15 2020

@author: kamyar

Implementation of Factorial function using Recursion and Iteration
"""
# factorial using recursion
def factorial_rec(n):
  if n == 1:
    return n
  else:
    return (n*factorial_rec(n-1))
  
print('recursion:',factorial_rec(10))

# factorial using iteration
def factorial_iter(n):
  answer = 1
  for i in range(n,0,-1):
    answer = i*answer
  return answer

print('iteration:', factorial_iter(10))