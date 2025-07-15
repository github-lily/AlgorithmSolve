import sys
from collections import Counter

text = sys.stdin.read()

counter = Counter(c for c in text if c.isalpha() and c.islower())

if counter:
    max = max(counter.values())

    for char in sorted(counter):
        if counter[char] == max:
            print(char, end='')
