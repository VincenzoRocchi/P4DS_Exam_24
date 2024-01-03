#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:12:17 2022

@author: vincenzorocchi
"""

from os import getcwd , listdir

get_path = (getcwd())
directory = (listdir())

for x in directory:
    print(get_path, x)