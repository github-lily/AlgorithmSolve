import sys
input = sys.stdin.readline

lst = []
for i in range(8) :
    lst.append([int(input()),i])

lst = sorted(lst, reverse=True)
scores = lst[:5]

sum_val = 0
ans_lst = []
for score in scores :
    sum_val += score[0]
    ans_lst.append(score[1]+1)


print(sum_val)
print(*sorted(ans_lst))
