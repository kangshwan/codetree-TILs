MAX_ID = 100001
COLOR_MAX = 5

class Node:
    def __init__(self):
        self.id = 0
        self.color = 0
        self.lastUpdate = 0
        self.maxDepth = 0
        self.pId = 0
        self.childIds = []

nodes = [Node() for _ in range(MAX_ID)]
isRoot = [False] * MAX_ID

def canMakeChild(curr, needDepth):
    if curr.id == 0:
        return True
    if curr.maxDepth <= needDepth:
        return False
    return canMakeChild(nodes[curr.pId], needDepth + 1)

def getColor(curr):
    if curr.id == 0:
        return 0, 0
    info = getColor(nodes[curr.pId]) # parent의 정보
    # parent의 정보에서 lastupdate가 curr보다 작다면 --> curr보다 과거에 생성된 것.
    # parent의 정보에서 lastUpdate가 curr보다 크다면 --> parent info로 최신화
    if info[1] > curr.lastUpdate:
        return info
    else:
        return curr.color, curr.lastUpdate
    

if __name__ == "__main__":
    Q = int(input())
    for i in range(1, Q+1):
        query = list(map(int, input().split()))
        T = query[0]
        if T == 100:
            mId, pId, color, maxDepth = query[1:]

            if pId == -1:
                isRoot[mId] = True
            if isRoot[mId] or canMakeChild(nodes[pId], 1):
                nodes[mId].id = mId
                nodes[mId].color = color
                nodes[mId].lastUpdate = i
                nodes[mId].pId = pId
            
                if not isRoot[mId]:
                    nodes[pId].childIds.append(mId)
        
        elif T == 200:
            mId, color = query[1:]

            nodes[mId].color = color
            nodes[mId].lastUpdate = i
        
        elif T == 300:
            mId = query[1]
            print(getColor(nodes[mId])[0])

        elif T == 400:
            value = 0
            # for i in range(1, MAX_ID):
                # if isRoot[i]:
                    # value += getValue()