import sys
input = sys.stdin.readline

n,m = map(int,input().split())
gcd = 0
lcm = 0

# 최소공약수(greatest common divisor)
a,b = n,m
while b != 0 :
    a,b = b, a%b
gcd = a

# 최소공배수(least common multiple)
lcm = n*m // gcd

print(gcd)
print(lcm)
