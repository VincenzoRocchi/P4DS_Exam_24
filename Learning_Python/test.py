#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:42:01 2022

@author: vincenzorocchi
"""

# in line exercises chapter 3 - first programming chapter

#%% exercise 1

#Display some texts of your liking using a Python program.
#But take note that if you want to display text strings, you have to enclose them
#in double quotes – or single quotes, those work too.

print("hello i like fucking vagianas and asses" , "btw",
      "getting BJ too, a lot,", "i'm", 4 , "real")

print("hello i\'m vincenzo and i like pussy")
print("hello i\\'m vincenzo and i like pussy")

#%% exercise 2

#When you use integers in Python, you cannot write them with “thousands separators”
#(commas in English) to make them more readable. I.e., the number one billion
#should be written as 1000000000 rather than 1,000,000,000.
#Check out the following code and think about what it will display when you run it.
#Then copy it to the Python shell and run it.

#print( 1,000,000,000 )

#Exercise If your prediction of what this code would do was not correct,
#find out why it produces this result.

print(1,000,000,000)

#you cannot write it like this
#but you can use unscores "_" to separate and create no problems

print(1_000_000_000)


#%% exercise 3

#Exercise. Now it is time to write your first program.
#Write a program that displays the number of seconds in a week.
#You should, of course, not grab your calculator or smart- phone to do the
# calculation and then just print the resulting number, but you should do 
#the calculation in Python code. Since this program needs only one line of code,
#you could just write it in the Python shell, though you are encouraged to create 
#a program file and use that.

days = 7
hours = 24
minutes = 60
seconds = 60

seconds_in_a_week = (days*hours*minutes*seconds)

print("there are:", seconds_in_a_week, "seconds in a week")

#if you go further a bit in the book you can solve the space problem by
#concatenating the value to the strings with the str() casting function
#something like that -->

print("there are:" + str(seconds_in_a_week) , "seconds in a week")

#%% Exercise 3.1 

#The cover price of a book is $24.95, but bookstores get a 40 percent discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# Calculate the total wholesale costs for 60 copies.

book = 24.95
store_discount = .40
ship_cost1 = 3
ship_cost2 = .75
copies = 60

book_cost = (book - (book*store_discount))
ship_cost = (ship_cost1 + (ship_cost2)*(copies - 1))

wholesale_cost = copies * book_cost + ship_cost

print("total cost would be", round(wholesale_cost, 2))

#%% Exercise 3.5

#ou look at the clock and see that it is currently 14.00h.
# You set an alarm to go off 535 hours later.
#At what time will the alarm go off? Write a program that prints the answer.
# Hint: for the best solution, you will need the modulo operator

import pcinput as pc

print("see at wich hour yout alarm will go of!")

current_time = pc.getInteger("insert your current time:")
alarm_hours = pc.getInteger("how long till it goes off? : ")
print("\n")

days_passed = round(alarm_hours/24)
going_off_hour = alarm_hours%24 + current_time

print("your allarm will go off in", days_passed, "days", "at", str(going_off_hour)+".00" )


#%%

