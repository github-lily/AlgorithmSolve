def solution(babbling):
    ans = 0
    words = [ "aya", "ye", "woo", "ma"]
    for k in babbling :
        used = 0
        # 사용 가능 단어 한바퀴 돌면서 단어 찾기
        for word in words :
            if k.find(word) != -1 :
                used += len(word)
        # 사용한 단어 수가 전체 단어의 길이와 같다면 += 1
        if len(k) == used :
            ans += 1              
    return ans