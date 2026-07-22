def solution(routes):
    routes.sort(key=lambda x:x[0])
    # 첫차 진출 위치에 설치하는게 가장 겹칠 가능성이 큼
    camera = routes[0][1]
    cnt = 1
    for route in routes[1:] :
        # 카메라를 만나기 전에 차가 나간다면
        if camera > route[1]:
            camera = route[1]   # 카메라 위치 이동
        # 진입 전에 카메라가 있다면
        if camera < route[0] :
            camera = route[1]   # 진출 위치에 카메라 설치
            cnt += 1
    
    return cnt
            
        
    