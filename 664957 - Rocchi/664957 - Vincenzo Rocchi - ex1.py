#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:04:31 2023

@author: vincenzorocchi
"""

# =============================================================================
# Exercise 1. Define a Python function orderAlt(l) that takes as input a list l1 of integers, 
# and return as output a new list l2 such that: i) the first portion of l2 contains 
# the even numbers of l1, in ascending order; ii) the second portion of l2 contains 
# the odd numbers of l1, in descending order. Test your function on an input list. 
# =============================================================================


# =============================================================================
# Bonus: the user inputs the list l1 from the terminal (use -1 as termination character of 
# the endless insertion loop). 
# =============================================================================
from random import randint, seed
from pcinput import getInteger

def IsEven(n):
    return n %2 == 0

seed(10)
i = 0
l1 = []

while i < 10:
    l1.append(randint(1,100)) #creating a random list to simulate user input 
    i += 1

# bonus
# print("You can write the number of integers u want to start the program just enter \"-1\"")

while i <1000:
    i = getInteger("Write integers here:") 
    if i != -1:
        l1.append(i)
        continue
    else:
        break
# end of bonus
        
def orderAlt(l):
    even = sorted([x for x in l1 if IsEven(x) == True])
    odd = sorted([x for x in l1 if IsEven(x) != True], reverse = True)
    return even + odd

print(orderAlt(l1))

