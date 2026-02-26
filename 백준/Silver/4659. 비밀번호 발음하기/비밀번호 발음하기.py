import sys

def validate_password(pwd):
    vowels = "aeiou"
    
    if not any(char in vowels for char in pwd):
        return False

    v_count, c_count = 0, 0
    for i in range(len(pwd)):
        if i > 0 and pwd[i] == pwd[i-1]:
            if pwd[i] not in 'eo':
                return False
        
        if pwd[i] in vowels:
            v_count += 1
            c_count = 0
        else:
            c_count += 1
            v_count = 0
            
        if v_count >= 3 or c_count >= 3:
            return False
            
    return True

def solve():
    for line in sys.stdin:
        password = line.strip()
        if password == "end":
            break
            
        if validate_password(password):
            print(f"<{password}> is acceptable.")
        else:
            print(f"<{password}> is not acceptable.")

if __name__ == "__main__":
    solve()