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


# 피보나치 함수
def count_fibonacci(n):
    zero_count = [1,0]
    one_count = [0,1]
    if n <= 1:
        return
 
    for i in range(2, n+1):
        zero_count.append(zero_count[i-1] + zero_count[i-2])
        one_count.append(one_count[i-1] + one_count[i-2])
 
    return zero_count, one_count
 
n = int(input())
zero_count, one_count = count_fibonacci(40)
 
for _ in range(n):
    m = int(input())
    print("%d %d" % (zero_count[m], one_count[m]))
    
    


# 01타일
def tile001(n):
    answer = 0
    temp_1 = 1
    temp_2 = 2
    for i in range(1, n+1):
        if i == 1:
            answer = temp_1
        elif i == 2:
            answer = temp_2
        else:
            answer = temp_1 + temp_2
            temp_1 = temp_2 % 15746
            temp_2 = answer % 15746
    
    print(answer % 15746)
        
tile001(int(input()))




# 파도반 수열

t = int(input())
dp = [0 for _ in range(101)]

def wave():
    dp[1], dp[2], dp[3] = 1, 1, 1
    dp[4], dp[5] = 2, 2
    dp[6] = 3
    for i in range(7, 101):
        dp[i] = dp[i-1] + dp[i-5]
    return

for _ in range(t):
    n = int(input())
    wave()
    print(dp[n])