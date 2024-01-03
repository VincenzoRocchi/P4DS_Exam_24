#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 23:13:20 2022

@author: vincenzorocchi
"""

#%% in line ex tests

# =============================================================================
# Exercise Write a for loop that displays all the values of the elements of a 
# tuple, and also displays their index.
# =============================================================================

data = ("hello", "world", "hi", "cunt")

for i in range(len(data)):
    print( "[{}:{}]".format(data[i],i), end = " " )

i = 0  
while i < len(data):
    print( "[{}:{}]".format(data[i],i), end = " " )
    i +=1
    
#%% exercise 11.1

# =============================================================================
# A complex number is a number of the form a + bi, whereby a and b are constants,
# and i is a special value that is defined as the square root
#  of -1. Of course, you never try to actually calculate what the square 
#  root of -1 is, as that gives a runtime error; in complex numbers, you 
#  always let the i remain. For instance, the complex number 3 + 2i cannot 
#  be simplified any further. Addition of two complex numbers a + bi and 
#  c + di is defined as (a + c) + (b + d)i. Represent a complex number as 
#  a tuple of two numeric values, and create a function that calculates 
#  the addition of two complex numbers.8
# =============================================================================

x = (3,2,"i")
y = (4,15,"i")

def complex_sum(x,y):
        split1 = (int(x[0]) + int(y[0]))
        split2 = (int(x[1]) + int(y[1]))
        return "{} + {}{}".format(split1,split2,x[2])
    
complex_sum(x,y)

#%%exercise 11.2

# =============================================================================
# Multiplication of two complex numbers a + bi and c + di is defined as
#  (a*c - b*d) + (a*d + b*c)i. Write a function that calculates the multiplication 
#  of two complex numbers.
# =============================================================================

x = (3,2,"i")
y = (4,15,"i") 

def complex_mult(x,y):
    split1 = (int(x[0]) * int(y[0]) )
    split2 = (int(x[1]) * int(y[1]) )
    
    if x[2] == y[2]:
        x = str(x[2])
        return "{}+{}{}".format(split1,split2,x)
        
    if x[2] != y[2]:
        xy = str(x[2]) + str(y[2])
        return "{}+{}{}".format(split1,split2,xy)
    
complex_mult(x, y)

#%%exercise 11.3

# =============================================================================
# Consider the definition of a new datatype. The new datatype is the inttuple.
#  An inttuple is defined as being either an integer, or a tuple consisting 
#  of inttuples. You see an example of an inttuple in the code block below. 
#  Write a func- tion that prints all the integer values stored in an inttuple. 
#  Hint: Since the inttuple is defined recursively, a recursive function is 
#  probably the right approach. If you skipped Chapter 9, you probably should 
#  skip this exercise too. Use the isinstance() function (ex- plained in 
# Chapter 8) to determine whether you are dealing with an integer or a tuple.
#  If you do this correctly, for the inttuple given below, the function will 
#  print the numbers 1 to 20 sequentially.
# =============================================================================

inttuple = ( 1, 2, ( 3, 4 ), 5, ( ( 6, 7, 8, ( 9, 10 ), 11 ), 12, 
    13 ), ( ( 14, 15, 16 ), ( 17, 18, 19, 20 ) ) )

def display_inttuple( it ): #copied solution
    for element in it:
        if isinstance( element, int ):
            print( element, end=" ")
        else:
            display_inttuple( element )

display_inttuple( inttuple )
