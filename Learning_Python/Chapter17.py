#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 22:09:06 2023

@author: vincenzorocchi
"""

#%% Exceptions 


try:
    print( 3 / int( input( "Please enter a number: " ) ) )
except ZeroDivisionError:
   print("ZDE")
except ValueError:
    print("VE")
except:
    print("hi")

# Exception examples

# • ZeroDivisionError: Trying to divide by zero
# • IndexError: Trying to access a list or tuple element with an out-of-bounds index 
# • KeyError: Trying to access a dictionary element with an unknown key
# • IOError: Any error that occurs while trying to access a file
# • FileNotFoundError: Trying to open a file that does not exist for reading
# • ValueError: Error while trying to type cast a value to another value
# • TypeError: Using a value of a type that is not supported for an operation

#%%

fruitlist = ["apple", "banana", "cherry"]
try:
    num = input( "Please enter a number: " )
    if "." in num:
        num = float( num )
    else:
        num = int( num )
    print( fruitlist[num] )
except TypeError:
    print(""""{}: how to solve it: {}""".format("TyperError","list indices must be integers or slices, not float"))
except ValueError:
    print("Value Error")
except IndexError as x:
    print("IndexError")
    print(x.args)
    
#%%

try:
    fp = open("test")
    fp.close()
except IOError as ex:
    print(ex.args)

#%%

import errno

try:
    fp = open( "NotAFile" )
    fp.close()
except IOError as ex:
    if ex.args[0] == errno.ENOENT:
        print( "File not found!" )
    else:
        print( ex.args[0], ex.args[1] )

#%% Exercise 17.1

# =============================================================================
# Which exceptions can the code below raise? Extend the code to handle
# all of them in a reasonable manner.
# =============================================================================

numlist = [ 100, 101, 0, "103", 104 ]

try:
    i1 = int( input( "Give an index: " ) )
    print( "100 /", numlist[i1], "=", 100 / numlist[i1] ) 
except IndexError as ex:
    print(ex.args)   
except ValueError as ex:
    print(ex.args)  
except ZeroDivisionError as ex:
    print(ex.args)   
except TypeError as ex:
    print(ex.args)
    