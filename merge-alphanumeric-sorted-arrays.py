# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:30:26 2020

@author: kamyar

Implementation of a function in python 3 which can merge two sorted alphanumeric arrays
and return a sorted alphanumeric array

Note:
this script should receive inputs from user in commandline
run this script from cmd to see the result

Sample input:
H,L,M,P,P,R,S,b,d,i,n,o,o,p,s;1,5,5,6,7,8,C,U,V,V,W,f,h,r,s
which should be processed as:
#array1 = ['H','L','M','P','P','R','S','b','d','i','n','o','o','p','s']
#array2 = [1,5,5,6,7,8,'C','U','V','V','W','f','h','r','s']

"""
import sys
    
def mergesort(x,y):
  result = []
  pairs = []
  i = 0
  j = 0
 
  if len(x) == 0 and len(y) == 0:
      print("invalid inputs!")
      return []
  elif len(x) == 0:
      return y
  elif len(y) == 0:
      return x
  else:
      while i<len(x) and j<len(y):
          #check if both elements are integers
          try:
              if int(x[i]) < int(y[j]):
                  result.append(x[i])
                  pairs.append((x[i],y[j]))
                  i+=1
              elif int(x[i]) >= int(y[j]):
                  result.append(y[j])
                  pairs.append((y[j],x[i]))
                  j+=1
          #else:        
          except:
              if x[i] < y[j]:
                  result.append(x[i])
                  pairs.append((x[i],y[j]))
                  i+=1
              else:
                  result.append(y[j])
                  pairs.append((y[j],x[i]))
                  j+=1
      while i<len(x):
          result.append(x[i])
          pairs.append((y[j-1],x[i]))
          i+=1
      while j<len(y):
          result.append(y[j])
          pairs.append((x[i-1],y[j]))
          j+=1     
  return result, pairs


for line in sys.stdin:
    if line.rstrip() == 'q':
        break
    try:
        s1,s2 = [i for i in (str(line.rstrip())).split(';')]
        a = [j for j in s1.split(',')]
        b = [k for k in s2.split(',')]
    except:
        print('invalid input!')
    if a != [] and b != []:
        print(a)
        print(b)
        r, p = mergesort(a,b)
        print(r)
        print(p)
        a.clear()
        b.clear()
    else:
        continue



