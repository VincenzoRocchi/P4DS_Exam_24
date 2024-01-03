#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 19:36:47 2022

@author: vincenzorocchi
"""

# in line exercises

#%% in line

# =============================================================================
# Exercise Write a while loop to print the elements of a list.
# =============================================================================


fruitlist = ["apple", "banana", "cherry", 27, 3.14]

i = 0
while i < len(fruitlist):
    print(fruitlist[i])
    i += 1
    
#%% in line

# =============================================================================
# Change a list that contains only words (you can take one of the fruitlists
# above) by turning every word in the list into a word consisting 
# of only capitals. At this point in the book, the way to do that
#  is by using a while loop that uses a variable i that starts at 0 
#  and runs up to len(<list>)-1. Use i as an index for this list.
# =============================================================================

fruitlist = ["apple", "banana", "cherry", "durian", "orange"] 

i = 0
while i < len(fruitlist):
    fruitlist[i] = fruitlist[i].upper()
    i += 1

for i in range(len(fruitlist)):
    fruitlist[i] = fruitlist[i].upper()
    
print(fruitlist)

#%% 

#exercise 12.1

# =============================================================================
# Exercise 12.1 A magic 8-ball, when asked a question, provides a random
#  answer from a list. The code below contains a list of possible answers.
#  Create a magic 8-ball program that asks a question, then gives a random answer.
# =============================================================================
import random

answers = [ "It is certain", "It is decidedly so", "Without a \ doubt", 
            "Yes, definitely", "You may rely on it", "As I see it, \ yes",
            "Most likely", "Outlook good", "Yes", "Signs point to yes", 
            "Reply hazy try again","Ask again later", "Better not tell you \ now",
            "Cannot predict now", "Concentrate and ask again",
            "Don ' t \ count on it", "My reply is no", "My sources say no",
            "Outlook \ not so good", "Very doubtful" ]

def otto_ball(l1):
    input("write down a question: ")
    l = len(l1)
    x = random.randint(0, l)
    return(l1[x])


def otto_ball2(l1):
    input("write down a question: ")
    return(random.choice(l1))

print(otto_ball2(answers))

#%% 

# =============================================================================
# Exercise 12.2 A playing card consists of a suit ("Hearts", "Spades", "Clubs",
# "Diamonds") and a value (2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace").
# Create a list of all possible playing cards, which is a deck. Then create a func- 
# tion that shuffles the deck, producing a random order.
# =============================================================================
import random

sym = ["Hearts", "Spades", "Clubs", "Diamonds"]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]
deck = []

def deck_shuffle(sym, cards):
    for i in range(len(sym)):
        for j in range(len(cards)):
            deck.append((str(cards[j]) + " of " +  str(sym[i])))
    random.shuffle(deck)
    return deck
        
print(deck_shuffle(sym, cards))

#%%