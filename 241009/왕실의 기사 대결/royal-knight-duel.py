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

L, N = 0, 0

def inRange(x, y):
    return 0 <= x < L and 0 <= y < L

def makeMove(id, dir):
    global knight_board
    push_list = set([])
    for x in range(L):
        for y in range(L):
            if knight_board[x][y] == id:
                print('in,',id)
                visited = [[False for _ in range(L)] for _ in range(L)]
                next_knight_board = [[0 for _ in range(L)] for _ in range(L)]
                Q = deque()
                Q.append((id, x, y))
                visited[x][y] = True
                while Q:
                    k_num, cx, cy = Q.popleft()
                    push_list.add(k_num)
                    # dir 방향으로 이동이 가능한지 확인
                    nx, ny = cx + dx[dir], cy + dy[dir]
                    if inRange(nx, ny) and board[nx][ny] != 2:
                        next_knight_board[nx][ny] = k_num
                    else:
                        #push 불가능
                        return False

                    for d in range(4):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if inRange(nx, ny) and not visited[nx][ny] and board[nx][ny] != 2 and knight_board[nx][ny] != 0:
                            Q.append((knight_board[nx][ny], nx, ny))
                            visited[nx][ny] = True
                knight_board = next_knight_board
                return True
    
def checkHurt(id):
    for x in range(L):
        for y in range(L):
            if knight_board[x][y] != 0 and knight_board[x][y] != id:
                knight_id = knight_board[x][y]
                if knights[knight_id] != 0 and board[x][y] == 1:
                    knights[knight_id] -= 1
                if knights[knight_id] == 0:
                    visited = [[False for _ in range(L)] for _ in range(L)]
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

    for i in range(L):
        for j in range(L):
            print(knight_board[i][j], end=' ')
        print()

    for _ in range(Q):
        k_num, d = map(int, input().split())
        print(k_num)
        
        if makeMove(k_num, d):
            checkHurt(k_num)
    answer = 0
    for i in range(1,N+1):
        if knights[i]:
            answer += origin_health[i] - knights[i]
    print(answer)