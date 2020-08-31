# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 20:48:16 2020

@author: kamyar

Implementation of Stack in python using Arrays
"""

class Stack():
  def __init__(self):
    self.arr =[]

  def peek(self):
    if self.IsEmpty():
      return None
    else:
      return self.arr[len(self.arr) - 1]
  
  def pop(self):
    if self.IsEmpty():
      print("Stack is empty!")
    else:
      self.arr.pop()
      
  def push(self, value):
    self.arr.append(value)

  def printstack(self):
    for i in range(len(self.arr)-1,-1,-1):
      print(self.arr[i], ' <-- ', end=' ')
    print('None\n', end='')

  def IsEmpty(self):
    if len(self.arr) == 0:
      return True
    else:
      return False




mystack = Stack()
mystack.push('google')
mystack.push('LinkedIn')
mystack.push('Udemy')
mystack.push('Spotify')
print(mystack.IsEmpty())
print(mystack.peek())
mystack.printstack()
mystack.pop()
mystack.pop()
mystack.printstack()
mystack.push("Repl.it")
mystack.printstack()