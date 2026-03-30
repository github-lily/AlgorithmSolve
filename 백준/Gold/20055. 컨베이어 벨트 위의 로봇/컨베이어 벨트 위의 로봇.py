
# 0. 입력값
N,K = map(int,input().split())
belt = list(map(int,input().split()))

robot = [False] * N
size = N*2
stage = 0

while True :
    stage += 1

    # 1-1. 벨트 한바퀴 회전
    temp = belt[size-1]
    for i in range(size-1,0,-1) :
        belt[i] = belt[i-1]
    belt[0] = temp

    # 1-2. 로봇 함께 회전
    for i in range(N-1, 0, -1) :
        robot[i] = robot[i-1]
    robot[0] = False        
    robot[N-1] = False      # 끝에 도착하면 로봇 빼기

    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동(이동칸에 로봇이 없고, 내구도가 1 이상일 경우에만 이동)
    for i in range(N-1, 0, -1) :
        if robot[i-1] and robot[i] == False and belt[i] > 0 :
            robot[i] = robot[i-1]
            robot[i-1] = False
            belt[i] -= 1
    
    robot[N-1] = False      # 끝에 도착하면 로봇 빼기

    # 3. 로봇 올리기 (내구도 1이상일 경우)
    if belt[0] > 0 :
        robot[0] = True
        belt[0] -= 1

    # 4. 내구도가 0인 칸의 개수가 K개 이상이면 종료, 아니면 1번으로 이동 
    if belt.count(0) >= K :
        break

print(stage)