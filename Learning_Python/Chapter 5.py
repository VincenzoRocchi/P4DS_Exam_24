#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 15:11:37 2022

@author: vincenzorocchi
"""

#in line exercises chapter 5
#%% exercise 5.1

#Exercise 5.1 Ask the user to enter a string. Then print the length of that string. 
#Use the input() function rather that the getString() function from pcinput, 
#as the getString() function removes leading and trailing spaces.

print("wanna know the enght of your phrase?")
x = input("Just write something down  ")

lenght = len(x)

print("{} is {} words long".format(x, lenght))

#%% exercise 5.2

#The Pythagorean theorem states that of a right triangle, the square of the length of the diagonal
#side is equal to the sum of the squares of the lengths of the other two sides (or a2 + b2 = c2).
#Write a program that asks the user for the lengths of the two sides that meet at a right angle,
#then calculate the length of the third side (in other words: take the square root of the sum of 
#the squares of the two sides that you asked for), and display it in a nicely formatted way.
#You may ignore the fact that the user can enter negative or zero lengths for the sides.

import math as math
import pcinput as pc

print("calculating the diagonal side of a triangle!","\n")

short_side1 = pc.getInteger("write your side here: ")
short_side2 = pc.getInteger("write the other side here: ")

pyth = (short_side1**2 + short_side2**2)

result = math.sqrt(pyth)
result = round(result,2)

print("the lenght of the diagonal is {}".format(result))

#%% exercise 5.3

#Ask the user to enter three numbers. Then print the largest, the smallest,
#and their average, rounded to 2 decimals.

import math as math
x = list(map(float,input("Enter 3 comma separated values: ").split(",",3)))
print("\n")
lenght = round(len(x),2)
smallest = round((min(x)),2)
largest = round((max(x)),2)

somma = sum(x)
average = float(somma/lenght)
average = round(average,2)

print("your smallest number is {} ".format(smallest))
print("your largest number is {} ".format(largest))
print("the average is {} ".format(average))

#%% exercise 5.4

#Calculate the value of e to the power of -1, 0, 1, 2, and 3, and display the results,
#with 5 decimals, in a nicely formatted manner.

from math import pow

e = input("write a number here: ")
e = float(e)

first = pow(e,-1)
second = pow(e, 0)
third = pow(e, 1)
fourth = pow(e,2)
fifth = pow(e,3)

result = "the power of e to {:^3d} is {:>15.5f}"
print(result.format(-1,first))
print(result.format(0,second))
print(result.format(1,third))
print(result.format(2,fourth))
print(result.format(3,fifth))

#%% exercise 5.5

#Exercise 5.5 Suppose you want to generate a random integer between 1 and 10 
#(1 and 10 both included), but from the random module you only have the random() 
#function available (you can use functions from other modules, though). How do you do that?

from math import log10
from random import random,seed

for x in range (1):
    seed()
    x = random()
    x = x*10
    print(int(x))
    
    