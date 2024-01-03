#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 14:49:30 2022

@author: vincenzorocchi
"""

#%% factorial recursive function test

def fact( n ):
    if n == 1:
        return n
    return n * fact( n-1 )

print( fact( 10) )

#%% exercise 9.1 - 9.2 - 9.3

# =============================================================================
# Exercise 9.1 A recursive definition of the nth number of the Fibonacci
#  sequence fib(n) states that fib(n) is equal to fib(n-1) + fib(n-2). Moreover
#  , fib(1) and fib(2) are both 1. Write a recursive function that you can call 
#  with an integer argument n that returns the nth number of the Fibonacci sequence.
# =============================================================================

# Python program to display the Fibonacci sequence - copiata netta

def recur_fibo(n, depth = 0):
    # indent = depth * 4 *" "
    if n <= 1:
        return n
    else:
        x = (recur_fibo(n-1, depth +1) + recur_fibo(n-2, depth +1))
        # print(indent, x)
        return x
    
   
recur_fibo(15)

#%% exercise 9.4 

# =============================================================================
# Exercise 9.4 The greatest common divider is the greatest integer that 
# divides two other integers without remainder. For instance, the greatest 
# common divider of 14 and 21 is 7, as 7 is the greatest number that divides
#  both 14 and 21. Euclid’s algorithm that calculates the greatest common 
#  divider of two numbers says that if the largest divided by the smallest 
#  is an integer, it is the smallest. Otherwise, it is the result of 
#  calculating the greatest common divider of the smallest and the remainder 
#  of the largest divided by the smallest. This is a recursive defintion.
#  Implement Euclid’s algorithm in a recursive function. Hint: testing whether 
#  two numbers divide each other, and calculating the remainder, can both be 
#  done with the modulo operator. This code can be really brief.
# =============================================================================

#Greatest Common Divider

def GCD(n1, n2):
    if n1%n2 == 0:
        return n2
    return GCD(n2, n1%n2)
        
GCD(1460,230)

#%% exercise 9.5


