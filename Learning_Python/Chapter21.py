#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 23:28:42 2023

@author: vincenzorocchi
"""

#%%

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )
    def __eq__( self, p ):
        return self.x == p.x and self.y == p.y

p1 = Point( 3, 4 )
p2 = Point( 3, 4 )
p3 = p1
print( p1 is p2 )
print( p1 is p3 )
print( p1 == p2 )
print( p1 == p3 )

#%%

# =============================================================================
# In Chapter 20, a Rectangle class was defined. Add to this class operators to 
# test for equality of rectangles (two rectangles are equal if they have exactly 
# the same shape), and greater/smaller operators (a rectangle is smaller than 
# another rectangle if it has a smaller surface area). Test the new operators. 
# Note: I am a bit on the fence on whether these
# =============================================================================

from math import sqrt

class Rectangle:
    def __init__(self, w, h):
        self.h = sqrt(h**2) # can actually use abs() u dumb bastard
        self.w = sqrt(w**2) 
        
    def area(self):
        return (self.h * self.w)
    
    def circumference(self):
        return ((self.h + self.w)*2)

    def __eq__(self,r):
        return self.h == r.h and self.w == r.w
    
    def __gt__(self,r):
        return self.area() > r.area()
    
    def __lt__(self,r):
        return self.area() <r.area()
    
    def __str__(self):
        return ("h = {}, w = {}".format( self.w,self.h))
    
r1 = Rectangle(15,5)
r2 = Rectangle(10,5)

print(r2<r1)

#%%

# =============================================================================
# A Sentence is a list of words. A basic Sentence class is given below. 
# Implement __len__(), __getitem__(), __setitem__(), and __contains__() 
# methods for this class.
# =============================================================================

class Sentence:
    def __init__( self, words ):
        self.words = words
    def __repr__( self ):
        return " ".join( self.words )
    def __len__(self):
        return len(self.words)
    def __getitem__(self,key):
        return self.words[key]
    def __setitem__(self,n,value):
        self.words[n] = value
    def __contains__(self,value):
        if value in self.words:
            return True
        else:
            return False
        

s = Sentence( [ "There", "is", "only", "one", "thing", "worse", 
"than", "being", "talked", "about", 
"and", "that", "is", "not", "being", "talked", "about" ] )
print( s )
print( len( s ) )
print( s[5] )
s[5] = "better"
print( s[5] )
print( "being" in s )

#%% Exercise 21.1

SUITS = ["Hearts","Spades","Clubs","Diamonds"]
RANKS = ["2","3","4","5","6","7","8","9","10",
    "Jack","Queen","King","Ace"]

class Card:
    def __init__( self, suit, rank ):
        self.suit = suit # used as index in the SUITS list
        self.rank = rank # used as index in the RANKS list
    def __repr__( self ):
        return "({},{})".format( self.suit, self.rank )
    def __str__( self ):
        return "{} of {}".format( RANKS[self.rank], \
            SUITS[self.suit] )
    def __eq__( self, c ):
        if isinstance( c, Card ):
            return self.rank == c.rank
        return NotImplemented
    def __gt__( self, c ):
        if isinstance( c, Card ):
            return self.rank > c.rank
        return NotImplemented
    def __ge__( self, c ):
        if isinstance( c, Card ):
            return self.rank >= c.rank
        return NotImplemented
        
c5 = Card( 2, 3 )
d5 = Card( 3, 3 )
sk = Card( 1, 11 )

print(c5)   



