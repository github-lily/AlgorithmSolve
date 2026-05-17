from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def is_yellow(time, signal):
    g, y, r = signal
    cycle = g + y + r
    
    pos = (time - 1) % cycle + 1
    
    return g < pos <= g + y

def solution(signals):
    limit = 1
    
    for signal in signals:
        cycle = sum(signal)
        limit = lcm(limit, cycle)
    
    for time in range(1, limit + 1):
        if all(is_yellow(time, signal) for signal in signals):
            return time
    
    return -1