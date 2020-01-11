# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 13:35:04 2020

@author: ChangYeol
"""

### 프로그래머스 해시 : 베스트앨범

def solution(genres, plays):
    
    import operator
    gp_list = list()
    answer = list()
    
    for i in range(len(genres)):
        c_genre = genres[i]
        c_plays = plays[i]
        if gp_list.count(c_genre) == 0:
            gp_list.append(c_genre)
            gp_list.append([c_plays])
        else :
            gp_list[gp_list.index(c_genre)+1].append(c_plays)
            
    answer_dic = dict()
    for i in range(1,len(gp_list),2):
        val = (sorted(gp_list[i], reverse = True))
        k = sum(val)
    
        answer_dic[k] = val
    
    answer_dic = sorted(answer_dic.items(), key=operator.itemgetter(1), reverse=True)
    answer_play = list()
    for i in range(len(answer_dic)):
        for j in answer_dic[i][1][:2]:
            answer_play.append(j)
    
    for i in answer_play:
        answer.append(plays.index(i))
    
    return answer