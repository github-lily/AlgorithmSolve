def solution(arr, commands):
    ans = []
    for i,j,k in commands :
        temp = sorted(arr[i-1:j])
        ans.append(temp[k-1])
    return ans
        