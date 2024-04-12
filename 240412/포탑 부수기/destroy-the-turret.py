'''
    # 시작시간 아마 대충 6시?

    공격력이 0인 포탑: 부서진 포탑.

    STEP 1:
    1. 부서지지 않은 포탑 중 가장 약한 포탑이 공격자로 선정
    2. 공격력이 가장 낮은 포탑이 2개 이상이면, 최근 공격한 포탑이 약한포탑! 
    --> 여기서 왠지 priority queue를 쓰면 잘 될것 같은 느낌이 든다.
    3. 그런 포탑이 2개 이상이라면, 행+열 합이 가장 큰 포탑이 약한포탑.
    4. 그것도 2개 이상이면, 열 값이 가장 큰 포탑이 약한 포탑.

    Priority Queue의 인자로 (공격력, 공격시간, 행+열, 열) 순서대로 넣어서 정렬하면 될 것 같다!
    공격력을 제외한 나머지는 최근 혹은 가장 커야하기 때문에 (공격력, -공격시간, -(행+열), -열) 로 priority queue를 진행한다.

    공격자는 공격력이 1+N+M이 된다.

    STEP 2:
    가장 강한 포탑을 공격한다.
    1. 공격력이 가장 높음
    2. 공격한지 오래됨
    3. 행+열 합이 가장 작음
    4. 열이 가장 작음
    (-공격력, 공격시간, 행+열, 열) 순서대로 넣으면 된다.


    STEP 3:
    레이저공격/포탄공격
    #레이저 공격
    조건1: 부서진 포탑 지날수 없음
    조건2: 반대방향으로 나올 수 있음
    조건3: 최단경로로 공격함, 이때 최단 경로가 2개 이상이면 우/하/좌/상 순서로 경로선택
    BFS? 너낌
    결과: 공격대상은 공격자의 공격력만큼 피해. 나머지 경로에 있는 포탑은 절반(/2)의 피해

    #포탄공격
    공격대상: 공격력만큼 피해받음
    주위 8개의 방향도 피해를 입는데, 공격력의 절반만큼 피해를 입음.
    공격자는 영향을 밪지 않는다.
    가장자리에 떨어진다면 레이저처럼 반대편 격자에 영향을 미친다.

    STEP 4:
    공격력이 0 이하가 된 포탑은 부서진다.

    STEP 5:
    공격하지도 않고, 맞지도 않은 포탑은 공격력이 1씩 증가한다.

    시간제한: 1초
    STEP1의 O(NM)
    STEP2의 O(NM)
    STEP3의 O((NM)^2 + 1)
    STEP4의 O(NM)
    STEP5의 O(NM)
    STEP1~5를 K번 반복.
    즉 전체 알고리즘의 big-o: O(K*(NM)^2) ==> O(10000000) 1천만, 0.1초!

    SSAP Able이다.

    또한 애초에 포탑 개수도 100개밖에 안되기 때문에, copy-N-paste를 잘 사용해서
    해도 될 것이다!
'''
import sys
import heapq
from collections import deque
input = sys.stdin.readline

# 우/하/좌/상/우하/좌하/우상/좌상
dx = [0,1,0,-1,1,1,-1,-1]
dy = [1,0,-1,0,1,-1,1,-1]

# N, M, K 입력.
N,M,K = map(int, input().split())
board = []
broken = [[False for _ in range(M)] for _ in range(N)]
attackTime=[[-1 for _ in range(M)] for _ in range(N)]

for x in range(N):
    row = list(map(int, input().split()))
    board.append(row)

# def heapifyTower():
#     print("HEAPIFY TOWER")
#     global towers
#     new_towers = []
#     for x in range(N):
#         for y in range(M):
#             if board[x][y] != 0:
#                 new_towers.append((board[x][y], -attackTime[x][y], -(x+y), -y))
#     print(new_towers,'\n')
#     towers = new_towers
#     heapq.heapify(towers)

def select():
    at, tg = None, None
    for x in range(N):
        for y in range(M):
            if board[x][y] != 0:
                if at == None:
                    at = (x, y)
                if tg == None:
                    tg = (x, y)
                # step 1
                # Attacker 조건
                # 1. 공격력 낮은지 확인
                if board[x][y] < board[at[0]][at[1]]:
                    at = (x, y)
                elif board[x][y] == board[at[0]][at[1]]:
                    # 2. 최근에 공격했는지 확인
                    if attackTime[x][y] > attackTime[at[0]][at[1]]:
                        at = (x, y)
                    elif attackTime[x][y] == attackTime[at[0]][at[1]]:
                        # 3. 행+열 합이 큰지 확인
                        if x+y > at[0]+at[1]:
                            at = (x, y)
                        elif x+y == at[0]+at[1]:
                            # 4. 열이 가장 큰지 확인
                            if y > at[1]:
                                at = (x, y)
                #step 2
                # Target 조건
                # 1. 공격력 높은지 확인
                if board[x][y] > board[tg[0]][tg[1]]:
                    tg = (x, y)
                elif board[x][y] == board[tg[0]][tg[1]]:
                    # 2. 공격한지 오래됐는지 확인
                    if attackTime[x][y] < attackTime[tg[0]][tg[1]]:
                        tg = (x, y)
                    elif attackTime[x][y] == attackTime[tg[0]][tg[1]]:
                        # 3. 행+열 합이 작은지 확인
                        if x+y < tg[0]+tg[1]:
                            tg = (x, y)
                        elif x+y == tg[0]+tg[1]:
                            # 4. 열이 가장 작은지 확인
                            if y < tg[1]:
                                tg = (x, y)
    return at, tg

def lazerAttack(at, tg):
    # 레이저 공격 시도
    visited = [[None for _ in range(M)] for _ in range(N)]
    at_x, at_y= at
    tg_x, tg_y = tg
    power = board[at_x][at_y]
    
    # BFS로 최단 경로 탐색
    Q = deque()
    Q.append((at_x, at_y))
    
    # visited에 이전 위치를 저장하여 경로를 쫒아갈 수 있도록 구현
    visited[at_x][at_y] = (at_x, at_y)
    
    while Q:
        c_x, c_y = Q.popleft()

        for d in range(4):
            # %를 이용하여 반대로 이어지는것 구현
            n_x, n_y = (c_x + dx[d])%N, (c_y + dy[d])%M
            # 방문했거나, 부서진 포탑이면 갈 수 없음
            if visited[n_x][n_y] or board[n_x][n_y] == 0:
                continue

            visited[n_x][n_y] = (c_x, c_y)
            Q.append((n_x, n_y))

    # 경로에 있는 포탑 부수기
    if visited[tg_x][tg_y] != None:
        broken[tg_x][tg_y] = True
        board[tg_x][tg_y] -= power
        if board[tg_x][tg_y] < 0:
            board[tg_x][tg_y] = 0
        c_x, c_y = visited[tg_x][tg_y]

        while (c_x, c_y) != visited[c_x][c_y]:
            broken[c_x][c_y] = True
            board[c_x][c_y] -= power//2
            if board[c_x][c_y] < 0:
                board[c_x][c_y] = 0
            c_x, c_y = visited[c_x][c_y]
        return True
    
    return False

def cannonAttack(at, tg):
    at_x, at_y= at
    tg_x, tg_y = tg
    power = board[at_x][at_y]

    # target에 포탄 떨어뜨리기
    board[tg_x][tg_y] -= power
    if board[tg_x][tg_y] < 0:
        board[tg_x][tg_y] = 0

    # 주변 8방향에 공격 전파되기
    for d in range(8):
        n_x, n_y = (tg_x+dx[d])%N, (tg_y+dy[d])%M
        # 공격자는 피해 입지 않는다.
        if (n_x, n_y) != (at_x, at_y):
            broken[n_x][n_y] = True
            board[n_x][n_y] -= power//2
            if board[n_x][n_y] < 0:
                board[n_x][n_y] = 0

def attack(at, tg, time):
    # attack 시간 최신화
    attackTime[at[0]][at[1]] = time
    # Broken 초기화
    for x in range(N):
        for y in range(M):
            broken[x][y] = False
    # 공격 참가자들은 repair 안됨
    broken[at[0]][at[1]] = True
    broken[tg[0]][tg[1]] = True

    if lazerAttack(at, tg):
        return
    cannonAttack(at, tg)

def repair():
    for x in range(N):
        for y in range(M):
            if not broken[x][y] and board[x][y] != 0:
                board[x][y] += 1

def printall():
    for row in board:
        print(row)
    print()

for t in range(K):
    attacker, target = select()
    if attacker == target:
        break
    at_x, at_y = attacker
    # 공격력 증가
    board[at_x][at_y] += N + M
    attack(attacker, target, t)
    repair()
_, tg = select()
print(board[tg[0]][tg[1]])