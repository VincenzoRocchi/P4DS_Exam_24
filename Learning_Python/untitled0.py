#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 01:39:44 2023

@author: vincenzorocchi
"""

#%% 

triplelist = [ (x,y,z) for x in range( 1, 5 )
for y in range( 1, 5 ) for z in range( 1, 5 ) if x != y if x != z if y != z]
print( triplelist )
