from collections import deque
MAX_K = 15
MAX_M = 305
BOARD_SIZE = 5
DIR = 8

K, M = 0, 0
rotation = [90, 180, 270]
# → ↘ ↓ .... ↗
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]

board = [[]for _ in range(BOARD_SIZE)]
wall = []
wallIndex = 0
def inRange(x, y):
    return 0 <= x < BOARD_SIZE and 0 <= y < BOARD_SIZE

def bfs(board):
    visited = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    Q = deque()
    total_piece = 0
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if not visited[x][y] and board[x][y] > 0:
                used = [[False for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
                piece = 1
                Q.append((board[x][y], x, y))
                visited[x][y] = True
                used[x][y] = True
                while Q:
                    num, cx, cy = Q.popleft()
                    for d in range(0, DIR, 2):
                        nx, ny = cx + dx[d], cy + dy[d]
                        if inRange(nx, ny) and not visited[nx][ny] and board[nx][ny] == num:
                            Q.append((num, nx, ny))
                            visited[nx][ny] = True
                            used[nx][ny] = True
                            piece += 1
                if piece >= 3:
                    total_piece += piece
                    for i in range(BOARD_SIZE):
                        for j in range(BOARD_SIZE):
                            if used[i][j]:
                                board[i][j] = 0
    return total_piece, board

def rotate(x, y, rot, board):
    grid=[[0 for _ in range(3)] for _ in range(3)]
    for d in range(DIR):
        grid[1 + dx[d]][1 + dy[d]] = board[x + dx[d]][y + dy[d]]
    grid[1][1] = board[x][y]

    if rot == 90:
        for d in range(DIR):
            board[x + dx[d]][y + dy[d]] = grid[1 + dx[(d-2)%DIR]][1 + dy[(d-2)%DIR]]
    elif rot == 180:
        for d in range(DIR):
            board[x + dx[d]][y + dy[d]] = grid[1 + dx[(d-4)%DIR]][1 + dy[(d-4)%DIR]]
    elif rot == 270:
        for d in range(DIR):
            board[x + dx[d]][y + dy[d]] = grid[1 + dx[(d-6)%DIR]][1 + dy[(d-6)%DIR]]
    
    total_piece, board = bfs(board)
    return total_piece, board
    
def copyBoard():
    newBoard = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            newBoard[i][j] = board[i][j]
    return newBoard

def findBest():
    global board
    best_val = 0
    best_loc = [0, 0]
    best_rot = 0
    best_board = []
    for x in range(1, 4):
        for y in range(1, 4):
            for rot in rotation:
                newBoard = copyBoard()

                val, tmp_board = rotate(x, y, rot, newBoard)
                # check is best!
                if val > best_val:
                    best_val = val
                    best_loc = [x, y]
                    best_rot = rot
                    best_board = tmp_board
                elif val == best_val:
                    if rot < best_rot:
                        best_val = val
                        best_loc = [x, y]
                        best_rot = rot
                        best_board = tmp_board
                    elif rot == best_rot:
                        if y < best_loc[1]:
                            best_val = val
                            best_loc = [x, y]
                            best_rot = rot
                            best_board = tmp_board
                        elif y == best_loc[1]:
                            if x < best_loc[0]:
                                best_val = val
                                best_loc = [x, y]
                                best_rot = rot
                                best_board = tmp_board
                            
    board = best_board
    return best_val

def fillIn():
    global wallIndex
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE-1, -1, -1):
            if board[x][y] == 0:
                board[x][y] = wall[wallIndex]
                wallIndex += 1

def digTreasure():
    global board
    # First find rotate
    treasure_val = findBest()
    if treasure_val == 0:
        return 0

    while(True):
        fillIn()
        val, board = bfs(board)
        if val != 0:
            treasure_val += val
        else:
            break
    
    return treasure_val
    


if __name__ == '__main__':
    K, M = map(int, input().split())
    for i in range(BOARD_SIZE):
        row = list(map(int, input().split()))
        board[i] = row
    wall = list(map(int, input().split()))

    for _ in range(K):
        treasure = digTreasure()
        if treasure != 0:
            print(treasure, end = ' ')
        else:
            break