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
    

# 소수 구하기
# 하나씩 확인해야하기 때문에 시간이 너무 많이 소요된다.
import math
def Prime(num):
    if num==1:
        return False
    
    n=int(math.sqrt(num))

    for i in range(2,n+1):
        if num%i==0:
            return False
    return True

M, N = list(map(int,input().split(' ')))
for i in range(M,N+1):
    if Prime(i) == True:
        print(i)    

# 정답
# 주어지는 값중 더 큰 값까지의 소수들을 모두 구한뒤 작은 값부터 소수를 출
M, N = list(map(int,input().split(' ')))
arr = [i for i in range(N+1)]
arr[1] = 0
for i in range(2,N+1):
    if arr[i] == 0:
        continue
    for j in range(i*2,N+1,i):
        arr[j] = 0
prime = [i for i in range(M,N+1) if arr[i] == i]

for i in prime:
    if i >= M:
        print(i)
     
        
# 베르트랑 공준
while True:
    n = int(input())
    N = 2 * n
    if n == 0 :
        break
    else :
        arr = [i for i in range(N+1)]
        arr[1] = 0
        for i in range(2,N+1):
            if arr[i] == 0:
                continue
            for j in range(i*2,N+1,i):
                arr[j] = 0
        prime = [i for i in range(n+1,N+1) if arr[i] == i]
        print(len(prime))



# 골드바흐의 추측
# 최대값인 10000까지의 소수 리스트를 우선 만들어 놓는다.
# 그 차이가 최소인 소수들만 출력해야하기 때문에 10의 경우 5+5가 최소
# 이처럼 가운데서부터 다음 소수 그다음 소수를 찾아가는 것이 문제가 원하는
# 답을 찾는 방법
# 입력값 n의 중간에서 부터 시작해서 소수 리스트의 값에 값이 있으면 그것은 소수이기
# 때문에 중간 값에서부터 차근차근 하나씩 빼가며 소수를 찾고, 그 소수를
# 입력값 n에서 뺀 값이 소수인지 판단하고 그게 참이면 출력하는 형태
# 그리고 break를 하지 않으면 최소 값이아닌 모든 조합이 출력된다.

N = 10000
arr = [i for i in range(0,N+1)]
arr[1] = 0
for i in range(2,N+1):
    if arr[i] == 0:
        continue
    for j in range(i*2,N+1,i):
        arr[j] = 0

case = int(input())
for i in range(case):
    n = int(input())
    for i in range(n//2,1,-1):
        if bool(arr[i]) :
            if bool(arr[n-i]) :
                print(i, n-i)
                break
    