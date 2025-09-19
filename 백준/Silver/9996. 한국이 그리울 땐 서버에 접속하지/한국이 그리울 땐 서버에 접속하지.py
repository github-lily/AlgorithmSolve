N = int(input())
pattern = input().strip()

idx = pattern.find("*")
start_pattern = pattern[:idx]
end_pattern = pattern[idx+1:]
e = len(end_pattern)


for _ in range(N) :
    text = input().strip()
    if len(text) < len(pattern)-1 :
        print("NE")
    elif text[:idx] == start_pattern and text[-len(end_pattern):] == end_pattern :
        print("DA")
    else :
        print("NE") 