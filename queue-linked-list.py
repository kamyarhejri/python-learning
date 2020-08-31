# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 13:46:00 2020

@author: kamyar

Implementation of Queues in Python using Linked Lists
"""

class Node():
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue():
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def peek(self):
    if self.IsEmpty():
      return None
    else:
      return self.first
      
  def dequeue(self):
    if self.IsEmpty():
      print("Stack is empty!")
    else:
      if self.length == 1:
        self.last = None
      self.first = self.first.next
      self.length -= 1

  def enqueue(self, value):
    newnode = Node(value)
    if self.IsEmpty():
      self.first = newnode
      self.last = newnode
    else:
      self.last.next = newnode
      self.last = newnode
    self.length += 1

  def printqueue(self):
    currentnode = self.first
    while currentnode != None:
      print(currentnode.value, ' --> ', end=' ')
      currentnode = currentnode.next
    print('None\n', end='')

  def IsEmpty(self):
    if self.length == 0:
      return True
    else:
      return False




myqueue = Queue()
myqueue.enqueue('Amir')
myqueue.enqueue('Ali')
myqueue.enqueue('Nima')
myqueue.enqueue('Kamyar')
myqueue.enqueue('Negin')
myqueue.enqueue('Joe')
myqueue.printqueue()
print(myqueue.peek().value)
myqueue.dequeue()
myqueue.dequeue()
myqueue.printqueue()
myqueue.enqueue('Jim')
myqueue.printqueue()
myqueue.dequeue()
myqueue.printqueue()
