N = int(input())
nums = 1

while N > 0 :
    nums *= N
    N -= 1

nums = list(str(nums))
cnt = 0
for i in range(len(nums)-1,-1,-1) :
    if nums[i] == "0" :
        cnt += 1
    else :
        break

print(cnt)
        
            