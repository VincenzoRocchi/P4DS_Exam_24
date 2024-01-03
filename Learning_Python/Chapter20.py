#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 18:52:58 2023

@author: vincenzorocchi
"""

#%% OBJECT ORIENTED PROGRAMMING FIRST PART

class Point:
    pass #means do nothing and leave it for latee
    
p = Point()
print(type(p))  
    
#%%

class Point():
    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        
p = Point()
print(p.x, p.y)

# you can ceate attributes outside of the __init__ function
# is not a good habit cause u dont know what objects have them 
# and which not but u can still modify them outside of the class>function

p.z = 1.1
print(p.x,p.y,p.z)

#%% __init__ can get arguments to create them when creating the object

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(1.4,1.5)

print("{} : {} ".format(p.x,p.y))

#%% trying to do a function to create a list of points , didnt work

class Point:
    def __init__ (self, x=0.0,y=0.0):
        self.x = x
        self.y = y
    
    def __repr__(self): # usually cointains every information needed to recreate obj
        return ( "x = {}, y = {}".format(self.x, self.y) )
    
# def CreatePoints():
#     i = -1
#     while i < 3:
#         i+=1
#         doti = -1
#         while doti <3:
#             doti+=1
#             point = "p" + str(i) + str(doti)
#             point = Point(i.doti,i.doti)
            
# CreatePoints() 
  
pointlist = []
for i in range(0,3):
    for j in range(4):
        point = Point(i,j)
        pointlist.append(point)

print(pointlist)

#%% __repr__ function so when u print an attributes it gives what u specified under
# the specific function

class Point():
    def __init__ ( self, x= 0.0 , y= 0.0 ):
        self.x = x
        self.y = y
    
    def __repr__(self): # usually cointains every information needed to recreate obj
        return ( "x = {}, y = {}".format(self.x, self.y) )
    
    def __str__(self): # usually to present a nice format of the more useful stuff
        return ( "x = {}, y = {}".format(self.x, self.y) )
    
p = Point(x =0.5 ,y =1.5)

print(p)

# =============================================================================
# It is commonly understood that in the __repr__() method you are supposed to 
# return a string that contains each and every bit of information that is needed 
# to recreate an object, while in __str__() you can just return a string that 
# contains a nicely formatted represen- tation of the most important information
# that you want to see in the program. Very often, these two are the same.
# =============================================================================

#%%

class Point():
    
    def __init__(self, x= 0.0, y=0.0, color = 0):
        self.x = x
        self.y = y
        self.color = color
        
    def __repr__(self):
        return ("x = 0.0, y=0.0, color = from 0 to 2**24 -1")
    
p = Point()

print(p)

#%% get / set / is 
from math import sqrt

class Point():
    
    def __init__(self, x= 0.0, y=0.0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return ( "x = {}, y = {}".format(self.x, self.y) )
    
    def distance_from_origin(self):
        return sqrt(self.x*self.x + self.y*self.y)
    
    def translate(self, shift_x , shift_y):
        self.x += shift_x
        self.y += shift_y
    
    def polar_opposite(self, minus = -1):
        self.x *= minus
        self.y *= minus
    
p = Point(3.5,-5.0)
p.distance_from_origin()
p.translate(1.3, 1.5)
print(p)
p.polar_opposite()
print(p)

#%%

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, right_point, left_point ):
        self.right_point = right_point
        self.left_point = left_point
    def __repr__( self ): 
        return "[{},{}]".format( self.right_point, self.left_point, )
    
p1 = Point(3,4)
p2 = Point(5,4)

r = Rectangle(p1,p2)
print(r)

#%%

from copy import copy

class Point:
    def __init__( self, x=0.0, y=0.0 ):
        self.x = x
        self.y = y
    def __repr__( self ):
        return "({}, {})".format( self.x, self.y )

class Rectangle:
    def __init__( self, point, width, height ):
        self.point = copy( point ) #if no copy and change point rectangle is changed
        self.width = width         #too but if u reference a copy when u create
        self.height = height       #the rect obj u do not change it
    def __repr__( self ):
        return "[{},w={},h={}]".format( self.point, self.width, 
            self.height )

p = Point( 3.5, 5.0 )
r = Rectangle( p, 4.0, 2.0 )
print( r )

p.x = 1.0
p.y = 1.0
print( r )

#%% Exercise 20.1

# =============================================================================
# Create a version of the Rectangle class that is safe by assuring that both width 
# and height are positive values (how you do that is up to you). Expand it with 
# meth- ods that calculate its surface area and its circumference. Also provide 
# a method that returns the bottom-right corner of the rectangle as a Point. Finally,
# create a method that gets a sec- ond Rectangle object as parameter, and returns 
# the overlapping area of the two rectangles as a new Rectangle object (the last 
# one is much harder than the other ones).
# =============================================================================
from math import sqrt
from copy import copy

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return ("x:{}, y:{}".format(self.x, self.y))
    
class Rectangle:
    def __init__(self, point, w, h):
        self.point = copy(point)
        self.h = sqrt(h**2)
        self.w = sqrt(w**2) 
        
    def area(self):
        return (self.h * self.w)
    
    def circumference(self):
        return ((self.h + self.w)*2)
    
    def get_right_corner(self):
        return Point(self.point.x + self.w, self.point.y)
    
    def __str__(self):
        return ("{}, h = {}, w = {}".format(self.point, self.w,self.h))

p = Point(3,4)
r = Rectangle(p, 5, 10)

print(r.area())
print(r.circumference())
print(r.get_right_corner())

#%%

# =============================================================================
# A student has a last name, a first name, a date of birth (either a year, month, 
# and day, or a datetime object if you took the liberty of studying the datetime 
# module already), and an administration number. A course has a name and a number. 
# Students can enroll in courses. Create a class Student and a class Course. Create 
# several students and several courses. Enroll each student in some of the courses. 
# Display a list of students, showing their number, first name, last name, and age, 
# and per student which courses he or she is enrolled in.
# =============================================================================
from random import randint

class Course:
    def __init__(self, course_name, course_number):
        self.course_name = course_name
        self.course_number = course_number
        
    def __repr__(self):
        return ("\"{}\" and the course number is {}".format(
            self.course_name, self.course_number))

class Students:
    def __init__(self, first_name, administration_number):
        self.first_name = first_name
        self.administration_number = administration_number
        self.enrolled_courses = []
        
    def __repr__(self):
        return ("the name of the student is:\"{}\" the\
                administration number is: {} and the enrolled courses are: {}".format(self.first_name,
                self.administration_number, self.enrolled_courses))
    
    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            
students = []
courses = []

# creating courses list
course_list = ["math","geo","phis","ita","eng"]
i = 0
for j in course_list:
    i += 10
    courses.append(Course(j, i))

# creating students list
name_list = ["vero","gianna","flavio","fabio"]
administration_number = []
x = 0
for j in range(4):
    x = randint(1,100000)
    administration_number.append(x)
    
for j in range(4):
    students.append(Students(name_list[j], administration_number[j]))
    
for stud in students:
    for cours in courses:
        stud.enroll(cours)
        

for j in students:
    print("{}{}{}".format(j.first_name,j.administration_number,j.enrolled_courses))