# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 10:26:18 2020

@author: ChangYeol
"""

# 팩토리얼

def factorial(n):
    if n == 1 or n == 0:
        return 1
    
    return n * factorial(n-1)

n = int(input())
print(factorial(n))


# 피보나치 수
def fibonacci(n):
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(int(input())))