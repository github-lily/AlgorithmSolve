import heapq as hq

def solution(genres, plays):
    # 속한 노래가 많이 재생된 장르
    # 장르 내에서 많이 재생된 노래
    # 같다면, 고유 번호가 낮은 노래 먼저
    
    # 노래 카운트
    cnt_dic  = dict()
    song_dic = dict()
    
    for i in range(len(genres)) :
        g = genres[i]
        if not g in cnt_dic :
            cnt_dic[g] = 0
            song_dic[g] = []
        cnt_dic[g] += plays[i]
        song_dic[g].append((plays[i],-i))       # 고유번호 낮은 번호 먼저
    
    # 순서 정렬
    order = []
    for gen in song_dic :
        song_dic[gen].sort(key=lambda x : (x[0], x[1]), reverse=True)
        hq.heappush(order, (-cnt_dic[gen], gen))       # 최대힙
    
    # 앨범 수록
    ans = []
    while order :
        cur_cnt, cur_gen = hq.heappop(order)
        rng = min(len(song_dic[cur_gen]),2)    # 원소가 하나일 수도 있으므로
        for i in range(rng) :
            ans.append(-song_dic[cur_gen][i][1])
    
    return ans
        
