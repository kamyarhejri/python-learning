# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:32:11 2020

@author: kamyar

creating my own doubly linked list class

"""

class Node():
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
  def __str__(self):
    return str(self.value)
  
class LinkedList():
  def __init__(self, value ):
    #self.head = {'value':value, 'next':None}
    #defining Node class instead of creating a new dictiomnary as
    #a new node every time
    self.head = Node(value)
    self.tail = self.head
    self.length = 1

  def append(self, value):
    #newnode = {'value':value, 'next':None}
    newnode = Node(value)
    newnode.prev = self.tail
    self.tail.next = newnode
    self.tail = newnode
    self.length += 1

  def prepend(self, value):
    #newnode = {"value": value , 'next': None}
    newnode = Node(value)
    self.head.prev = newnode
    newnode.next = self.head
    self.head = newnode
    self.length += 1
  
  def printlinkedlist(self):
    currentnode = self.head
    while(currentnode != None):
      print(currentnode.value, ' --> ', end=' ')
      currentnode = currentnode.next
    print('None', end=' ')

  def insert(self, index, value):
    if index >= self.length:
      self.append(value)
      self.length += 1
    elif index == 0:
      self.prepend(value)
      self.length += 1
    else:
      counter = 0
      prenode = self.head
      while(counter < index-1):
        prenode = prenode.next
        counter += 1
      afternode = prenode.next
      newnode = Node(value)
      newnode.prev = prenode
      prenode.next = newnode
      newnode.next = afternode
      afternode.prev = newnode
      self.length += 1

          

  
mylist = LinkedList(10)
mylist.append(5)
mylist.append(16)
mylist.prepend(1)
mylist.insert(2,23)
mylist.printlinkedlist()

