# 16:12 시작
# 밥먹고 온시각 기록 못했다... 약 17:30에 나가서 19:11에 들어옴 19:31 잠시 외출
from collections import deque

MAX_N = 50
MAX_M = 1000
MAX_P = 33
MAX_C = 50
MAX_D = 50
MAX_DIR = 8
N, M, P, C, D = 0, 0, 0, 0, 0
# 2, 1 2, 3
# 루돌프는  r이 큰것부터, c가 큰것부터 이동함.
# ↘ ↓ ↙ → ← ↗ ↑ ↖ 순서.
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
# 여기서 산타의 이동방향은 상, 우, 하, 좌
# 6, 3, 4, 1 순서로 움직인다
santa_move = [6,3,4,1]

isStun = [False for _ in range(MAX_P)]
isLive = [False for _ in range(MAX_P)]
santaLoc = [(0,0) for _ in range(MAX_P)]
santaCnt = 0
# 0: empty, n: santa, 50: rudolph
board = [[0 for _ in range(MAX_N)]for _ in range(MAX_N)]

ruLoc = (0, 0)
santaScore = 0

def inRange(x, y):
    return 0 <= x < N and 0 <= y < N

def moveRudolph():
    global ruLoc, santaScore, board
    visited = [[False for _ in range(N)] for _ in range(N)]

    x, y = ruLoc
    Q = deque()
    Q.append((0, x, y))
    visited[x][y] = True

    foundSanta = []
    minDist = 0
    while Q:
        dist, cx, cy = Q.popleft()
        if foundSanta and dist >= minDist:
            continue

        for d in range(MAX_DIR):
            nx, ny = cx + dx[d], cy + dy[d]
            if inRange(nx, ny) and not visited[nx][ny]:
                Q.append((dist + 1, nx, ny))
                visited[nx][ny] = True

                if board[nx][ny] > 0:
                    foundSanta.append(board[nx][ny])
                    minDist = dist + 1

    print(foundSanta)
    nearX, nearY = santaLoc[foundSanta[0]]
    thatSanta = foundSanta[0]

    for i in range(1, len(foundSanta)):
        santa = foundSanta[i]
        sanLoc = santaLoc[santa]
        if nearX < sanLoc[0]:
            nearX, nearY = sanLoc
            thatSanta = santa
        elif nearX == sanLoc[0]:
            if nearY < sanLoc[1]:
                nearX, nearY = sanLoc
                thatSanta = santa

    # santa를 찾은 상태. 찾지 못했으면 나올 수 없다!
    # 가장 가까운 산타의 위치
    neardx = 1 if nearX - x > 0 else (-1 if nearX - x < 0 else 0) 
    neardy = 1 if nearY - y > 0 else (-1 if nearY - y < 0 else 0) 
    
    ru_nx, ru_ny = x + neardx, y + neardy
    ruLoc = (ru_nx, ru_ny)

    nextRudolph = board[ru_nx][ru_ny]
    if nextRudolph != 0:
        santaScore += C

        isStun[nextRudolph] = True
        hitLoc = santaLoc[nextRudolph]
        nx, ny = hitLoc[0] + neardx*C, hitLoc[1] + neardy*C 
        santaLoc[nextRudolph] = (nx, ny)
        # 연쇄작용
        while inRange(nx, ny) and board[nx][ny] != 0:
            nextRudolph = board[nx][ny]
            hitLoc = santaLoc[nextRudolph]
            nx, ny = hitLoc[0] + neardx, hitLoc[1] + neardy
            santaLoc[nextRudolph] = (nx, ny)

        if not inRange(nx, ny):
            isLive[nextRudolph] = False

    new_board = [[0 for _ in range(MAX_N)] for _ in range(MAX_N)]
    new_board[ru_nx][ru_ny] = 50
    for p in range(1, P+1):
        if isLive[p]:
            new_board[santaLoc[p][0]][santaLoc[p][1]] = p
    board = new_board

def moveSanta():
    pass

def simulate():
    printBoard()
    # move Rudolph 안에는 충돌 로직이 있다.
    moveRudolph()
    # move Santa 안에는 충돌 로직이 있다.
    moveSanta()
    
def printBoard():
    print('='*20)
    for x in range(N):
        for y in range(N):
            if board[x][y] == 50:
                print('R', end=' ')
            else:
                print(board[x][y], end=' ')
        print()
if __name__ == '__main__':
    N, M, P, C, D = map(int, input().split())
    santaCnt = P

    x, y = map(int, input().split())
    ruLoc = (x-1, y-1)
    board[x-1][y-1] = 50
    for _ in range(P):
        n, x, y = map(int, input().split())
        x, y = x-1, y-1
        isLive[n] = True
        santaLoc[n] = (x, y)
        board[x][y] = n

    for _ in range(M):
        simulate()
    
    printBoard()