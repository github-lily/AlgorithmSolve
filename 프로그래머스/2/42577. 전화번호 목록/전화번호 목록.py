def solution(phone_book):    
    pset = set(phone_book)

    for phone in phone_book :
        temp = ""
        for num in phone :
            temp += num
            if temp in pset and temp != phone :
                return False
    
    return True