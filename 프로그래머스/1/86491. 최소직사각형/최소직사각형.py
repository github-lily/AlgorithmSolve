def solution(sizes):
    mx_h = 0
    mx_w = 0
    
    for card in sizes :     # 세로가 더 긴 지갑 형태
        # card[0]이 더 긴 경우
        if card[0] > card[1] :
            if mx_h < card[0] :
                mx_h = card[0]
            if mx_w < card[1] :
                mx_w = card[1]
                
        # card[1]이 더 긴 경우
        else :
            if mx_h < card[1] :
                mx_h = card[1]
            if mx_w < card[0] :
                mx_w = card[0]
                
    
    return mx_h * mx_w