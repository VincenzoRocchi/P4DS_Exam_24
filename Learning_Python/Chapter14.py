#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 14:33:27 2022

@author: vincenzorocchi
"""

#%% exercise 14.1

allthings = {"Socrates", "Plato", "Eratosthenes", "Zeus", "Hera", "Athens", "Acropolis", "Cat", "Dog"}
men = {"Socrates", "Plato", "Eratosthenes"}
mortalthings = {"Socrates","Plato","Eratosthenes","Cat","Dog"}

print(men.intersection(mortalthings))

print("Socrates" in men)
print("Socrates"in mortalthings)

print(allthings.difference(mortalthings))

print(mortalthings.difference(men))

#%%

stringset = set("ciao")

fruitset = {"apple", "banana", "mango", "cherry", "durian"}

while len( fruitset ) > 0:
    print( fruitset.pop() )
    
print(fruitset)

#%% in line exercise

one = set("hello")
two = set("pollice")

one.intersection(two)

#%%

set3 = set( [3*x for x in range( 1, int( 1001/3 )+1 )] )
set7 = set( [7*x for x in range( 1, int( 1001/7 )+1 )] )
set11 = set( [11*x for x in range( 1, int( 1001/11 )+1 )] )

seta = set3 & set7 & set11
setb = (set3 & set7) - set11
setc = set( range( 1, 1001 ) ) - set3 - set7 - set11