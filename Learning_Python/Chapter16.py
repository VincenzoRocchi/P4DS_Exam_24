#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:44:39 2022

@author: vincenzorocchi
"""

with open("ciao.txt") as ciao:
    print(ciao.read())
   
    # two different methods of opening a file, the first one
    # closes it automatically cause it's all inside an istance 
    
ciao = open('ciao.txt')
print(ciao.read())
ciao.close()

#%% in line exercise 

# =============================================================================
# Write a program that reads the lines from “pc_rose.txt,” and displays only 
# those lines that contain the word "name".
# =============================================================================

tf = open('ciao.txt')
x ="name"

while True:
    buffer = tf.readline()
    if x in buffer:
        print(buffer)
    elif buffer =="":
        break
    else:
        continue

tf.close()

#%% 

with open("ciao.txt") as ciao:
    print(ciao.read() )
    
ciao = open("ciao.txt")
print(ciao.readlines() )
ciao.close()

#%% read a limited amount of lines (2)

tf = open("ciao.txt")

count = 0
while count <5:
    buffer = tf.readline()
    print(buffer, end = "" )
    if buffer == "":
        break
    count +=1
    
#%% adapt the code above to count occurencies etc. "pc_jabberwocky"

# =============================================================================
# Adapt the code above to count how often the word “jabberwock” 
# (with any capitalization) occurs in the first 5 lines. Print 
# only the number of occurrences of that word. Once it works, remove 
# the count so that you count the number of occurrences of the word in
#  the text as a whole.
# =============================================================================

df = open("pc_jabberwocky.txt", "r") 
x = "jabberwock"
w_count = 0
count = 0

while True:
    buffer = df.readline().lower()
    if x in buffer:
        w_count += 1
    if buffer == "":
        break
    
print("{} : {}".format(x, w_count) )
df.close()

#%% 
    
    
#%% 

fp = open( "pc_writetest.tmp", "w" )
while True:
    text = input( "Please enter a line of text: " )
    if text == "":
        break
    fp.write( text + "\n")
fp.close()

fp = open( "pc_writetest.tmp" )
buffer = fp.read()
fp.close()

print( buffer )   

#%%  “pc_writetest.tmp" “pc_rose.txt"

# =============================================================================
# Write a program that reads the contents of “pc_rose.txt,” and writes exactly 
# the same contents to the file “pc_writetest.tmp.” Then open the file 
# “pc_writetest.tmp” and display the contents. You can easily construct 
# this program by cobbling together some of the code given above.
# =============================================================================

rose = open("pc_rose.txt") 
write = open("pc_writetest.txt", "w")
count = 0

while count < 10:
    buffer = rose.readlines()
    if buffer != "":
        write.writelines(reversed(buffer) )
    elif buffer == "":
        break
    count +=1 

write.close()

write = open("pc_writetest.txt")
buffer = write.readlines()
print(buffer)
write.close()

#%%

from os import listdir , getcwd ; from os.path import join
filelist = listdir( "." ) 
for name in filelist:
    pathname = join( getcwd(), name ) 
    print( pathname )
    
#%%
    
from os.path import getsize 
numbytes = getsize( "pc_rose.txt" )
print( numbytes )

#%%

# =============================================================================
# Write a program that adds up the sizes of all the files in the current 
# directory, and prints the result.
# =============================================================================
total_size = 0

filelist = listdir(".")
for name in filelist:
    size = (getsize(name))
    total_size += size
print(total_size)

#%%

from sys import getfilesystemencoding 
print( getfilesystemencoding() )

#%%

# =============================================================================
# If you want to see which special characters are supported with values in the 
# range 80-FF on your system, run the code below
# =============================================================================

for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 10, 16 ):
    print( chr( ord( 'A' )+i-10 ), end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
    
#%% Exercise 16.1

# =============================================================================
# Exercise 16.1 Write a program that reads the contents of the file “pc_woodchuck.txt,”
# splits it into words (where everything that is not a letter is considered 
# a word boundary), and case-insensitively builds a dictionary that stores for 
# every word how often it occurs in the text. Then print all the words with their 
# quantities in alphabetical order. 
# =============================================================================

tf = open("pc_woodchuck.txt", "r")
text = tf.read()
tf.close()

def clean(s):
    s = s.lower()
    news = ""
    for i in s:
        if i >= "a" and i <= "z":
            news += i
        else:
            news += " "
    return news

wordlist = clean(text).split()

worddict = {}
for word in wordlist:
    
    # worddict[word] = worddict.get( word, 0 ) + 1 #[optimal solution]
    #
    # the value for the specified key if key is in the dictionary.
    # none if the key is not found and value is not specified.
    # value if the key is not found and value is specified.
    
    if word not in worddict:
        worddict[word] = 1
    else:
        worddict[word] += 1
    
keylist = list(worddict.keys())
keylist.sort()
for key in keylist:
    print("{:<10} : {}".format(key, worddict[key]))


#%% Exercise 16.2

# =============================================================================
# Do the same thing as you did for the previous exercise, but now process the 
# text line by line. This is something that you would have to do if you had 
# to process a very long text.
# =============================================================================

def clean(s):
    s = s.lower()
    news = ""
    for i in s:
        if i >= "a" and i <= "z":
            news += i
        else:
            news += " "
    return news

tf = open("pc_woodchuck.txt", "r")

word_dict = {}

while True:
    buffer = tf.readline()
    clean_buff = clean(buffer).split()
    for word in clean_buff:
        word_dict[word] = word_dict.get(word, 0) +1
        
    if buffer == "":
        break

keylist = list(word_dict.keys())
keylist.sort()
for key in keylist:
    print("{:<10} : {}".format(key, word_dict[key]))

tf.close()
#%% Exercise 16.3 

# =============================================================================
# Write a program that processes the contents of “pc_woodchuck.txt,” line by line. 
# It creates an output file in the current working directory called 
# “pc_woodchuck.tmp,” which has the same contents as “pc_woodchuck.txt,”
# except that all the vowels are removed (case-insensitively). At the end, 
# display how many characters you read, and how many characters you wrote.
# =============================================================================

tfi = open("pc_woodchuck.txt", "r")
tfo = open("pc_woodchuck.tmp", "w")

def cleanvow(s):
    vowels = ("a","e","i","o","u")
    s = s.lower()
    news = ""
    for i in s:
        if i not in vowels:
            news += i
        # else:
        #     news += " "
    return news

countread = 0
countwritten = 0

while True:
    buffer = tfi.readline()
    countread += len(buffer)
    if buffer == "":
        break
    novow_buffer = cleanvow(buffer)
    countwritten += len(novow_buffer)
    tfo.write(novow_buffer)

print(countread)
print(countwritten)

tfi.close()
tfo.close()

#%% Exercise 16.4

# =============================================================================
# Write a program that determines how many words of 2 or more letters the files 
# “pc_woodchuck.txt,” “pc_jabberwocky.txt” and “pc_rose.txt” have in common.
# You have to treat the words case-insensitively, and, as always, any character
# that is not a letter can be treated as a word boundary. If your program is 
# correct, you will find three such words.
# =============================================================================
def clean_split(s):
    s = s.lower()
    news = ""
    for i in s:
        if i >= "a" and i <= "z":
            news += i
        else:
            news += " "
    return news.split()

files = ["pc_woodchuck.txt", "pc_rose.txt", "pc_jabberwocky.txt"]
setlist = []

for name in files:
    wordset = set()
    setlist.append(wordset)
    tf = open(name, "r")
    while True:
        line = tf.readline()
        if line == "":
            break
        cleanline = clean_split(line)
        for word in cleanline:
            if len(word) >= 2:
                wordset.add(word)
            else:
                continue
            
combination = setlist[0].copy()
i = 1
while i < len(setlist):
    combination = combination & setlist[i]
    i += 1

#%% Exercise 16.5

# =============================================================================
# For the three files that you used in the previous exercise, count for each of 
# them how often each letter (case-insensitively) occurs. Calculate for each let-
# ter and eachfile thef raction <number of occurrences of letter in the file>/<total 
# number of letters in the file>. Write an outputfile (any name, as long as you 
# can safely overwrite it) with extension .csv, that contains 26 lines, each 
# line for- matted as follows: "<letter>",<fraction for first file>,<fraction
# for second file>,<fraction for third file>. The first line should have letter
# a, the second let- ter b, etcetera. The fractions should be stored with 5 decimals.
# Finally, display the contents of the outputfile. As the outputfile is a CSV file,
# you should also be able to load it in a spreadsheet program.
# =============================================================================

def clean(s):
    s = s.lower()
    news = ""
    for i in s:
        if i >= "a" and i <= "z":
            news += i
        else:
            news += " "
    return news

files = ["pc_woodchuck.txt", "pc_rose.txt", "pc_jabberwocky.txt"]
letter_dict = {}
wordcount = []

for name in files:
    tf = open(name, "r")
    wordcount.append(count)
    letter_dict[name] = letter_dict.get(name, 0) +1
    count = 0
    while True:
        line = tf.readline()
        if line == "":
            break
        cleanline = clean(line)
        for letter in cleanline:
            letter_dict[name][letter] = letter_dict.get(letter,0) +1
            count += 1
            
print(letter_dict)   
print(wordcount)         

#%% Exercise 16.5 solution

from os.path import join
from os import getcwd

files = ["pc_jabberwocky.txt","pc_rose.txt","pc_woodchuck.txt"]
letterlist = [ len( files )*[0] for i in range( 26 ) ]
totallist = len( files ) * [0]

# Process all the input files, read their contents line by line,
# make them lower case, and keep track of the letter counts in 
# letterlist, while keeping track of total counts in totallist.
filecount = 0
for name in files:
    filename = join( getcwd(), name )
    fp = open( filename )
    while True:
        line = fp.readline()
        if line == "":
            break
        line = line.lower()
        for c in line:
            if c >= 'a' and c <= 'z':
                totallist[filecount] += 1
                letterlist[ord(c)-ord("a")][filecount] += 1
    fp.close()
    filecount += 1

# Write the counts in CSV format.
outfilename = join( getcwd(), "pc_writetest.csv" )
fp = open( outfilename, "w" )
for i in range( len( letterlist ) ):
    s = "\"{}\"".format( chr( ord("a")+i ) )
    for j in range( len( files ) ):
        s += ",{:.5f}".format( letterlist[i][j]/totallist[j] )
    fp.write( s+"\n" )
fp.close()

# Print the contents of the created output file as a check.
fp = open( outfilename )
print( fp.read() )
fp.close()