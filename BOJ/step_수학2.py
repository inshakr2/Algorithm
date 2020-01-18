# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 18:06:04 2020

@author: ChangYeol
"""

# 소수 찾기
# 2 ~ n-1 의 숫자까지 나누어 지는 수가 있는지 판별 (느리다)

def Prime(n):
    if n <= 1:
        return 0
    elif n <= 3:
        return 1
    else :
        D = 0
        for i in range(2,n):
            if n % i == 0:
                D += 1
        
        if D == 0 :
            return 1
        else :
            return 0

case = int(input())
test = list(map(int,input().split(' ')))
cnt = 0
for i in test :
    cnt += Prime(i)
print(cnt)


# 소수
# 위 함수를 활용
# 미리 1 ~ 10000 까지의 소수를 찾아놓은 리스트를 만든 뒤 
# 주어진 범위에서 가져오는 것이 더 효율적으로 보인다.
def Prime(n):
    if n <= 1:
        pass
    elif n <= 3:
        return n
    else :
        D = 0
        for i in range(2,n):
            if n % i == 0:
                D += 1
        
        if D == 0 :
            return n


N = int(input())
M = int(input())
res = list()
for i in range(N, M+1):
    if bool(Prime(i)) == True:
        res.append(Prime(i))
if sum(res) != 0 :
    print(sum(res),min(res), sep='\n')
else :
    print(-1)
