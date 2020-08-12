# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:03:36 2020

@author: kamyar
"""

def primecheck(x):
  result = True
  for i in range(x-1, 1, -1):
    if x%i == 0:
      result = False
      return result
      break
  return result

def primefinder(y):
  l = []
  for i in range(y-1, 1, -1):
    if primecheck(i):
      l.append(i)
  return l

def goldbachfinder(z):
  if z > 2:
    l = primefinder(z)
    print(l)
    r = [(x,y) for x in l for y in l if (x+y == z and x != y)]
    return r
  else:
    return 0


r = goldbachfinder(20)
print(r)