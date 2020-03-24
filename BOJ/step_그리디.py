# -*- coding: utf-8 -*-

# 동전 0

N, K = map(int, input().split()) 
value_list = [] 

for _ in range(N): 
    value = int(input()) 
    
    if value <= K: 
        value_list.append(value) 
        
cnt = 0 
for i in range(len(value_list)): 
    value = value_list[(len(value_list))-i-1] 
    cnt += (K // value) 
    K = K%value 
    
print(cnt)

# ATM

N = int(input())
nums = list(map(int, input().split()))

if N == 1 : #1
    print(nums[0])
else : 
    nums.sort() #2

    i_sum = 0 
    min_sum = 0

    for i in range(N): 
        min_sum += (i_sum + nums[i]) #3
        i_sum += nums[i] #4
        
    print(min_sum)