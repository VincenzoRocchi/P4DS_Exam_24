#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:40:48 2022

@author: vincenzorocchi
"""

#in line exercises
#%% exercise 1

x = 1/2
y = 0.5
one_divided_2 = (x < 0.5, x > 0.5, x == 0.5)

print(x , y)
print(one_divided_2)

#%%exercise 2

my_name = "vincenzo"

print( "a" in my_name)
print( "e" in my_name)
print( "i" in my_name)
print( "o" in my_name)
print( "u" in my_name)

#%%exercise 3

a = False
b = True
c = True

print( (a and b) or c ) 
print( a and (b or c) )

#%% exercise 4

#You can test whether an integer is odd or even using the modulo operator.
# Specifically, when x%2 equals zero, then x is even, else it is odd. 
#Write some code that asks for an integer and then reports whether it is
# even or odd (you can use the getInteger() function from pcinput to ask 
#for an integer).

import pcinput as pc #module 

print("is it even or odd??")
num = pc.getInteger("Let's find out: ")

if num%2 == 0:
    print("even")
if num%2 != 0:
    print("odd")
    
#%% exercise 5

#xercise Write a program that defines a variable weight. 
#If weight is greater than 20 (kilo’s), print: 
#“There is a $25 surcharge for luggage that is too heavy.”
#If weight is smaller than 20, print: “Have a safe flight!” If weight
#is exactly 20, print: “Pfew! The weight is just right!” Make sure
#that you change the value of weight a couple of times to check 
#whether your code works.

weight = 25

if weight > 20 :
    print("there is a 25$ surcharge for luggage that is too heavy")
elif weight <20:
    print("Have a safe flight!")
elif weight == 20:
    print("Just about right!")
else:
    print("WTF?")
    
#%% exercise 6

x = 7
if x%7 == 0:
    # --- Here starts a nested block of code ---
    if x%11 == 0:
        print( x, "is dividable by both 7 and 11." )
    else:
        print( x, "is dividable by 7, but not by 11." )
    # --- Here ends the nested block of code ---
elif x%11 == 0:
    print( x, "is dividable by 11, but not by 7." )
else:
    print( x, "is dividable by neither 7 nor 11." )
    
    
#%% Exercise 6.1

#Exercise 6.1 Grades are values between zero and 10 (both zero and 10 
#included), and are always rounded to the nearest half point. 
#To translate grades to the American style, 8.5 to 10 become an
#“A,” 7.5 and 8 become a “B,” 6.5 and 7 become a “C,” 5.5 and 6 become 
#a “D,” and other grades become an “F.” Implement this translation, 
#whereby you ask the user for a grade, and then give the American 
#translation. If the user enters a grade lower than zero or higher 
#than 10, just give an error message. You do not need to handle the 
#user entering grades that do not end in .0 or .5, though you may do
#that i#f you like – in that case, if the user enters such an illegal
#grade, give an appropriate error message.

import pcinput as pc

grade = pc.getFloat("Insert your grade here -->")

#rounding to closest .5
grade = round(grade*2)/2

#grades list
A = [10,9.5,9,8.5]
B = [8,7.5]
C = [7,6.5]
D = [6,5.5]
F = [5,4.5,4,3.5,3,2.5,2,1.5,1,0.5]

#function
if grade == 0 or grade > 10:
    print("processing")
    print("uhm....")
    print("Wrong number, try again!")
    
if grade >0 or grade <10:
    if grade in A:
        print("You got an \"A\"")
    elif grade in B:
        print("You got a \"B\"")
    elif grade in C:
        print("You got a \"C\"")
    elif grade in D:
        print("you got a \"D\"")
    elif grade in F:
        print("Well done you got an \"F\"")
    else:
        exit()
    
#%% exercise 6.2

#spot the error
score = 98.0
if score >= 60.0:
    grade = 'D'
elif score >= 70.0:
    grade = 'C'
elif score >= 80.0:
    grade = 'B'
elif score >= 90.0:
    grade = 'A'
else:
    grade = 'F'
print( grade )

#corrected version
score = 98.0
if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'B'
elif score >= 70.0:
    grade = 'C'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'F'
print( grade )

#%% exercise 6.3

#Ask the user to supply a string. Print how many different vowels 
#there are in the string. The capital version of a lower case vowel 
#is considered to be the same vowel. y is not considered a vowel. 
#Try to print nice output (e.g., printing “There are 1 different 
#vowels in the string” is ugly). Example: When the user enters the
#string “It’s Owl Stretching Time,” the program should say that
#there are 3 different vowels in the string.

print("let's find out how many vowels there are in a phrase!")
#my_str = input("Write down whatever you want: ")

my_str = "Ciao"

def countvowels(string):
    numvowels = 0
    for char in string:
        if char in "aeiou":
            numvowels += 1

countvowels(my_str)
    

#%% Exercise 6.4

#Exercise 6.4 You can solve quadratic equations using the quadratic formula.
#Quadratic equations are of the form Ax2 + Bx + C = 0. Such equations have
#zero, one or two solutions. The first solution is 
#(−B + sqrt(B2 − 4AC))/(2A). The second solution is 
#(−B − sqrt(B2 − 4AC))/(2A). There are no solutions if the value under 
#the square root is negative. There is one solution if the value under 
#the square root is zero. Write a pro- gram that asks the user for the 
#values of A, B, and C, then reports whether there are zero, one, or two 
#solutions, then prints those solutions. Note: Make sure that you also 
#take into account the case that A is zero (there is only one solution 
#then, namely −C/B), and the case that both A and B are zero.

import math
import pcinput as pc

print("lets solve a quadratic equation")
print("you have to insert the values for \"A\", \"B\" and \"C\"")

A = 6 #pc.getInteger("insert A: ")
B = 11 #pc.getInteger("insert B: ")
C = 35 #pc.getInteger("insert C: ")

if A == 0 and B > 0:
    print(-B/C)

elif A == 0 and B == 0:
    print("get your shit togheter")
    
elif A > 0 and B > 0:
    DELTA = (B**2) - (4*A*C)
    SQRT = math.sqrt(DELTA)
    solution1 = (-B + SQRT) / (2*A)
    solution2 = (-B - SQRT) / (2*A)
    solution1 = round(solution1, 4)
    solution2 = round(solution1, 4)
    if DELTA > 0:
        print("There are two solutions")
        print("solutions are: {} and: {}".format(solution1, solution2))
    elif DELTA == 0:
        print("There is only one solution")
        print("And it is: ", solution1)
    elif DELTA < 0:
        print("There are no solutions with a discriminant that equals zero")
  
