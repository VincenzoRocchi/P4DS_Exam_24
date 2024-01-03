#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 14:15:55 2022

@author: vincenzorocchi
"""

# 16/11/22 - lecture (slide 13 - 24 - )

#%%

#exercise 24.1


# =============================================================================
# Create a program that can be started with zero or more numerical argu- ments.
#  If it gets presented with a non-numerical argument, the program gives an 
#  error message. If it gets presented with only numerical arguments, it adds 
#  them up and prints the sum. Test the program on the command line.
# =============================================================================

import sys

numbers = []

for i in range(len(sys.argv)):
    numbers.append(sys.argv[:i])
    
if isinstance(numbers, str):
    sys.exit(1)

if isinstance(numbers, int):
    

    