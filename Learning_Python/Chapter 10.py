#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 15:59:31 2022

@author: vincenzorocchi
"""

#%% tests

# x = "banana"

# for i in range(len(x)):
#     i = x[i]
#     print(i)
    
fruit = "orange"

print( fruit[:] )
print( fruit[0:] )
print( fruit[:6] )
print( fruit[:100])
print( fruit[:len(fruit)])
print( fruit[1:-1])
print( fruit[2], fruit[1:6] )

fruit = "orange"
print(fruit[2])
print(fruit[-3])
print(fruit[4:0:-1])

#%% in line exercises

# =============================================================================
# Exercise Write code that for a string prints the indices of all 
# of its vowels (a, e, i, o, and u). This can be done with a for 
# loop or a while loop, though the while loop is more suitable.
# =============================================================================

string = "ciao andrea"
vowels = "aeiou"

for i in range(len(string)):
    if string[i] in vowels:
        print("[{}:{}]".format(string[i], str(i)), end = " " )
        
#%% in line esercises

# =============================================================================
# Write code that uses two strings. For each character in the first 
# string that has exactly the same character at the same index in the 
# second string, you print the character and the index. Watch out that 
# you do not get an “index out of bounds” runtime error. Test it with 
# the strings "The Holy Grail" and "Life of Br
# =============================================================================

str1, str2 = "The Holy Grail" , "Life of Brian"

def comparing(str1,str2,str3 = ""):
    for i in range(len(str1)):
        for j in range(len(str2)):
            if [i] == [j]:
                if str1[i] == str2[j]:
                    str3 += "[{}:{}]".format(str1[i].upper(), str(i))
                    
    return(str3)

print(comparing("The Holy Grail" , "Life of Brian"))

#%% in line

# =============================================================================
# Exercise Write a function that takes a string as argument, and creates 
# a new string that is a copy of the argument, except that every non-letter
#  is replaced by a space (e.g., "ph@t l00t" is changed to "ph t l t").
#  To write such a function, you will start with an empty string, and 
#  traverse the characters of the argument one by one. When you encounter a
#  character that is acceptable, you add it to the new string. When it 
#  is not acceptable, you add a space to the new string. Note that you
#  can check whether a character is acceptable by simple comparisons. 
#  For example, any lower case letter can be found using the test if 
#  ch >= 'a' and ch <= 'z'
# =============================================================================

def nonletter(str1, str3 = ""):
    for i in range(len(str1)):
        if str1[i] >= "a" and str1[i] <= "z":
            str3 += str1[i]
        if not str1[i] >= "a" and str1[i] <= "z":
            str3 += " "
            
    return str3

print(nonletter("ph@t l00t"))

#%% string methods

s = " And now for something completely different \n " 
print( "["+s+"]" )
s = s.strip()
print( "["+s+"]" )
print("------------------\n")

s = "The Meaning of Life" 
print( s )
print( s.upper() )
print( s.lower() )
print("------------------\n")

s = "Humpty Dumpty sat on the wall"
print( s.find( "sat" ) )
print( s.find( "t" ) )
print( s.find( "t", 12 ) )
print( s.find( "q" ) )
print("------------------\n")

s = ' Humpty Dumpty sat on the wall '
print( s.replace( 'sat on ', 'fell off ' ) )
print("------------------\n")

s = ' Humpty Dumpty sat on the wall ' 
wordlist = s.split()
for word in wordlist:
    print( word )
    
csv = "2016,September,28,Data Processing,Tilburg University" 
values = csv.split(',')
for value in values:
    print( value )
print("------------------\n")

s = "Humpty;Dumpty;sat;on;the;wall" 
wordlist = s.split( ';' )
s = " ".join( wordlist )
print( s )

#%% in line

# =============================================================================
# Exercise In the string "How much woot would a wootchuck chuck if a wootchuck 
# could chuck woot." the word "wood" is misspelled. Use replace() 
# to replace all occur- rences of this spelling error with the correct spelling.
# =============================================================================

str1 = "How much woot would a wootchuck chuck if a wootchuck could chuck woot."
print(str1.replace("woot" , "wood"))

#%% in line 

# =============================================================================
# Display the contents of the string "Nobody expects the Spanish Inquisition!# In 
# fact, those who do expect the Spanish Inquisition..." up to, but not including, 
# the hash mark (#). Use find() to get the index of the hash mark.
# =============================================================================

str1 = """Nobody expects the Spanish Inquisition!# 
       In fact, those who do expect the Spanish Inquisition..."""

print(str1.find("#"))
print(str1[0:39])

#%% in line

# =============================================================================
# Write a program that prints a “cleaned” version of all the words in a string.
#  Everything that is not a letter should be removed and be considered a 
#  separator. All the letters should be lower case. For example, the string "
#  I'm sorry, sir." should produce four words, namely "i", "m", "sorry", and 
#  "sir". You can use the function for string cleaning which you wrote as an 
#  exercise above.
# =============================================================================

def nonletter(str1, str3 = ""):
    for i in range(len(str1)):
        if str1.casefold()[i] >= "a" and str1[i] <= "z":
            str3 += str1[i]
        if not str1[i] >= "a" and str1[i] <= "z":
            str3 += " "
    return str3

print(nonletter(" I'm sorry, sir.").split())

#%% test

print( ord( 'A' ) )
print( ord( 'a' ) )
print( chr( 65 ) )
print( chr( 97 ) )
print( "orange" < "ordinal" )
print("------------------\n")

print( "The 12th letter after g is", chr( ord( "g" )+12 ) )
print("------------------\n")

print( ' ', end='' )
for i in range(16):
    if i < 10:
        print( ' '+chr( ord( '0' )+i ), end='' )
    else:
        print( ' '+chr( ord( 'A' )+i-10 ), end='' )
print()
for i in range( 2, 8 ):
    print( i, end='' )
    for j in range( 16 ):
        c = i*16+j
        print( ' '+chr( c ), end='' )
    print()
    
print("------------------\n")

alpha = "\u0391"
for i in range( 25 ):
    print( chr( ord( alpha )+i ), end=" " )
print("\n------------------\n")
    
#%% exercise 10.1

# =============================================================================
# Count how many of each vowel (a, e, i, o, u) there are in a text string,
#  and print the count for each vowel with a single formatted string. 
#  Remember that vowels can be both lower and uppercase.
# =============================================================================
vowels = "aeiou"
str1 = """And Saint Attila raised the hand grenade up on high,
# saying, "O Lord, bless this thy hand grenade, that with it
# thou mayst blow thine enemies to tiny bits, in thy mercy." 
# And the Lord did grin. And the people did feast upon the lambs, 
# and sloths, and carp, and anchovies, and orangutans, and 
# breakfast cereals, and fruit bats, and large chu..."""

def cvow(fstr, str3 = ""):
    fstr = fstr.casefold()
    counta, counte, counti, counto, countu = 0, 0, 0, 0, 0
    for i in range(len(fstr)):
        if fstr[i] in vowels[0]:
            counta += 1 
        elif fstr[i] in vowels[1]:
            counte += 1 
        elif fstr[i] in vowels[2]:
            counti += 1
        elif fstr[i] in vowels[3]:
            counto += 1 
        elif fstr[i] in vowels[4]:
            countu += 1            
    str3 = "[a={}, e={}, i={}, o={}, u={}]".format(
        counta, counte, counti, counto, countu )
    return str3
                
print(cvow(str1))
#%% prof solution exercise 10.1

text = """And Saint Attila raised the hand grenade up on high,
saying, "O Lord, bless this thy hand grenade, that with it
thou mayst blow thine enemies to tiny bits, in thy mercy." 
And the Lord did grin. And the people did feast upon the lambs, 
and sloths, and carp, and anchovies, and orangutans, and 
breakfast cereals, and fruit bats, and large chu..."""

counta, counte, counti, counto, countu = 0, 0, 0, 0, 0
for c in text:
    if c.upper() == "A":
        counta += 1
    elif c.upper() == "E":
        counte += 1
    elif c.upper() == "I":
        counti += 1
    elif c.upper() == "O":
        counto += 1
    elif c.upper() == "U":
        countu += 1
        
print( "Counts: a={}, e={}, i={}, o={}, u={}".format( 
    counta, counte, counti, counto, countu ) )

#%% exercise 10.2

# =============================================================================
# Below is a text with several characters enclosed in square brackets [ and ].
#  Scan the text and print out all characters which are between square brackets.
# =============================================================================


text = """And sending tinted postcards of places they don't realise they haven 
' t even visited to 'All at nu[m]ber 22, weather w[on]derful, our room is 
marked with an 'X'. Wish you were here. Food very greasy but we've 
found a charming li[t]tle local place hidden awa[y ]in the back streets 
where they serve Watney ' s Red Barrel and cheese and onion cris[p]s and 
the accordionist pla[y]s "Maybe i[t]'s because I'm a Londoner"' and spending 
four days on the tarmac at Luton airport on a five-day package tour wit[h]
 n[o]thing to eat but dried Watney's sa[n]dwiches..."""
 
# =============================================================================
# HO SBAGLIATO A FARE L'ESERCIZIO
# 
# def replacement(str1):
#     for c in str1:
#         if c == "[" or "]":
#             str1 = str1.replace("[", "")
#             str1 = str1.replace("]", "")
#             str1 = str1.replace("  ", "")
#     return str1
#             
# print(replacement(text))
# 
# =============================================================================

def find_char(str1, start =0):
    while True:
        start = str1.find("[", start +1)
        if start <0:
            break
        finish = str1.find("]", start -1)
        if finish <0:
            break
        print(text[start+1:finish], end = "")
        start = finish
    print()
    
find_char(text)

# =============================================================================
# start = 0
# while True:
#     start = text.find( "[", start+1 )
#     if start < 0:
#         break
#     finish = text.find( "]", start-1 )
#     if finish < 0:
#         break
#     print( text[start+1:finish], end="" )
#     start = finish 
# print()
# =============================================================================

#%% exercise 10.3

# =============================================================================
# Exercise 10.3 Print a line of all the capital letters "A" to "Z". 
# Below it, print a line of the letters that are 13 positions in the 
# alphabet away from the letters that are above them. E.g., below the
#  "A" you print an "N", below the "B" you print an "O", etcetera. 
#  You have to consider the alphabet to be circular, i.e., after the
#  "Z", it loops back to the "A" again.
# =============================================================================

for c in range(65,91):
    print(chr(c),end = " ") 
    
print()

for c in range(65,91):    
    if c <= 77:
        print(chr((c+13)), end =" ")
    if c > 77:
        print(chr((c -13)),end = " ")
        
#%% prof solution 10.3
ch = "A"
while ch <= "Z":
    print( ch, end=" " )
    ch = chr( ord( ch )+1 )
print()

for i in range( 26 ):
    rotr13 = (i + 13)%26
    ch = chr( ord( "A" ) + rotr13 )
    print( ch, end=" " )
    print(rotr13)
    
print(rotr13)

#%% exercise 10.4

# =============================================================================
# In the text below, count how often the word “wood” occurs 
# (using pro- gram code, of course). Capitals and lower case 
# letters may both be used, and you have to consider that the word 
# “wood” should be a separate word, and not part of another word.
#  Hint: If you did the exercises from this chapter, you already 
#  developed a function that “cleans” a text. Combining that 
#  function with the split() function more or less solves the 
#  problem for you.
# =============================================================================

text = """How much wood would a woodchuck chuck If a 
woodchuck could chuck wood?
He would chuck , he would , as much as he could , 
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

text = text.casefold()
count=0

def clean_string(s, ns = ""):
    for i in range(len(s)):
        if s.casefold()[i] >= "a" and s[i] <= "z":
            ns += s[i]
        if not s[i] >= "a" and s[i] <= "z":
            ns += " "
    return ns

ex = clean_string(text)
ex = ex.split()

for word in ex:
    if word == "wood":
        count += 1
        
print("{} appears {} times".format(word,count))


#%% exercise 10.5

# =============================================================================
# Exercise 10.5 Write a program that takes a string and produces a new
#  string that con- tains the exact characters that the first string 
#  contains, but in order of their ASCII-codes. For instance, the 
#  string "Hello, world!" should be turned into " !,Hdellloorw". 
#  This is relatively easy to do with list functions, which will 
#  be introduced in a future chapter, but for now try to do it with 
#  string manipulation functions alone.
# =============================================================================

text = "hello world!"
new_text = ""

for i in range(len(text)):
    ch = text[i]
    for j in range(len(text)):
        if text[j] < ch:
            ch = text[j]
    text = text[:i] + text[i+1:]
    print(text)
    new_text += ch
    
print(new_text)

# for i in range(len(text)):
#     ch = text[i]
#     print("{}, {}".format(ch, ord(ch)))

# text = "Hello, world!"
# newtext = ""

# while len( text ) > 0:
#     i = 0
#     ch = text[i]
#     j = 1
#     while j < len( text ):
#         if text[j] < ch:
#             ch = text[j]
#             i = j
#         j += 1
#     text = text[:i] + text[i+1:]
#     newtext += ch
    
# print( newtext )

#%% exercise 10.6 

# Exercise 10.6 Typical autocorrect functions are the following: 
# (1) if a word starts with two capitals, followed by a lower-case letter,
#  the second capital is made lower case; (2) if a sentence contains a 
#  word that is immediately followed by the same word, the second 
#  occurrence is removed; (3) if a sentence starts with a lower-case 
#  letter, that letter is turned into a capital; (4) if a word 
#  consists entirely of capitals, except for the first letter which 
#  is lower case, then the case of the letters in the word is 
#  reversed; and (5) if the sentence contains the name of a day
#  (in English) which does not start with a capital, the first 
#  letter is turned into a capital. Write a program that takes 
#  a sentence and makes these auto- corrections. Test it out on the string below.

text = "as it turned out our chance meeting with REverend \
aRTHUR BElling was was to change our whole way of life, and \
every sunday we'd hurry along to St lOONY up the Cream BUn \
and Jam..."

newtext = text[0].upper() + text[1:]

wordlist = newtext.split()
for word in wordlist:
    
    if len(word) > 2:
        if word[0:1] >= "A" and word[0:1] <= "Z" and word[2] >= "a" and word[2] <= "z":
            word = word[0] + word[1].lower() + word[2:]
            
    newtext += word + " "
    lastword = word
         
print(newtext)
# text = text.split()
# print(text)

