#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 13:45:47 2023

@author: vincenzorocchi
"""

#%% iterators and iterable objects

#  the call fo ran iterator is iter()

x = iter(["ciao","ciao2"])

for o in x:
    print(o)
    
#%% there are three different methods of creating an iteratable obj

# the first one is using the __iter__ and __next__ call
# u can only iter on this one time because it removes element from the seq

class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
    def __iter__(self):
        return self
    def __next__(self):
        if len (self.seq) >0:
            return self.seq.pop(0)
        raise StopIteration()

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
    
#%% the other method is with __iter__ and __next__ but adding an index
# and resetting it after the iterations on the sequence ends
# and adding a reset function to reset the index variable 

class Fibo:
    def __init__( self ):
        self.seq = [1,1,2,3,5,8,13,21,34,55]
        self.index = -1
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.index < len(self.seq)-1:
            self.index += 1
            return self.seq[self.index]
        raise StopIteration
    def reset(self):
        self.index = -1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
    
fseq = Fibo()
for n in fseq:
    print( n, end=" " )
    
#%% the third and last approach is to create the iterator not as a container
# but as a call to the next item

class Fibo:
    def reset( self ):
        self.nr1 = 0
        self.nr2 = 1
    def __init__( self, maxnum=1000 ):
        self.maxnum = maxnum
        self.reset()
    def __iter__( self ):
        return self
    def __next__( self ):
        if self.nr2 > self.maxnum:
            raise StopIteration()
        nr3 = self.nr1 + self.nr2
        self.nr1 = self.nr2
        self.nr2 = nr3
        return self.nr1

fseq = Fibo()
for n in fseq:
    print( n, end=" " )
print()
fseq.reset()
for n in fseq:
    print( n, end=" " )
    
#%% 

# =============================================================================
# Create an iterator that generates all the squares of integers between 1 and 10. 
# You may choose whichever approach you prefer.
# =============================================================================

class SquaresOf:
    def __init__(self):
        self.seq = [1,2,3,4,5,6,7,8,9,10]
        self.index = -1
    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.seq)-1:
            self.index += 1
            x = self.seq[self.index]
            return x**x
        raise StopIteration()
    def reset(self):
        self.index = -1

x = SquaresOf()

for i in x:
    print(i)
    
# another way of doing it is using another object to call the iteration
# sont know how to implement it here

class SquaresOfIterable:
    def __init__(self, seq):
        self.seq = seq
    def __next__(self):
        if len(self.seq) > 1:
            return self.seq.pop() #no need of an index cause it resets automatically
        raise StopIteration()
        
class SquaresOf:
    def __init__(self):
        self.numseq = [1,2,3,4,5,6,7,8,9,10]
        self.pwrnumseq = []
    def __iter__(self):
        for i in self.numseq:
            y = i**i
            self.pwrnumseq.append(y)
            return SquaresOfIterable(self.pwrnumseq)

# works but not as intended cause it returns the list with
# the number is complicated
x = SquaresOf()

for i in x:
    print(i)    
        
#%% zip() - not solved

# =============================================================================
# Create a zip-object that produces tuples of two items: the first item is an 
# integer, which runs from 1 to 10. The second item is the square of that integer.
# =============================================================================

x =[1,2,3,4,5,6,7,8,9,10]

z = zip( x,x)

for i in z:
    print(i)
    
#%% reversed() sorted()

#%% Generators 

# using genberator is easier u just use yield on the value u want to return 
# when the iteration stops

class SquaresOf:
    def __init__(self):
        self.numseq = [1,2,3,4,5,6,7,8,9,10]
        self.pwrnumseq = []
    def __iter__(self):
        for i in self.numseq:
            y = i**i
            yield y #it just works! lmfao
            
x = SquaresOf()
for i in x:
    print(i)
    
#%% generator expression are list comprehension for generator but with
# ROUND BRACKETS the

list1 = [1,2,3,4,5,6,7,8,9,10]
y = (x**x for x in list1 if x > 3) #like this it creates a generator object
print(y, "\n")

list3 = [1,2,3,4,5,6,7,8,9,10]
y3 = [x**x for x in list3 if x > 3] #like this it creates a list object
print(y3, "\n")                           #list comprehension

list2 = [1,2,3,4,5,6,7,8,9,10] #without list comprehension
y2 = []
for x in list2:
    if x > 3:
        y2.append(x**x)
print(y2, "\n")

# The difference between a generator and a list is that generators
# create objects as needed and not all at once

for x in y:
    print(x)
#%%


