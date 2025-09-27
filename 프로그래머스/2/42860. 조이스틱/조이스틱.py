def solution(name):
    
    N = len(name)
    char_cnt = 0
    cursor_cnt = N - 1
    
    for i,char in enumerate(name) :
        diff = ord(char) - ord('A')
        char_cnt += min(diff, 26-diff)

        j = i + 1
        while j < N  and name[j] == 'A' :
            j += 1

        cursor_cnt = min(cursor_cnt, 2*i+N-j, i + (N-j)*2)
            
    
            
    
    return char_cnt + cursor_cnt