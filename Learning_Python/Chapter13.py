#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 21 16:40:13 2022

@author: vincenzorocchi
"""

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

print(fruitbasket["mango"])

#%% adding elements to a dictonary

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

fruitbasket["mango"] = 15
print(fruitbasket["mango"])

#%% modifying elements in a dictonary and deleting them

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

fruitbasket["apple"] = 15
print(fruitbasket["apple"])

# del fruitbasket['banana']
for key in fruitbasket:
    print("{} {}".format(key, fruitbasket[key]))
    
#%% as its not ordered u cnnot use the slice trick to copy a dictonary
# cause its returning an alias of the 1st variable and not an actul copy 

fruitbasket = { "apple":3, "banana":5, "cherry":50 } 
fruitbasketalias = fruitbasket
fruitbasketcopy = fruitbasket.copy()

print(id(fruitbasket),
      id(fruitbasketalias),
      id(fruitbasketcopy),
      )

#%% u cannot make a deep copy whitout importing the copy function 
import copy

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

ciao = copy.deepcopy(fruitbasket)
fruitbasket["apple"] = 15

ciao2 = copy.copy(fruitbasket)

fruitbasket["apple"] = 15

print(fruitbasket)
print(ciao)
print(ciao2)

#%%

fruitbasket = { "apple":3, "banana":5, "cherry":50 }

c = fruitbasket.keys()
b = fruitbasket.values()
a = fruitbasket.items()

print(a, list(a))
print(b, list(b))
print(c, list(c))

#%%

fruitbasket = { "apple":3,
               "banana":5,
               "cherry":50, 
               "durian":0,
               "mango":2 }

keylist = list(fruitbasket.keys())
print(keylist)

keylist.sort()
print(keylist)

for key in keylist:
    print("{:^10}:{:>3}".format( key, fruitbasket[key] ) )

print( sum( fruitbasket.values() ) )

#%%

fruitbasket = { "apple":3, "banana":5, "cherry":50, "durian":0, "mango":2 }

apple = fruitbasket.get( "apple" )
print(apple)
if apple:
    print( "apple is in the basket" )
else:
    print( "no apples in the basket")

orange = fruitbasket.get( "orange" )
if orange:
    print( "orange is in the basket" )
else:
    print( "no oranges in the basket")

banana = fruitbasket.get( "banana", 0 )
print( "number of bananas in the basket:", banana )

strawberry = fruitbasket.get( "strawberry", 0 )
print( "number of strawberries in the basket:", strawberry )

#%%

# =============================================================================
# Exercise The code below contains a list of words
# . Build a dictionary that contains all
# these words as keys, and their quantities as values.
#  Print the words with their quantities.
# =============================================================================

wordlist = ["apple","durian","banana","durian","apple","cherry",
    "cherry","mango","apple","apple","cherry","durian","banana",
    "apple","apple","apple","apple","banana","apple"]

wordfreq = {}

for i in wordlist:
    wordfreq[i] = wordfreq.get(i, 0) +1
    # if i not in wordfreq:
    #     wordfreq[i] = 1
    #     continue
    # wordfreq[i] += 1
    
print(wordfreq)

#%%

text = "apple,durian,banana,durian,apple,cherry,cherry,mango," + \
    "apple,apple,cherry,durian,banana,apple,apple,apple," + \
    "apple,banana,apple"
    
wordfreq = {}
wordlist = text.split(sep = ",")

for word in wordlist:
    if word not in wordfreq:
        wordfreq[word] =0
    wordfreq[word] +=1

print(wordfreq)

#%%

english_dutch = { "last":"laatst", "week":"week", "the":"de",
    "royal":"koninklijk", "festival":"feest", "hall":"hal", "saw":
    "zaag", "first":"eerst", "performance":"optreden", "of":"van", 
    "a":"een", "new":"nieuw", "symphony":"symphonie", "by":"bij", 
    "one":"een", "world":"wereld", "leading":"leidend", "modern":
    "modern", "composer":"componist", "composers":"componisten", 
    "two":"twee", "shed":"schuur", "sheds":"schuren" }

sentence = "Last week The Royal Festival Hall saw the first \
performance of a new symphony by one of the world's leading \
modern composers, Arthur \"Two-Sheds\" Jackson."

translated_sentence = ""
sentence = sentence.lower()
sentence = sentence.split()

for word in sentence:
    a = english_dutch.get(word)
    if a is not None:
        translated_sentence += a + ' '
    else:
        translated_sentence += word + ' '
    
print(translated_sentence)

#%% 13.1

# =============================================================================
# Exercise 13.1 Write a program that takes a text (for instance the one 
# given below), splits it into words (where everything that is not 
# a letter is considered a word boundary), and case-insensitively builds
# a dictionary that stores for every word how often it occurs 
# in the text. Then print all the words with their quantities 
# in alphabetical order.
# =============================================================================

text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""


def clean_text(text):
    new_text = ""
    text = text.lower()
    for c in text:
        if c >= "a" and c <= "z":
            new_text += c
        else:
            new_text += " "
    return new_text

def word_count(text):
    word_freq = {}
    text = text.split()
    for word in text:
        if word not in word_freq:
            word_freq[word] = 0
        word_freq[word] += 1
    return word_freq
    
def printing(wordfreq):
    keylist = list(wordfreq.keys())
    keylist.sort()
    for key in keylist:
        print("{} : {}".format(key, wordfreq[key]))
        
printing(word_count(clean_text(text)))

#%% 13.2

# =============================================================================
# The code block below shows a list of movies. For each movie it also shows a 
# list of ratings. Convert this code in such a way that it stores all 
# this data in one dictionary, then use the dictionary to print the 
# average rating for each movie, rounded to one decimal.
# =============================================================================

movies = {  "Monty Python and the Holy Grail": 
            [ 9, 10, 9.5, 8.5, 3, 7.5,8 ],
            "Monty Python's Life of Brian": 
            [ 10, 10, 0, 9, 1, 8, 7.5, 8, 6, 9 ],
            "Monty Python's Meaning of Life": 
            [ 7, 6, 5 ],
            "And Now For Something Completely Different": 
            [ 6, 5, 6, 6 ] }

movie_list = list(movies.keys() )

for key in movie_list:
    print("{} : {:.1f}".format(key,sum(movies[key])/len(movies[key]) ))