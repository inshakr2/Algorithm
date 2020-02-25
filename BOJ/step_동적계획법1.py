# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 23:15:29 2020

@author: ChangYeol
"""

# 피보나치 수 2
N = int(input())
F_0, F_1 = 0, 1
for i in range(N):
    F_0, F_1 = F_1, F_0+F_1
print(F_0)