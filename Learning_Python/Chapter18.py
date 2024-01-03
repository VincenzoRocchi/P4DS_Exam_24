#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:54:35 2023

@author: vincenzorocchi
"""

#%%

hw1 = "Hello, world!" 
hw2 = b"Hello, world!"

print( hw1 ) ;print( hw2 )

#%% listing 1801

hw1 = "Hello, world!" 
hw2 = b"Hello, world!"

for c in hw1:
    print( c, end=" " )
print()
for c in hw1:
    print( ord( c ), end=" " ) 
print()
for c in hw2:
    print( c, end=" " )
    
#%% listing 1802

bs = bytes( [72,101,108,108,111,44,32,119,111,114,108,100,33] )
print( bs )
bch = bytes( [72] )
print( bch )
wrong = bytes( 72 )
print( wrong )

#%% listing 1803 

# cannot cast str() but need to .encode() / .decode()

hw1 = b"Hello, world!"
hw2 = hw1.decode( "utf-8" )
print( hw2 )
hw3 = hw2.encode( "utf-8" )
print( hw3 )

#%%

fp = open( "pc_rose.txt", "rb" )
for i in range( 10 ):
    buffer = fp.read( 10 )
    print( buffer )
fp.close()

#%%

from os.path import getsize

FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, "wb" )
fp.write( b"And now for something completely different...\x0A\
\x00\x00\x00\x00\xD4\xE8\xE5\xA0\xD3\xF0\xE1\xEE\xE9\xF3\xE8\xA0\
\xC9\xEE\xF1\xF5\xE9\xF3\xE9\xF4\xE9\xEF\xEE\x00\x00\x00" )
fp.close()
print( getsize( FILENAME ), "bytes written" )

#%%
FILENAME = "pc_binarytest.tmp"
fp = open( FILENAME, "rb")
while True:
    buffer = fp.readline()
    if buffer == b"":
        break
    print( buffer )
fp.close()

#%%
fp = open( "pc_binarytest.tmp", "rb" )
print( "1. Current position of the file pointer is", fp.tell() )
fp.seek( 50 )
print( "2. Current position of the file pointer is", fp.tell() )
buffer = fp.read( 23 )
print( "3. Current position of the file pointer is", fp.tell() )
fp.close()

print( buffer )
s = ""
for c in buffer:
    s += chr( c-128 )
print( "The secret words are:", s )

#%%

# =============================================================================
# Open the file “pc_binarytest.tmp” in binary “reading and writing” mode, and 
# overwrite the encoded secret words with their decoded translation. Once 
# you have closed the file, open it again in text mode, read the contents, and 
# display them. If you did it all correctly, you should see two readable lines. 
# Should you mess up the file in some way, you can always recreate it.
# =============================================================================

bf = open("pc_binarytest.tmp", "r+b")
bf.seek(50)
print(bf.tell())
encstr = bf.read(23)
bf.write(encstr)
bf.close()

bf = open("pc_binarytest.tmp", "r")

while True:
    buffer = bf.readline()
    if buffer == "":
        break
    print(buffer)

#%% Exercise 18.1

# =============================================================================# 
# Create a simple file encryption program. Open a file and read it in binary mode.
#  For each byte, if it is smaller than 128, add 128; if it is bigger than or equal
#  to 128, subtract 128. Overwrite the byte with new value. Test the program on a 
#  copy of a text file (make sure it is a copy, because you will destroy the file).
#  Check the contents of the encrypted file: they should be a mess. However, when 
#  you run the program again, the original file should be restored. If it isn’t, 
#  you have a bug in your program. Aren’t you glad you were only working on a copy?
# =============================================================================
 
def display_contents(filename):
    tf = open(filename, "rb")
    buffer = tf.read()
    return buffer

def encryption(filename):
    tf = open(filename, "r+b")
    buffer = tf.read()
    tf.seek(0)
    for c in buffer:
        if c >= 128:
            tf.write( bytes([c-128]) )
        else:
            tf.write( bytes([c+128]) )
    tf.close()

display_contents("ciao_copy.txt")
encryption("ciao_copy.txt")
display_contents("ciao_copy.txt")

# decryption
encryption("ciao_copy.txt")
display_contents("ciao_copy.txt")

#%% Exercise 18.2 

#copyed the solution hope is not on the exam

letters = "etaoinshrdlcum "
unencoded = "Hello, world!"

# Print the unencoded string, as a check.
print( unencoded, len( unencoded ) )

# Create a half-byte-list as a basis for the encoding.
halfbytelist = []
for c in unencoded:
    if c in letters:
        halfbytelist.append( letters.index( c )+1 )
    else:
        byte = ord( c )
        halfbytelist.extend( [0, int( byte/16 ), byte%16 ] )
if len( halfbytelist )%2 != 0:
    halfbytelist.append( 0 )

# Turn the half-byte-list into a byte-list.
bytelist = []
for i in range( 0, len( halfbytelist ), 2 ):
    bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )

# Turn the byte-list into a byte string and print it, as a check. 
encoded = bytes( bytelist )
print( encoded, len( encoded ) )

#%% Exercise 18.3

# copyed the solution hope is not on exam

# =============================================================================
# Write a program that asks for an input file, that must exist, and an output file,
# that should not exist. Then it asks whether you want to compress or decompress. 
# If you choose com- press, the input file is compressed using the method developed 
# above, and written as the output file. If you choose decompress, the input file 
# is decompressed under the assump- tion that it was compressed with the method 
# developed above, and written as the output file. So you should be able to get 
# the original file again by first compressing and then decompressing.
# =============================================================================

from pcinput import getString, getLetter
from os.path import exists, getsize

LETTERS = b"etaoinshrdlcum "

# Compress byte string unencoded, return the compressed version.
def compress( unencoded ):
    halfbytelist = []
    for c in unencoded:
        if c in LETTERS:
            halfbytelist.append( LETTERS.index( c )+1 )
        else:
            halfbytelist.extend( [0, int( c/16 ), c%16 ] )
    if len( halfbytelist )%2 != 0:
        halfbytelist.append( 0 )
    bytelist = []
    for i in range( 0, len( halfbytelist ), 2 ):
        bytelist.append( 16*halfbytelist[i] + halfbytelist[i+1] )
    return bytes( bytelist )

# Decompress byte string encoded, return decompressed version.
def decompress( encoded ):
    halfbytelist = []
    for c in encoded:
        halfbytelist.extend( [ int( c/16 ), c%16 ] )
    if halfbytelist[-1] == 0:
        del halfbytelist[-1]
    bytelist = []
    while len( halfbytelist ) > 0:
        num = halfbytelist.pop(0)
        if num > 0:
            bytelist.append( LETTERS[num-1] )
            continue
        num = 16*halfbytelist.pop(0) + halfbytelist.pop(0)
        bytelist.append( num )
    return bytes( bytelist )

# Ask for the input file and read its contents.
while True:
    filein = getString( "Which is the input file? " )
    if not exists( filein ):
        print( filein, "does not exist" )
        continue
    try:
        fp = open( filein, "rb" )
        buffer = fp.read()
        fp.close()
    except IOError as ex:
        print( filein, "cannot be processed, choose another" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break
    
# Ask for the output file and create it.
while True:
    fileout = getString( "Which is the output file? " )
    if exists( fileout ):
        print( fileout, "already exists" )
        continue
    try:
        fp = open( fileout, "wb" )
    except IOError as ex:
        print( fileout, "cannot be created,",
            "choose another file name" )
        print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))
        continue
    break

# Ask whether the user wants to compress or decompress.
while True:
    dc = getLetter( "Choose (C)ompress or (D)ecompress? " )
    if dc != 'C' and dc != 'D':
        print( "Please choose C or D" )
        continue
    break
    
# Compress or decompress the buffer.
if dc == 'C':
    buffer = compress( buffer )
else:
    buffer = decompress( buffer )
    
# Store the (de)compressed buffer in the output file.
try:
    fp.write( buffer )
    fp.close()
except IOError as ex:
    print( "The writing process failed" )
    print( "Error [{}]: {}".format( ex.args[0], ex.args[1] ))

# Report the sizes of input and output.
print( getsize( filein ), "bytes read" )
print( getsize( fileout ), "bytes written" )