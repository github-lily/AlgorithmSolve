def solution(arr):
    stand = arr[0]
    lenn = len(arr)
    ans = [arr[0]]
    
    for i in range(1,lenn) :
        if stand != arr[i] :
            ans.append(arr[i])
            stand = arr[i]
    
    return ans