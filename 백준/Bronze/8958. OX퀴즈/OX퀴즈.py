T = int(input())
for _ in range(T) :
    result = input()
    N = len(result)

    final_score = 0
    score = 0

    for mark in result :
        if mark == 'O' :
            score += 1
            final_score += score
            
        else :
            score = 0

    print(final_score)