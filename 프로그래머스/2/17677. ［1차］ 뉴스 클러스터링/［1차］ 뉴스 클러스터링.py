def solution(str1, str2):
    # 소문자 변환
    str1 = str1.lower()
    str2 = str2.lower()
    
    # 원소 추출
    list1 = []
    list2 = []
    
    for i in range(len(str1)-1) :
        new = str1[i] + str1[i+1]
        if new.isalpha() :
            list1.append(new)
    
    for i in range(len(str2)-1) :
        new = str2[i] + str2[i+1]
        if new.isalpha() :
            list2.append(new)

    # 모두 공집합
    if not list1 and not list2 :
        return 65536
    
    # 교집합 계산
    inter = []
    temp1 = list1.copy()        # 원본 유지되도록 : String이라 얕은복사로도 충분
    for word in list2 :
        if word in temp1 :
            inter.append(word)
            temp1.remove(word)  # 중복 방지 - 교집합 : $min(count)
            
    
    # 합집합 계산
    inter_cnt = len(inter)
    union_cnt = len(list1) + len(list2) - inter_cnt
    
    # 자카드 유사도 계산
    # 자카드 유사도 J(A, B) =  두 집합의 교집합 크기 / 두 집합의 합집합 크기
    if union_cnt == 0 :     # 0으로 못나눔
        ans = 1
    else :
        ans = inter_cnt / union_cnt
        
    return int(ans*65536)       # 소수점 버림
    