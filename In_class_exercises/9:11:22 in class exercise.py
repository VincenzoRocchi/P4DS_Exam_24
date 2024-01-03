#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:48:04 2022

@author: vincenzorocchi
"""

#slide

# %% 

# EX1: Write a Python program to compute the difference between two lists.

list1 = ["red", "orange", "green", "blue", "white"]
list2 = ["black", "yellow", "green", "blue"]

l1_dif = set(list1).difference(set(list2))
l2_dif = set(list2).difference(set(list1))

print(l2_dif, l1_dif)

#%%

# EX2: Write a Python program to insert a given string at the beginning 
# of all items in a list.

list1 = [1,2,3,4]
str1 =  "emp"

# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

list3 = []
for items in list1:
    list3.append(str1 + str(items))
    
print(list3)
    
#%%

# EX3: Write a Python program to combine two dictionary adding values 
# for common keys. Go to the editor

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}


# =============================================================================
# SUBOPTIMAL
# 
# for j in d1:
#      if j in d2:
#          d2[j] = d1[j] + d2[j]
#      else:
#          d2[j] = d1[j]
#         
#  print(d2)
# =============================================================================

k1 = list(d1.keys())
k2 = list(d2.keys())

for key in set(k1+k2):
    d3[key] = d2.get(key, 0) + d1.get(key, 0)
          
print(d3)

# Sample output: 
# Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

#%%

# EX4: Write a Python program to copy the contents of 
# a file to another file

#prof solution

with open("test.txt","r") as f1:
    with open("test2.txt", "w") as f2:
        content = f1.read()
        f2.write(content)

# optimal solution for big files

with open("test.txt","r") as f1:
    with open("test2.txt", "w") as f2:
        while True:
            content = f1.read(100)
            if len(content) == 0:
                break
            #or if content == ""
            f2.write(content)
        
                     
# using the with statement caus it auto invoces the close method

#%%

# EX5: Write a Python program to remove newline characters from a file.

with open("test.txt","r") as f1:
    with open("test2.txt", "w") as f2:
        content = f1.read()
        f2.write(content.replace("\n",""))
        

        

