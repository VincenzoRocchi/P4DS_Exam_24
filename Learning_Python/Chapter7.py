#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  1 22:12:59 2022

@author: vincenzorocchi
"""

#in line exercises
#%% exercise 1

num = 1
while num <= 9:
    print( num )
    num += 2
print( "Done" )

#%%

from pcinput import getInteger

total = 0
i = 0
while i < 2:
    total += getInteger( "Please insert first number: " )
    i += 1
    if i>0:
        total += getInteger("pls insert second")
    i += 1
    if i>1:
        total += getInteger("pls insert third")
    i+= 2
    
print( "Total is", total, total/(i) )

#%%
import pcinput as pc

num = pc.getInteger("here thx:")
total = 0
i = 1

while num != 0:
    total += num
    num = pc.getInteger("insert")
    i +=1
    
print("done", total, total/i)

#%%

#fix the loop so it ends - endless loop

number = 1
total = 0

while (number*number)%1000 == 0:
    total += number
    
print( "Total is", total )

#%% 

#Exercise Write countdown code. It starts with a given number 
#(e.g., 10), and counts down to zero, printing each number it encounters 
#(10, 9, 8, ...). It does not print 0, instead it prints “Blast off!”

num = 10
while num > 0:
    print(num)
    num -= 1
    if num == 0:
        print("Blast off")
        
#%% 

#write a program that calculates the factorial of a number 

num = 10
factorial = 1
i = 0

while i < num:
    i+=1
    factorial = factorial*i
    print(factorial)
    
#%%

fruit = "banana"

for letter in fruit:
    print( letter ) 
    if letter == "n":
        fruit = "orange" 
print( "Done" )

#%%
for x in range(100):
    print(x) 
    
#%%
for x in range (10,100,10):
    print(x)
    
#%%
for x in range(100, 0, -5):
    print(x)

#%%

#Exercise Use the for loop and range() function to print multiples 
#of 3, starting at 21, counting down to 3, in just two lines of code.

for x in range(21,0,-3):
    print(x)
    
#%%

for x in ("apple", "pear", "orange", "banana", "mango", "cherry"):
    print( x )

#%%

import pcinput as pc

#Exercise You already created code with a while loop that asked 
#the user for five numbers, and displayed their total. 
#Create code for this task, but now use a for loop.

total = 0

for x in range(5):
    num = pc.getInteger("hsdhadas")
    total += num
    print(total)
    
#%%

#Create a countdown function that starts at a certain count, 
#and counts down to
#zero. Instead of zero, print “Blast off!” Use a for loop.

for x in range(10,-1,-1):
    if x > 0:
        print(x)
    if x == 0:
        print("blast off")
        
#%%


i=1
while i <= 1000000:
    num1 = int( "1" +  str(i)  ) 
    num2 = int( str( i ) + "1" ) 
    if num2 == 3 * num1:
        print( num2, "is three times", num1 )
        break
    i += 1 
else:
    print( "No answer found" )

#%%

for grade in ( 8, 7.5, 9, 6, 6,5, 6, 7, 8, 7, 7.5 ):
    if grade < 5.5:
        print( "The student fails!" )
        break
else:
    print( "The student passes!" )
    
    
#%%

#listing0710.py
num = 0

while num < 100:
    num += 1
    if num%2 == 0:
        continue 
    if num%3 == 0:
        continue
    if num%10 == 7:
        continue
    if num%10 == 9:
        continue 
    print( num )
    
#%% exercise

#Exercise Write a program that processes a collection of numbers using 
#a for loop. The program should end immediately, printing only the word 
#“Done,” when a zero is encoun- tered (use a break for this). Negative 
#numbers should be ignored (use a continue for this; I know you can also
#do this with a condition, but I want you to practice with continue). 
#If no zero is encountered, the program should display the sum of 
#all numbers (do this in an else clause). Always display “Done” 
#at the end of the program. Test your program with the collection 
#( 12, 4, 3, 33, -2, -5, 7, 0, 22, 4 ). With these numbers,
#the program should display only “Done.” If you remove the zero, ù
#it should display 85 (and “Done”).

num = 0

for x in ( 12, 4, 3, 33, -2, 0, -5, 7, 22, 4 ):
    if x == 0:
        break
    if x < 0:
        continue
    else:
        num += x
        print(num)
        
print("Done!")

#%% exercise 

for i in range( 3 ):
    print( "Entering the outer loop for i =", i )
    for j in range( 3 ):
        print( "    Entering the inner loop for j =", j )
        print( "    (i,j) = ({},{})".format( i, j ) )
        print( "    Leaving the inner loop for j =", j )
    print( "Leaving the outer loop for i =", i )

#%%
for i in range( 4 ):
    for j in range( i+1, 4 ):
        print( "({},{})".format( i, j ) )

#%%

#Exercise Write code that prints all pairs (i,j) where i and j can take on the values 
#0 to 3, but they cannot be equal.

for i in range (4):
    for j in range (4):
        if j != i:
            print(("{} ,{}").format(i,j))
            
#%%

from pcinput import getInteger
from pcinput import getInteger 

while True:
    x = getInteger( "Enter number 1: " ) 
    if x == 0:
        break
    y = getInteger( "Enter number 2: " )
    if y == 0:
        break
    if (x < 0 or x > 1000) or (y < 0 or y > 1000):
        print( "The numbers should be between 0 and 1000" )
        continue
    if x%y == 0 or y%x == 0:
        print( "Error: the numbers cannot be dividers" )
        exit()
    print( "Multiplication of", x, "and", y, "gives", x * y )
        
print( "Goodbye!" )

#%%

# =============================================================================
# Exercise The user must enter a positive integer. You use the getInteger() f
# unction from pcinput for that. This function also allows entering negative numbers.
# If the user enters a negative number, you want to print a message and ask him again, 
# until he entered a positive number. Once a positive number is entered, you print that
# number and the program ends. Such a problem is typically solved using a loop-and-a-half,
#   as you cannot predict how often the user will enter a negative number before he gets wise. 
#   Write such a loop-and-a-half (you will need exactly one break, and you need at
# most one continue). Print the final number that the user entered after
#   you have exited the loop. The reason to do it afterwards is that the loop is
#   just there to control the entering of the input, not the processing of the resulting variable.
# =============================================================================
 
from pcinput import getInteger

while True:
    num = getInteger("Write whatever number you want: ")
    if num <0:
        print("you should enter a positive number")
        continue
    if num >0:
        break

print("Great: {} ".format(num))

#%% Exercise 7.1

# =============================================================================
# # Write a program that lets the user enter a number. 
# # Then the program dis- plays the multiplication table for that 
# # number from 1 to 10. E.g., when the user enters 12, the first 
# # line printed is “1 * 12 = 12” and the last line printed is “10 * 12 = 120”.
# =============================================================================

from pcinput import getInteger

num = getInteger("here: ")

for i in range (1,11):
    x = num * i
    print(x)
    
#%%exercise 7.2
# =============================================================================
# If you did the previous exercise with a while loop, then do it again 
# with a for loop. If you did it with a for loop, then do it again with a while
# loop. If you did not use a loop at all, you should be ashamed of yourself.
# =============================================================================

num = getInteger("here: ")
i = 1

while i < 11:
    x = num *i
    print(x)
    i += 1
    continue

#%% Exercise 7.3 

# =============================================================================
# Write a program that asks the user for ten numbers, and then prints the 
# largest, the smallest, and how many are divisible by 3. Use the algorithm 
# described earlier in this chapter.
# =============================================================================
from pcinput import getInteger

i=0
while i in range (3):
    num1 = getInteger("here")
    num3 = num1
    num2 = num1
    if num1 > num3:
        num3 = num1
    else:
        num2 =num1
        
    i+=1
print(num3)
print(num2)
#%%Exercise 7.4 

# =============================================================================
# “99 bottles of beer” is a traditional song in the United States and Canada. 
# It is popular to sing on long trips, as it has a very repetitive format which 
# is easy to memorize, and can take a long time to sing. The song’s simple lyrics
#  are as follows: “99 bottles of beer on the wall, 99 bottles of beer. Take one
#  down, pass it around, 98 bottles of beer on the wall.” The same verse is repeated,
#  each time with one fewer bottle. The song is completed when the singer or singers 
#  reach zero. Write a program that generates all the verses of the song (though you 
# might start a bit lower, for instance with 10 bottles). Make sure that your loop 
# is not endless, and that you use the proper inflection for the word “bottle.”
# =============================================================================
x = "bottles"
y = "bottle"

i= 100

while i >0:
    if i > 1:
        print("""{} {} of beer on the wall, {} {} of beer. take one down, pass it around,
              {} {} of beer on the wall \n""".format(i,x,i,x,i-1,x))
    elif i == 1:
        print("""{} {} of beer on the wall, {} {} of beer. take one down, pass it around,
              {} {} of beer on the wall""".format(i,y,i,y,i-1,x))
    i-=1
    
#%% exercise 7.5

# =============================================================================
# Exercise 7.5 The Fibonacci sequence is a sequence of numbers that starts with 1, 
# followed by 1 again. Every next number is the sum of the two previous numbers. 
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,... Write a program that 
# calculates and prints the Fibonacci sequence until the numbers get higher than 1000.
# =============================================================================
from sys import exit

n1, n2 = 0,1
i = 0

for i in range (10):
    print(n1)
    nth = n1+n2
    n1 = n2
    n2 = nth
    i += 1

#%% Exercise 7.6

# =============================================================================
# Write a program that asks the user for two words. Then print all 
# the char- acters that the words have in common. You can consider 
# capitals different from lower case letters, but each character that 
# you report, should be reported only once (e.g., the strings “bee”
# and “peer” only have one character in common, namely the letter “e”). 
# Hint: Gather the characters in a third string, and when you find a 
# character that the two words have in common, check if it is already 
# in the third string before reporting it.
# =============================================================================

str1, str2 = input(str("write something here: ")), input(str("comparing it to something here: "))
str3 =""

for i in range (len(str1)):
    i = str1[i]
    for j in range (len(str2)):
        j= str2[j]
        if j in str3:
            continue
        if [j] == [i]:
            str3 += str(i) +","
            
if len(str3) < 1:
    print("No words in common")
if len(str3) >1:
    print("this characters are the one in common", "\"", str3, "\"")
            
#%% exercise 7.7 manco per il cazzo lo faccio

#%% Exercise 7.8

# =============================================================================
# Write a program that takes a random integer between 1 and 1000 (you can use the randint() 
# function for that). The program then asks the user to guess the number.
#  After every guess, the program will say either “Lower” if the number it
#  took is lower, “Higher” if the number it took is higher, and “You guessed
#  it!” if the number it took is equal to the number that the user entered. It 
#  will end with displaying how many guesses the user needed. It might be wise,
#  for testing purposes, to also display the number that the program randomly picks,
#  until you are sure that the program works correctly.
# =============================================================================

from random import randint
import pcinput as pc

print("generating a random number...")
print("try and guess it!")

count = 0
rand = randint(1, 1000)
print(rand)

while True:
    guess = pc.getInteger("Take a guess: ")
    if guess > rand:
        print("wrong one, try again but go lower!\n")
        count += 1
    elif guess < rand:
        print("wrong one, try again but go higher!\n")
        count += 1
    elif guess == rand:
        break
    else:
        exit()
        
print("congrats!")
print("it took you \"only\" {} tries".format(count))

#%% Exercise 7.9

# =============================================================================
# Write a program that is the opposite of the previous one: now you take
#  a number in mind, and the computer will try to guess it. You respond 
#  to the computer’s guesses by entering a letter: “L” for lower if the 
#  number to guess is lower, “H” for higher if the number to guess is higher,
#  and “C” for correct (you can use the getLetter() function from pcinput for that)
#  . Once the computer has guessed your number, it displays how many guesses it needed. 
#  Make sure that you let the computer recognize when there is no answer (maybe 
# because you made a mistake or because you tried to fool the computer). A 
# smart program will need at most ten guesses.
# =============================================================================

from pcinput import getLetter
guess = randint(1, 100)
print(guess)

correct = "c"
higher = "h"
lower = "l"
correction = input(str("Write l for lower, h for higher or c if correct: "))

while True:
    for correction in range (len(correct)):
        if correction == correct:
            break
        

print("hi")