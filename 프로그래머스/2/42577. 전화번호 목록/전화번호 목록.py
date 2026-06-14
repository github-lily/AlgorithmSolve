def solution(phone_book):
    phone_set = set(phone_book)
    n = len(phone_book)

    for phone in phone_set :
        temp = ""
        for num in phone :
            temp += num
            if phone != temp and temp in phone_set :
                return False
    
    return True
        
        
            