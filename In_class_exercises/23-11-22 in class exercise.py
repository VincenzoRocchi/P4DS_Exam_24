#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:56:50 2022

@author: vincenzorocchi
"""

# 23/11/2022 - in class exercises

#%% 

def rec_sum(n):
    if n <= 1:
        return 1
    return n + rec_sum(n-1)

rec_sum(100)

#%% 

def rec_exp(x,n):
    if n <= 1:
        return x
    else:
        return x * rec_exp(x, n-1)

rec_exp(4,3)

#%% 

def rec_dig_count(n, i = 1):
    n = int(n)
    if n == 0:
        return 0
    else:
        return i + rec_dig_count(n/10, i)
    
rec_dig_count(14)

#%% 

def rec_dig_sum(n):
    if n == 0:
        return 0
    else:
        return (n%10 + rec_dig_sum(n/10))
    
rec_dig_sum(14)
    
#%%
def sum_of_digit( n ):
    if n == 0:
        return 0
    else:
        return (n % 10 + sum_of_digit(int(n / 10)))
    
rec_dig_count(12345)