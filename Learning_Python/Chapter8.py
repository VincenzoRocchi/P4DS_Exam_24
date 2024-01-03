#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:17:23 2022

@author: vincenzorocchi
"""

# in line ecìxercises

# %% exerise 1

# =============================================================================
# Exercise Write a function called printx() that just prints the letter “x.” 
# Then write a function called multiplex() which takes as argument an integer 
# and prints as many times the letter “x” as the integer indicates by calling 
# the function printx() that many times.
# =============================================================================
    
def multiplex(user_numx):
    
    def printx ():
        print("x")
        
    for j in range(user_numx):
        printx()
        
multiplex(100)
    
#%% exercise 2

# =============================================================================
# Exercise Write the function isEven().
#
# Exercise Write the function isOdd(), which determines whether a number is odd, by
# calling the function isEven() and inverting its result.
# =============================================================================

def isOddorEven(x):
    
    def isEven(x):
        j = x%2 == 0
        if x > 0:
            return j
        if x < 0:
            abs(j)
            return j
        
    if not isEven(x):
        print("its odd")
    if isEven(x):
        print("its even")
      
isOddorEven(14)

#%% exercise 3

# =============================================================================
# Write the function getFraction().
# =============================================================================

def getFraction(user_x):
    user_x = float(user_x)
    result = user_x%1
    return round(result,3)

getFraction(1.567842)

#%% Exercise 8.1

# =============================================================================
# Exercise 8.1 Create a function that gets a number as parameter, and then 
# prints the multiplication table for that number from 1 to 10. E.g., when the
# parameter is 12, the first line printed is “1 * 12 = 12” and the last line 
# printed is “10 * 12 = 120.”
# =============================================================================

def table_multiply(x = input("write down a number: ")):
    for i in range (1,11):
        result = int(x)*i
        print("{} * {} = {}".format(i,x,result))
        i +=1
        
table_multiply()

#%% exercise 8.2

# =============================================================================
# Write a function that gets as parameters two strings. The function 
# returns the number of characters that the strings have in common. Each character 
# counts only once, e.g., the strings "bee" and "peer" only have one character in 
# common (the letter “e”). You can consider capitals different from lower case
#  letters. Note: the function should return the number of characters that the 
#  strings have in common, and not print it. To test the function, you can print 
#  the result in your main program
# =============================================================================

def comparing_characters(str1 = input("Strings pls"), str2 = input("Strings pls")):
    str3 = ""
    for i in range (len(str1)):
        i = str1[i]
        for j in range (len(str2)):
            j= str2[j]
            if j in str3:
                continue
            if [j] == [i]:
                str3 += str(i) +" "
    return(str3)
    
        
print(comparing_characters())  

#%% exercise 8.3

# =============================================================================
# The Grerory-Leibnitz series approximates pi as 4 ∗ (1/1 − 1/3 + 1/5 − 1/7 + 1/9...)
# . Write a function that returns the approximation of pi according to this series. 
# The function gets one parameter, namely an integer that indicates how many of the 
# terms between the parentheses must be calculated.     
# =============================================================================

def grer_leib(x):
    result = 0
    for i in range(x):
        main_div = 1/i
        result += main_div
        
        
#%% exercise 8.4

# =============================================================================
# Exercise 8.4 In Chapter 6 you were asked to implement the quadratic formula to solve 
# quadratic equations. A quadratic equation is described by three numeric values, 
# usually called A, B, and C. It has zero, one, or two solutions, depending on the
#  discriminant (the part under the square root). Write a function that solves a 
#  quadratic equation. As param- eters it gets A, B, and C. It returns three values.
#  The first is an integer that indicates the number of solutions. The second is the 
#  first solution. The third is the second solution. Any of the solutions that do not
#  exist, you can return as zero.
# 
# =============================================================================


# =============================================================================
# NOT WORKING
# =============================================================================
import math
import pcinput as pc

print("lets solve a quadratic equation")
# print("you have to insert the values for \"A\", \"B\" and \"C\"")

A = 536 #pc.getInteger("insert A: ")
B = 0 #pc.getInteger("insert B: ")
C = 86 #pc.getInteger("insert C: ")


def quadratic_function(A,B,C):
    if A == 0 and B > 0:
        return (-B/C)
    
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
        
quadratic_function(6,11,35)
        
#%% exercise 8.5

# =============================================================================
# Exercise 8.5 In Chapter 7, the loop-and-a-half was explained. The final code
# for the example that was presented is given below, and I made the remark that 
# there is still some- thing ugly about this code, namely the fact that if x is 
# smaller than zero or higher than 1000, the code still asks for y even when it 
# can know that it has to ask a new value for x. I also remarked that you can 
# resolve this in an easy way by using a function. Create a function and insert
#  it in this code, so that this issue gets fixed. Also get rid of the exit() 
#  and thus the possible ugly output by introducing a main() function.
# =============================================================================

from pcinput import getInteger

def getx():
    while True:
        x = getInteger( "Enter x: " )
        if x < 0 or x >1000:
            print("your number has to be between 0 and 1000")
            continue
        if 0 < x <= 1000:
            break
    return x
    
def gety():
    while True:
        y = getInteger( "Enter y: " )
        if y < 0 or y >1000:
            print("your number has to be between 0 and 1000")
            continue
        if 0 < y <= 1000:
            break
    return y

def multiplication_x_y():
    x, y = getx(),gety()
    if y%x == 0 or x%y == 0:
        print( "Error: the numbers cannot be dividers" )
        return
    else:
        print( "Multiplication of", x, "and", y, "gives", x * y )
    
multiplication_x_y()

#%% exercise 8.6

# =============================================================================
# Exercise 8.6 In statistics, the binomial coefficient indexed by n and k 
# (often expressed as “n over k,” whereby n must be bigger than or equal to k)
# 
#  is calculated as n!/(k! ∗ (n − k)!), whereby n! indicates the factorial of n.
#  As I explained in Chapter 7: the factorial of a positive integer is that integer,
#  multiplied by all positive integers that are lower (excluding zero). You write the 
#  factorial as the number with an exclamation mark after it. E.g., the factorial of
#  5 is 5! = 5∗4∗3∗2∗1 = 120. If you did all the exercises until now, you wrote some 
#  code for this. Write a function that calculates the binomial coefficient for its 
#  two parameters, and returns the value. Write the code in such a way that it can
#  be used as a module by another program (i.e., put the tests of your program in
#  a main() function that is called as explained above).
# =============================================================================

def factorial_calc(num):
    factorial = 1
    i = 0
    while i < num:
        i+=1
        factorial = factorial*i
    return factorial
    
def binomial_coeff(n,k):
    coeff = n-k
    
    coefffact = factorial_calc(coeff)
    nfact = factorial_calc(n)
    kfact = factorial_calc(k)
    result = nfact/(kfact * coefffact)
    if result > 1:
        return result
    else:
        return
    
binomial_coeff(10, 4)



