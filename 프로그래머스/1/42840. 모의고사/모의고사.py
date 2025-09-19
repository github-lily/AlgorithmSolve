def solution(answers):
    one = [1,2,3,4,5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    s1 = s2 = s3 = 0
    
    for i in range(len(answers)) :
        answer = answers[i]
        if one[i%5] == answer :
            s1 += 1
        if two[i%8] == answer :
            s2 += 1
        if three[i%10] == answer :
            s3 += 1

    scores = [(s1,1),(s2,2),(s3,3)]
    scores.sort(reverse=True)
    mx = scores[0][0]
    ans = [scores[0][1]]
    for idx in range(1,3) :
        if scores[idx][0] == mx :
            ans.append(scores[idx][1])
    return sorted(ans)
