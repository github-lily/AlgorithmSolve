import heapq as hq

def solution(genres, plays):
    songs = {}
    songs_cnt = {}
    ans = []
    
    # 곡 및 장르별 재생횟수 저장
    for idx, genre in enumerate(genres) :
        if not genre in songs :
            songs[genre] = []
            songs_cnt[genre] = 0
        hq.heappush(songs[genre], (-plays[idx], idx))
        songs_cnt[genre] += plays[idx]
    
    # 장르별 재생횟수 정렬
    sorted_cnt = sorted(songs_cnt.items(), key = lambda x : x[1], reverse=True)
    
    lenn = len(sorted_cnt)
    
    for gen,_ in sorted_cnt :
        for _ in range(2) :
            if songs[gen] :
                val, idx = hq.heappop(songs[gen])
                ans.append(idx)
        
    return ans
    