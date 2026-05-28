def solution(phone_book):    
    pset = set(phone_book)

    for phone in phone_book :
        for i in range(1,len(phone)) :
            if phone[0:i] in pset :
                return False
        
    return True