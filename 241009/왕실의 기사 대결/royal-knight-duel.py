#2024.10.09 08:58 시작
from collections import deque
MAX_L = 45
MAX_N = 30

dx=[-1,0,1,0]
dy=[0,1,0,-1]


board = []
knight_board = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]
origin_health = [0 for _ in range(MAX_N)]
knights = [0 for _ in range(MAX_N)]
pushed = [False for _ in range(MAX_N)]
L, N = 0, 0

def inRange(x, y):
    return 0 <= x < L and 0 <= y < L

def push(x, y, dir):
    # print(f"Push DIR: {dir}")
    push_list = deque()
    push_list.append((knight_board[x][y], x, y))
    next_knight_board = [[0 for _ in range(L)] for _ in range(L)]

    while push_list:
        visited = [[False for _ in range(L)] for _ in range(L)]
        id, x, y = push_list.popleft()
        if visited[x][y]:
            continue
        # print((id, x, y))
        Q = deque()
        Q.append((id, x, y))
        visited[x][y] = True
        # print("INTO QUEUE")
        while Q:
            k_num, cx, cy = Q.popleft()
            pushed[k_num]=True
            # print((k_num, cx, cy))
            for d in range(4):
                nx, ny = cx + dx[d], cy + dy[d]
                # print(nx, ny)
                # 범위 밖, 방문함, 벽인 경우는 무시
                if not inRange(nx, ny):
                    # print("NOT IN RANGE")
                    if d == dir:
                        return False
                    continue

                if board[nx][ny] == 2:
                    # print("WALL")
                    if d == dir:
                        # print("CANT MOVE")
                        return False
                    continue

                

                # push하는 방향이라면
                if d == dir:
                    # next_knight_board 업데이트
                    next_knight_board[nx][ny] = id
                    # push한 위치에 다른 기사가 있다면
                    if knight_board[nx][ny] != 0 and knight_board[nx][ny] != id:
                        if not visited[nx][ny]:
                            push_list.append((knight_board[nx][ny], nx, ny))
                    # push한 위치가 벽이라면
                    if board[nx][ny] == 2:
                        return False
                
                if visited[nx][ny]:
                    # print("VISITED")
                    continue

                if knight_board[nx][ny] == id:
                    Q.append((knight_board[nx][ny], nx, ny))
                    visited[nx][ny] = True

    for i in range(L):
        for j in range(L):
            if pushed[knight_board[i][j]]:
                knight_board[i][j] = 0

    for i in range(L):
        for j in range(L):
            if next_knight_board[i][j] != 0:
                knight_board[i][j] = next_knight_board[i][j]

    return True

def makeMove(id, dir):
    global knight_board, pushed
    for i in range(N+1):
        pushed[i] = False

    for x in range(L):
        for y in range(L):
            if knight_board[x][y] == id:
                return push(x, y, dir)


def checkHurt(id):
    visited = [[False for _ in range(L)] for _ in range(L)]
    for x in range(L):
        for y in range(L):
            if knight_board[x][y] != 0 and knight_board[x][y] != id:
                knight_id = knight_board[x][y]
                if not pushed[knight_id]:
                    continue
                if knights[knight_id] != 0 and board[x][y] == 1:
                    knights[knight_id] -= 1
                if knights[knight_id] == 0:
                    Q = deque()
                    Q.append((x, y))
                    visited[x][y] = True
                    knight_board[x][y] = 0
                    while Q:
                        cx, cy = Q.popleft()
                        for d in range(4):
                            nx, ny = cx + dx[d], cy + dy[d]
                            if inRange(nx, ny) and not visited[nx][ny] and knight_board[nx][ny] == knight_id:
                                visited[nx][ny] = True
                                knight_board[nx][ny] = 0
                                Q.append((nx, ny))

def printBoard():
    print('='*10)
    for i in range(L):
        for j in range(L):
            print(knight_board[i][j], end=' ')
        print()
    print('='*10)

if __name__=='__main__':
    L, N, Q = map(int, input().split())
    for _ in range(L):
        board.append(list(map(int, input().split())))

    for i in range(1, N+1):
        r, c, h, w, k = map(int, input().split())
        knights[i] = k
        origin_health[i] = k
        r -= 1; c -= 1
        for x in range(h):
            for y in range(w):
                knight_board[r + x][c + y] = i
    # printBoard()
    for _ in range(Q):
        k_num, d = map(int, input().split())
        if knights[k_num] and makeMove(k_num, d):
            checkHurt(k_num)
            # printBoard()
    answer = 0
    for i in range(1,N+1):
        if knights[i]:
            answer += origin_health[i] - knights[i]
    print(answer)