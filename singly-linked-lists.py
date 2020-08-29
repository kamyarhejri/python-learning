# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 11:55:07 2020

@author: kamyar

making my own signly linked list class
"""

class Node():
  def __init__(self, value):
    self.value = value
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
    self.tail.next = newnode
    self.tail = newnode
    self.length += 1

  def prepend(self, value):
    #newnode = {"value": value , 'next': None}
    newnode = Node(value)
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
      prenode.next = newnode
      newnode.next = afternode
      self.length += 1

  def remove(self, index):
    if index == 0:
      self.head = self.head.next
      self.length -= 1
    elif index > self.length:
      print("\n\nIndex out of Range!")
    else:
      prenode = self.head
      counter = 0
      while(counter < index-1):
        prenode = prenode.next
        counter += 1
      afternode = prenode.next
      prenode.next = afternode.next
      self.length -= 1

  def reverse(self):
      if (self.length == 1):
          return self.head
      else:
          revlist = LinkedList(self.head.value)
          for i in range(0, self.length, 1):
              if self.head.next != None:
                  self.head = self.head.next
                  revlist.prepend(self.head.value)        
              else:
                  break
          self.head = revlist.head

          

          

  
mylist = LinkedList(10)
print('')
mylist.printlinkedlist()
mylist.append(5)
print('')
mylist.printlinkedlist()
mylist.append(16)
print('')
mylist.printlinkedlist()
mylist.prepend(1)
print('')
mylist.printlinkedlist()
mylist.insert(3,93)
print('')
mylist.printlinkedlist()
mylist.insert(2,88)
print('')
mylist.printlinkedlist()
print('\n\nItem removed')
mylist.remove(4)
print(' ')
mylist.printlinkedlist()
print(' \n')
mylist.reverse()
print('Reversed list:\n')
mylist.printlinkedlist()