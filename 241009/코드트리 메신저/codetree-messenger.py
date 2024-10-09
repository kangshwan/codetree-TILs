# 2024.10.09 19:18 시작
# 2024.10.09 20:48 1차 제출 - 시간초과
# 2024.10.09 21:11 2차 제출
from collections import deque

MAX_N = 100005
MAX_D = 20

class Node():
    def __init__(self):
        self.id = 0
        self.pId = -1
        self.children = []
        self.alarm = True
        self.power = 0

    def updateAlarm(self):
        self.alarm = not self.alarm
    
    def updatePower(self, power):
        self.power = power

    def updateChild(self, prev, cur):
        for i in range(len(self.children)):
            if self.children[i] == prev:
                self.children[i] = cur
                break

    def __repr__(self):
        return f"ID : {self.id}, Power: {self.power}"
rooms = [Node() for _ in range(MAX_N)]
alarm = [0 for _ in range(MAX_N)]
leafs = set()

# def updateTree():
#     global alarm
#     alarm = [0 for _ in range(MAX_N)]

#     Q = deque()
#     visited = [0 for _ in range(MAX_N)]
    
#     for leaf in leafs:
#         Q.append(leaf)

#     while Q:
#         curNode = Q.popleft()
#         visited[curNode] += 1
#         if visited[curNode] > 1:
#             continue
#         blocked = False
#         power = rooms[curNode].power
#         while power:
#             pId = rooms[curNode].pId
#             if pId == 0:
#                 break
#             if not blocked and not rooms[curNode].alarm:
#                 blocked = True

#             if not blocked:
#                 alarm[pId] += 1
#             Q.append(pId)
#             curNode = pId
#             power -= 1

def countAlarm(node):
    cnt = 0
    Q = deque()
    Q.append((1, node))
    rootRank = 1
    while Q:
        rank, curNode = Q.popleft()
        for child in rooms[curNode].children:
            childRank = rank + 1
            if not rooms[child].alarm:
                continue
            if childRank - rootRank <= rooms[child].power:
                cnt += 1
            Q.append((childRank, child))
    return cnt

if __name__ == "__main__":
    N, Q = map(int, input().split())
    leafs = set([i for i in range(0, N+1)])
    for _ in range(Q):
        query = list(map(int, input().split()))
        T = query[0]

        if T == 100:
            for idx, pId in enumerate(query[1:N+1]):
                leafs.discard(pId)
                rooms[idx+1].id = idx+1
                rooms[idx+1].pId = pId
                rooms[pId].children.append(idx+1)
            for idx, power in enumerate(query[N+1:]):
                rooms[idx+1].power = power
            # updateTree()

        elif T == 200:
            rooms[query[1]].updateAlarm()
            # updateTree()

        elif T == 300:
            rooms[query[1]].updatePower(query[2])
            # updateTree()

        elif T == 400:
            room1 = rooms[query[1]]
            room2 = rooms[query[2]]
            p_room1 = rooms[room1.pId]
            p_room2 = rooms[room2.pId]

            room1.pId, room2.pId = room2.pId, room1.pId
            p_room1.updateChild(room1.id, room2.id)
            p_room2.updateChild(room2.id, room1.id)
            # updateTree()

        elif T == 500:
            print(countAlarm(query[1]))