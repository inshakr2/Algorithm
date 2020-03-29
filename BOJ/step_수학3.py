# -*- coding: utf-8 -*-

# 배수와 약수

def solution(x,y) :
    if x % y == 0:
        return 'multiple'
    elif y % x == 0:
        return 'factor'
    else :
        return 'neither'

x, y = map(int,input().split(' '))

while x != 0 and y != 0:
    print(solution(x, y))
    
    x, y = map(int,input().split(' '))
    
