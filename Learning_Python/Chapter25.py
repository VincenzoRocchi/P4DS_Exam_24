#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 15:39:12 2023

@author: vincenzorocchi
"""

#%%

import re
mlist = re.finditer(r"([Bb])a+","A sheep says ' baaaaah ' to Ali Baba.") 
for m in mlist:
    print( "{} is found at {}.".format(m.group(), m.start()))
