from collections import defaultdict
import heapq as hq

def solution(genres, plays):
    
    songs = defaultdict(list)
    total_cnt = defaultdict(int)
    ans = []
    
    for i, cnt in enumerate(plays) :
        songs[genres[i]] += [(cnt, i)]
        total_cnt[genres[i]] += cnt
    
    # 장르 구하기
    sort_cnt = sorted(total_cnt, key = lambda x : total_cnt[x], reverse = True)
    
    # 노래 구하기
    for g in sort_cnt :
        # 주의! 재생수는 내림차순, 인덱스는 오름차순이므로 reverse = True 하면 인덱스 정렬에 문제생김!
        songs[g].sort(key=lambda x : (-x[0],x[1]))
        g_cnt = 0
        for song in songs[g] :
            ans.append(song[1])
            g_cnt += 1
            
            if g_cnt == 2 :
                break
                
    return ans
            
        

        
    
    
    
    
    
    
    
#     for i,cnt in enumerate(plays) :
#         hq.heappush(q,[-cnt, i, genres[i]])      # 최대 힙
#         # cnt_genre[genres[i]] += 1
    
    
#     while q :
#         play, num, genre = hq.heappop(q)
#         cnt_genre[genre] += 1
#         print(play,num)
#         print(cnt_genre.get(genre))
        
#         if cnt_genre.get(genre) > 2 :
#             continue
            
#         else :
#             ans.append(num)
#             print("ans:",ans)
            
        
#     return ans
        
        
    