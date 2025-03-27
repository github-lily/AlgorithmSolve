import sys
from collections import Counter

word = sys.stdin.readline().strip().upper()  # 대문자로 변환
counter = Counter(word)  # 알파벳 개수 세기

max_count = max(counter.values())  # 가장 많이 등장한 횟수 찾기
most_common = [char for char, count in counter.items() if count == max_count]  # 최다 빈도 문자 찾기

# 최다 빈도 문자가 하나면 출력, 여러 개면 '?'
print(most_common[0] if len(most_common) == 1 else '?')
