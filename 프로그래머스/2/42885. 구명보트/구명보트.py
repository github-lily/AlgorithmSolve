# 구명보트 한 번에 최대 2명 탑승 가능
def solution(people, limit):
    people.sort()
    
    left = 0                # 가벼운 사람
    right = len(people)-1     # 무거운 사람
    boat = 0
    
    while left <= right :
        light = people[left]
        heavy = people[right]
        
        if light + heavy <= limit :
            left += 1

        right -= 1
        boat += 1
    
    return boat
    
        
        
    
    