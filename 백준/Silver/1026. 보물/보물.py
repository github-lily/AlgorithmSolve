
N = int(input())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0

# B 인덱스와 함께 값 저장
idx_B = []

for i in range(N) :
    idx_B.append((B[i],i))

# B 오름차순 정렬
idx_B.sort(key=lambda x:x[0])


# A  내림차순 정렬(그리디)
A.sort(reverse=True)



for idx in range(N) :
    ans += A[idx] * idx_B[idx][0]

print(ans)