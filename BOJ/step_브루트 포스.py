# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 12:18:07 2020

@author: ChangYeol
"""

# 블랙잭
N, M = map(int,input().split(' '))
card = list(map(int,input().split(' ')))
res = set()
for i in range(N-1):
    
    pick = card[i:i+2]
    other = [x for x in card if x not in pick]
    
    for j in other:
        
        if M >= sum(pick,j) :
        
            res.add(sum(pick,j))

print(list(res)[-1])

# 반례를 못찾겠다.
# https://blog.naver.com/fhskf94kr/221383553649
# 

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()
res = 0

for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            s = card[i] + card[j] + card[k]
            if s > M:
                break
            else:
                res = max(res, s)
print(res)

# library 이용
import itertools
N, M = map(int, input().split())
card = list(map(int, input().split()))
pick = itertools.combinations(num_list, 3)

res = 0
for i in pick:
    if sum(i) <= M:
        if res < sum(i):
            res = sum(i)
print(res)



# 분해합
# 처음 작성한 코드 (실패)            
def constructor(a):
    scope = len(a) * 9
    for probe in range( int(a) - scope , int(a) + scope + 1 ):
        s = 0
        for element in str(probe):
            s += int(element)
            if probe + s == int(a):
                return probe
    return 0
constructor('')

# 수정한 코드 
def constructor(N):
    
    minimum = N - len(str(N)) * 9
    minimum = 1 if minimum < 1 else minimum
    
    for i in range(minimum, N):
        
        Sum = i
        Sum += sum(map(int,str(i)))  # 이 부분으로 2중 for문 안돌려도 됬다.
        
        if Sum == N:
            print(i)
            return
        
    print(0)
    
constructor(int(input()))

