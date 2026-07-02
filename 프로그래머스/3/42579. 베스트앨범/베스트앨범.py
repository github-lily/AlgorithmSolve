import heapq as hq

def solution(genres, plays):
    cnt_dic = dict()
    song_dic = dict()
    
    # 개수와 노래 저장
    for idx, (genre, play) in enumerate(zip(genres,plays)) :
        if genre not in cnt_dic :
            cnt_dic[genre] = 0
            song_dic[genre] = []
        cnt_dic[genre] += play
        song_dic[genre].append((idx,play))
    
    # 속한 노래가 많이 재생된 장르 정렬
    sorted_genre = sorted(cnt_dic.keys(), key=lambda g : cnt_dic[g], reverse = True)
    
    ans = []
    for genre in sorted_genre :
        # 장르 내 재생 횟수, idx별 정렬
        sorted_song = sorted(song_dic[genre], key = lambda x : (x[1], -x[0]), reverse = True)
        
        for idx,play in sorted_song[:2] :
            ans.append(idx)
            
    return ans
        
