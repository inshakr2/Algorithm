# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:35:04 2020

@author: ChangYeol
"""

### 프로그래머스 해시 : 베스트앨범

def solution(genres, plays):
    
    # 장르 순으로 정렬
    # 각 장르별 재생 횟수로 정렬
    # -> 각 인덱스 공통으로 사용
    
    hash_dic = dict()
    answer = list()
    for idx, genre in enumerate(genres) :
        if genre not in hash_dic.keys() :
            hash_dic[genre] = {'total' : plays[idx], idx : plays[idx]}

        else :
            hash_dic[genre]['total'] += plays[idx]
            hash_dic[genre][idx] = plays[idx]        


    sorted_hash_dic = sorted(hash_dic.items(), key = lambda x : x[1]['total'], reverse = True)

    for i in range(len(sorted_hash_dic)):

        tmp_dic = sorted_hash_dic[i][1]
        sorted_play_list = sorted(tmp_dic.items(), key = lambda x : x[1], reverse = True)

        dur = 1
        while dur <= 2:
            answer.append(sorted_play_list[dur][0])

            if len(sorted_play_list) < 3:
                break
            dur += 1

    return answer
