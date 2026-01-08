from math import gcd

def solution(arr):
    lcm = arr[0]
    for x in arr[1:]:
        lcm = lcm * x // gcd(lcm, x)
    return lcm
