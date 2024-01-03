#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 15:16:01 2022

@author: vincenzorocchi
"""

#14/11/2022 lecture(slide 13)

#%% exercise 22.1

class Rectangle:
    def __init__( self, x, y, w, h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
            self.w, self.h )
    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*(self.w + self.h)
    
# solution = 

class Square(Rectangle):
    def __init__(self, x, y, w):
        super().__init__( x, y, w, w )
        
quad = Square(2,2,5)

print(quad.area())
print(quad.circumference())

#%% exercise 22.2

from math import pi

class Shape:
    
    def __init__ (self, x,y):
        self.x , self.y = x,y
    
    def area ( self):
        raise NotImplementedError
    
    def circumference ( self):
        raise NotImplementedError
    
class Rectangle(Shape):
    
    def __init__( self, x, y, w, h ):
        super().__init__(x,y)
        self.w, self.h = h,w
        
    def __repr__( self ):
        return "[({},{}),w={},h={}]".format( self.x, self.y, 
            self.w, self.h )
    
    def area( self ):
        return self.w * self.h
    
    def circumference( self ):
        return 2*(self.w + self.h)

class Circle(Shape):
    
    def __init__( self, x, y, r):
        super().__init__(x,y)
        self.r = x,y,r        
    def __repr__ ( self):
        return ["({},{}), r = {}".format(self.x, self.y, self.r)]
    def area ( self):
        return self.r * self.r * pi
    
class Square(Rectangle):
    def __init__(self, x, y, w):
        super().__init__( x, y, w, w )
