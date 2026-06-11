def solution(participant, completion):
    players = {}
    
    for part in participant :
        players[part] = players.get(part,0) + 1
    
    for com in completion :
        players[com] -= 1
    
    for name, cnt in players.items() :
        if cnt > 0 :
            return name
        