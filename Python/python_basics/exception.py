# -*- coding: utf-8 -*-
"""
Created on Wed May 27 19:16:56 2020

@author: Home
"""


x = int(input("enter a number"))

print(x)

if x>100:
    raise Exception('x should not exceed 100. The value of x was: {}'.format(x))
