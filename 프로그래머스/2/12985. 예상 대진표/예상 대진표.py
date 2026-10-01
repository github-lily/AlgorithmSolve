def solution(n, a, b):
    answer = 0

    while a != b:
        # 현재 참가자가 다음 라운드에서 몇 번이 되는지 계산
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer