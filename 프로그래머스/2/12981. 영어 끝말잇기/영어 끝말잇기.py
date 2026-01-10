def solution(n, words):
    used = set()
    prev = words[0][0]

    for i, w in enumerate(words):
        if w in used or w[0] != prev:
            return [i % n + 1, i // n + 1]
        used.add(w)
        prev = w[-1]

    return [0, 0]
