#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 09:28:52 2023

@author: vincenzorocchi
"""

# =============================================================================
# Exercise 2. The built-in zip function "zips" two lists. Define a function named zap with 
# your own implementation of this function. The function takes two lists as input, 
# a and b, and returns a list of tuples. Each tuple should contain one item x from 
# the a list and one item y from b, with x and y being in the same position in their 
# list. You may assume a and b have equal lengths. Test your function on two input lists. 
# =============================================================================
from random import randint, seed

l1= []
l2= []

i = 0
seed(10)
while i < 5:
    l1.append(randint(1,100)) #creating a random list to simulate user input 
    i += 1
    
i = 0
seed(11)
while i < 5:
    l2.append(randint(1,100)) #creating a random list to simulate user input 
    i += 1
print(l1,l2)

def zap(a,b):
    l3 = []
    for i in range(len(a)):
        tuple = (a[i],b[i])
        l3.append(tuple)
    return l3
    
print(zap(l1,l2))


    
    