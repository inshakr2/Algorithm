# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 18:08:34 2020

@author: ChangYeol
"""
# N과 M 1

def sequence(stack,numbers,M):
    if len(stack)==M:
        print(*stack)
        return
    else:
        for number in numbers:
            if not number in stack:
                stack.append(number)
                sequence(stack,numbers,M)
                stack.pop()
 
a,b=map(int,input().split())
numbers=list(range(1,a+1))
stack=[]
for number in numbers:
    if not number in stack:
        stack.append(number)
        sequence(stack,numbers,b)
        stack.pop()