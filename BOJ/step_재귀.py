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


# 별찍기 10
# https://hydroponicglass.tistory.com/28
    # 1
    # https://has3ong.tistory.com/364
def Star(x, y, num, matrix):
    if num == 1:
        matrix[x][y] = '*'
        return

    div = num // 3
    for i in range (3):
        for j in range (3):
            if i == 1 and j == 1:
                pass
            else:
                Star(x + (i * div), y + (j * div), div, matrix)

def solution():
    matrix = [[' '] * 2201 for i in range(2201)]
    N = int(input())

    Star(0, 0, N, matrix)

    for i in range(N):
        string = ''
        for j in range(N):
            string += matrix[i][j]
        print(string)

solution()

    # 2
    # https://claude-u.tistory.com/146

def stars(n):
    matrix=[]
    for i in range(3 * len(n)):
        if i // len(n) == 1:
            matrix.append(n[i % len(n)] + " " * len(n) + n[i % len(n)])
        else:
            matrix.append(n[i % len(n)] * 3)
    return(list(matrix))

star = ["***","* *","***"]
n = int(input())
k = 0
while n != 3:
    n = int(n / 3)
    k += 1
    
for i in range(k):
    star = stars(star)
for i in star:
    print(i)
    

# 하노이 탑 이동 순서
# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-python-11729%EB%B2%88-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91-%EC%9D%B4%EB%8F%99-%EC%88%9C%EC%84%9Chanoi-top-in-python
# https://brenden.tistory.com/31
def hanoi(N, From, By, To):
    
    if N == 1:
        step.append([From,To])
    else :
        hanoi(N-1, From, To, By)
        step.append([From,To])
        hanoi(N-1, By, From, To)
        
step = []
n = int(input())
hanoi(n,1,2,3)

print(len(step))
print('\n'.join(([' '.join(str(element) for element in row) for row in step])))

