s = input()
result = ''

for c in s:
    if 'a' <= c <= 'z':
        result += chr((ord(c) - ord('a') + 13) % 26 + ord('a'))
    elif 'A' <= c <= 'Z':
        result += chr((ord(c) - ord('A') + 13) % 26 + ord('A'))
    else:
        result += c

print(result)
