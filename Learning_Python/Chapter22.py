#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 00:31:27 2023

@author: vincenzorocchi
"""

#%%

class Person:
    def __init__( self, firstname, lastname, age ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def __repr__( self ):
        return "{} {}".format( self.firstname, self.lastname )
    def underage( self ):
        return self.age < 18

class Student( Person ):
    pass

albert = Student( "Albert", "Applebaum", 19 )
print( albert )
print( albert.underage() )

#%% Exercise 22.1

# =============================================================================
# Below I give a Rectangle class that is created with the x and y coordinate of 
# the top-left corner, a width w, and a height h. Now create a Square class that 
# inherits as much as possible from the Rectangle class.
# =============================================================================

class Rectangle:
    def __init__( self, x, y, w, h ):
        self.x, self.y, self.w, self.h = x, y, w, h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
          self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)
    
class Square(Rectangle):
    def __init__(self, x,y,w):
        super().__init__(x,y,w,w)

s1 = Square(1,1,4)

s1.area()