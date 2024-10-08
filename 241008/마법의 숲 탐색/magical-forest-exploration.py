from collections import deque

MAX_R = 80
MAX_C = 80
MAX_K = 1005
MAX_DIR = 4

forest = [[0 for _ in range(MAX_C)] for _ in range(MAX_R)]

R, C, K = 0, 0, 0
dx = [-1,0,1,0]
dy = [0,1,0,-1]

class Golem():
    def __init__(self):
        self.id = 0
        self.dir = 0
        self.center = [0,0]
        # arms 순서는 항상 북/동/남/서
        self.arms = [[0, 0] for _ in range(MAX_DIR)]
        self.exit = [0, 0]

def update_arms(golem):
    x, y = golem.center
    for i in range(MAX_DIR):
        golem.arms[i] = [x + dx[i], y + dy[i]]
    golem.exit = [x + dx[golem.dir], y + dy[golem.dir]]

golems = [Golem() for _ in range(MAX_K)]

def inRange(x, y):
    return 0 <= x < R and 0 <= y < C

def moveDown(golem):
    for i in range(1, MAX_DIR):
        nx, ny = golem.arms[i][0] + dx[2], golem.arms[i][1] + dy[2]
        if not inRange(nx, ny) or forest[nx][ny] != 0:
            return False
    return True

def moveRight(golem):
    next_arm = [[] for _ in range(MAX_DIR)]
    for i in range(MAX_DIR):
        nx, ny = golem.arms[i][0] + dx[1], golem.arms[i][1] + dy[1]
        next_arm[i] = [nx, ny]
        if not inRange(nx, ny) or forest[nx][ny] != 0:
            return False

    for i in range(MAX_DIR):
        nx, ny = next_arm[i][0] + dx[2], next_arm[i][1] + dy[2]
        if not inRange(nx, ny) or forest[nx][ny] != 0:
            return False
    return True

def moveLeft(golem):
    next_arm = [[] for _ in range(MAX_DIR)]
    for i in range(MAX_DIR):
        nx, ny = golem.arms[i][0] + dx[3], golem.arms[i][1] + dy[3]
        next_arm[i] = [nx, ny]
        if not inRange(nx, ny) or forest[nx][ny] != 0:
            return False

    for i in range(MAX_DIR):
        nx, ny = next_arm[i][0] + dx[2], next_arm[i][1] + dy[2]
        if not inRange(nx, ny) or forest[nx][ny] != 0:
            return False
    return True

def canMove(golem):
    # 아래로 이동 가능한지 확인 - method = 1
    if moveDown(golem):
        return 1

    # 왼쪽으로 회전이 가능한지 확인 - method = 2
    if moveLeft(golem):
        return 2
    # 오른쪽으로 회전이 가능한지 확인 - method = 3
    if moveRight(golem):
        return 3
    # 모두 불가능한 경우 - method = 0
    return 0

def Move(golem, method):
    x, y = golem.center
    if method == 1:
        golem.center = [x + dx[2], y + dy[2]]

    elif method == 2:
        golem.center = [x + dx[3] + dx[2], y + dy[3] + dy[2]]
        golem.dir = (golem.dir - 1) % 4

    elif method == 3:
        golem.center = [x + dx[1] + dx[2], y + dy[1] + dy[2]]
        golem.dir = (golem.dir + 1) % 4

    update_arms(golem)

def inForest(golem):
    # center의 colum이 3 이하면 범위를 벗어난 것.
    x, y = golem.center
    return 4 <= x < R and 1 <= y < C-1

def moveElf(golem):
    visited = [[False for _ in range(C)]for _ in range(R)]
    # BFS 시작
    Q = deque()
    x, y = golem.center
    Q.append([x, y])
    visited[x][y] = True
    max_col = 0
    while Q:
        cx, cy = Q.pop()
        cur_id = forest[cx][cy]
        ex, ey = golems[cur_id].exit

        # cx, cy가 출구라면 --
        if cx == ex and cy == ey:
            for i in range(MAX_DIR):
                nx, ny = cx + dx[i], cy + dy[i]
                if inRange(nx, ny):
                    if not visited[nx][ny] and forest[nx][ny] != 0:
                        max_col = max(max_col, nx)
                        Q.append([nx, ny])
                        visited[nx][ny] = True
        # 아니라면
        else:
            for i in range(MAX_DIR):
                nx, ny = cx + dx[i], cy + dy[i]
                if inRange(nx, ny):
                    if not visited[nx][ny] and forest[nx][ny] == cur_id:
                        max_col = max(max_col, nx)
                        Q.append([nx, ny])
                        visited[nx][ny] = True

    return max_col - 2

def clearForest():
    for i in range(R):
        for j in range(C):
            forest[i][j] = 0

if __name__ == '__main__':
    R, C, K = map(int, input().split())
    R += 3 # 항상 최종 column위치에서 -2를 해줘야 하는 것을 잊지 말자.
    answer = 0
    for i in range(1,K+1):
        start_c, exit = map(int, input().split())
        golems[i].id = i
        golems[i].dir = exit
        golems[i].center = [1, start_c-1]
        update_arms(golems[i])

        # 골렘 움직이기
        while True:
            method = canMove(golems[i])
            if method == 0:
                break
            Move(golems[i], method)
        # 골렘이 움직일 수 없다면 
        # 골렘이 숲을 벗어났는지 확인
        if inForest(golems[i]):
            # forest에 id에 맞게 색칠
            for arm in golems[i].arms:
                x, y = arm
                forest[x][y] = i
                forest[golems[i].center[0]][golems[i].center[1]] = i
            # 중앙에 있는 요정 가장 아래로 내려가기
            answer += moveElf(golems[i])
        else:
            clearForest()
        # print('='*20)
        # for i in range(R):
        #     for j in range(C):
        #         print(forest[i][j], end = ' ')
        #     print()
        
    print(answer)