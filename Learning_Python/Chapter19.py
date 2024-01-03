#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 23:35:44 2023

@author: vincenzorocchi
"""

#%%

# =============================================================================
# Write some code that calculates the decimal number represented by a binary string
# of 8 ones and zeroes. The nicest solution uses a loop, a multiplier, and a total. 
# The total starts at 0. The multiplier (which is the represented value in the 
# example above) starts at 1, and every time the loop is traversed it is multiplied
# by 2. The loop processes the string from right to left (or the reversed 
# string from left to right), and if the character encountered is a “1,” it adds
# the multiplier to a total. This will end up with the number represented by the 
# string as the total.
# =============================================================================

byte = "00000110"

def bytereading(b, total=0, multiplier=2**0):
    for i in reversed(b):
        if i == "1":
            total += multiplier
        multiplier = multiplier*2
    return total
    
bytereading(byte)

#%%

print(345%32)
print(345&31)

#%%

byte = 200
one = 1

one = one << 7

print(~ one)

#%% Exercis 19.1

# =============================================================================
# Encode a string using the bitwise exclusive or (xor) and the pattern 00101010 as 
# mask. Display the resulting string. Then decode it, and display the decoded 
# string, which should be the same as the original string.
# =============================================================================
string = "ciao"

def bytereading(b, total=0, multiplier=2**0):
    for i in reversed(b):
        if i == "1":
            total += multiplier
        multiplier = multiplier*2
    return total

# def encode(s, news =""):
#     mask = (1<<5)  #00101010
#     for c in s:
#         ex = ord(c) ^ bytereading(encode_patt)
#         print(ex)
#     return news

# encode(string)

#  solution
s = "Hello, world!"
mask = (1<<5) | (1<<3) | (1<<1)    # 00101010

code = ""
for c in s:
    code += chr(ord(c)^mask)
print( code )

decode = ""
for c in code:
    decode += chr(ord(c)^mask)
print( decode )
        
#%% Exercise 19.2

def setBit( store, index, value ):
    mask = 1<<index
    if value:
        store |= mask
    else:
        store &= ~mask
    return store

# getBit() returns 0 when the bit corresponding to index is set,
# and something else otherwise. As only 0 is interpreted as False
# this function can be used to test the value of the bit.
def getBit( store, index ):
    mask = 1<<index
    return store & mask

def displayBits( store ):
    for i in range( 8 ):
        index = 7 - i
        if getBit( store, index ):
            print( "1", end="" )
        else:
            print( "0", end="" )
    print()
    
store = 0
store = setBit( store, 0, True )
store = setBit( store, 1, True )
store = setBit( store, 2, False )
store = setBit( store, 3, True )
store = setBit( store, 4, False )
store = setBit( store, 5, True )
displayBits( store )

store = setBit( store, 1, False )
displayBits( store )