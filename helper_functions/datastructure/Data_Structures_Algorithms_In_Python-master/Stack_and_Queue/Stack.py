#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:43:29 2019

@author: petern
"""

from sys import maxsize 
  
# Function to create a stack. It initializes size of stack as 0 
def createStack(): 
    stack = [] 
    return stack 
  
# Stack is empty when stack size is 0 
def isEmpty(stack): 
    return len(stack) == 0
  
# Function to add an item to stack. It increases size by 1 
def push(stack, item): 
    stack.append(item) 
    print(item + " pushed to stack ") 
      
# Function to remove an item from stack. It decreases size by 1 
def pop(stack): 
    if (isEmpty(stack)): 
        return str(-maxsize -1) #return minus infinite 
      
    return stack.pop() 
        
# Python program for linked list implementation of stack 
  
# Class to represent a node 
class StackNode: 
  
    # Constructor to initialize a node 
    def __init__(self, data): 
        self.data = data  
        self.next = None
  
class Stack: 
      
    # Constructor to initialize the root of linked list 
    def __init__(self): 
        self.root = None
  
    def isEmpty(self): 
        return True if self.root is None else  False 
  
    def push(self, data): 
        newNode = StackNode(data) 
        newNode.next = self.root  
        self.root = newNode 
        print ("%d pushed to stack" %(data) )
      
    def pop(self): 
        if (self.isEmpty()): 
            return float("-inf") 
        temp = self.root  
        self.root = self.root.next 
        popped = temp.data 
        return popped 
      
    def peek(self): 
        if self.isEmpty(): 
            return float("-inf") 
        return self.root.data

if __name__ == "__main__":
    # Driver program to test above class
    stack = createStack()
    push(stack, str(10))
    push(stack, str(20))
    push(stack, str(30))
    print(pop(stack) + " popped from stack")

    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print ("%d popped from stack" %(stack.pop()) )
    print ("Top element is %d " %(stack.peek()) )
