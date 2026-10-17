def solution(array, commands):
    answer = []

    for i, j, k in commands:
        # 배열 자르기
        sliced = array[i-1:j]

        # 오름차순 정렬
        sliced.sort()

        # k번째 숫자 저장
        answer.append(sliced[k-1])

    return answer