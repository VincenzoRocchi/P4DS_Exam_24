#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:52:52 2022

@author: vincenzorocchi
"""

#in line exercises chapter 4
#%% exercise 1

#Exercise In the previous chapter you wrote a calculation that determines the number of
#seconds in a week. Copy this calculation into a program, and assign it to a variable.
#Then add a statement to print the contents of the variable.

#already did it if right in the previous exercise
#exercisenumber 3 chapter 3

#%% Exercise 4.1

#Define three variables var1, var2 and var3. Calculate the average of these
#variables and assign it to average. Print the average. Add three comments.

VAR1=1 #first variabble
VAR2=2 #second variable
VAR3=3 #third variable

AVERAGE = ((VAR1+VAR2+VAR3)/3)

print(AVERAGE)

#%% Exercise 4.2

#Write code that can compute the surface of circle, using the variables radius and pi = 3.14159.
#The formula, in case you do not know, is radius times radius times pi.
#Print the outcome of your program as follows: “The surface area of a circle with radius ... is ...”

radius=5
pi=3.14159

area= radius*radius*pi

print("The surface area of a circle with radius", radius,"is", area)

#%% Exercise 4.3

"""
Exercise 4.3 Write code that classifies a given amount of money (which you store in a
variable named amount), specified in cents, as greater monetary units. Your code lists the
monetary equivalent in dollars (100 ct), quarters (25 ct), dimes (10 ct), nickels (5 ct), 
and pennies (1 ct). Your program should report the maximum number of dollars that fit in 
the amount, then the maximum number of quarters that fit in the remainder after you subtract 
the dollars, then the maximum number of dimes that fit in the remainder after you subtract 
the dollars and quarters, and so on for nickels and pennies. The result is that you express
the amount as the minimum number of coins needed.
"""
import pcinput as pc

print("trasforming your cents in avery possible way")
print("and see how much of any you should have!\n")

amount= pc.getInteger("insert an amount here -->")

dollars= amount/100
quarters= amount/25
dimes= amount/10
nickels= amount/5

print("dollars =",dollars)
print("quarters =", quarters)
print("dimes =", dimes)
print("nickels =", nickels,"\n")

max_dollar_am = int(amount/100)
print("max dollar amount=", max_dollar_am,"\n")

amount_left = amount - max_dollar_am*100
quarters_left = amount_left%100/25
print("quarter amount after dollar subtraction", int(quarters_left),"\n")

amount_left -= int(quarters_left)*25
dimes_left = amount_left%100/10
print("dimes amount after quarter subtraction", int(dimes_left),"\n")

amount_left -= int(dimes_left)*10
nickels_left =amount_left%100/5
print("nickels amount after dimes subtraction", int(nickels_left))

#%% Exercise 4.4

a = 17
b = 23
print( "a =", a, "and b =", b )
a += b
b = a - b #done
a = a - b #done

print("a=", a, "b=", b)
# add two more lines of code here to cause swapping of a and b print( "a =", a, "and b =", b )

