# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:04:35 2020

@author: kamyar
"""

A = ['a','b','c','x']
B = ['z', 'y', 'o']

def matchfinder(l1 : list, l2: list):
  d = {}
  res = False
  for i,v in enumerate(l1):
    if v in d:
      res = True
      break
    else:
      d[v] = i
  print(d)
  
  for i,v in enumerate(l2):
    if v in d:
      res = True
      break
    else:
      d[v] = i
  print(d)
  return res

a = matchfinder(A,B)
print(a)