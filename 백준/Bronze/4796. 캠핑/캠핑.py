import sys

case_num = 1
for line in sys.stdin:
    L, P, V = map(int, line.split())
    if L == 0 and P == 0 and V == 0:
        break

    full_blocks = V // P
    remain = V % P

    days = full_blocks * L + min(remain, L)
    print(f"Case {case_num}: {days}")
    case_num += 1
