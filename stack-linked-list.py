# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 18:21:03 2020

@author: kamyar

Implementation of stack in python using linked lists
"""

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack():
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0
  
  def peek(self):
    if self.IsEmpty():
      return None
    else:
      return self.top
  
  def pop(self):
    if self.IsEmpty():
      print("Stack is empty!")
    else:
      if self.length == 1:
        self.bottom = None
      self.top = self.top.next
      self.length -= 1
      
  def push(self, value):
    newnode = Node(value)
    if self.IsEmpty():
      self.bottom = newnode
      self.top = newnode
    else:
      last = self.peek()
      self.top = newnode
      self.top.next = last
    self.length += 1

  def printstack(self):
    currentnode = self.top
    while(currentnode != None):
      print(currentnode.value, ' --> ', end=' ')
      currentnode = currentnode.next
    print('None\n', end='')

  def IsEmpty(self):
    if self.length == 0:
      return True
    else:
      return False




mystack = Stack()
print(mystack.IsEmpty())
mystack.push(23)
mystack.push(6)
mystack.push(7)
mystack.push(95)
print(mystack.IsEmpty())
print(mystack.peek().value)
mystack.printstack()
mystack.pop()
mystack.pop()
mystack.printstack()
mystack.push(105)
mystack.printstack()