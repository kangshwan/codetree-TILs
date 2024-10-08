# 2024.10.08 18:56 시작

from heapq import heappush, heappop, heapify

MAX_N = 2005
MAX_M = 10005
INF = 100*MAX_M + 5
MAX_ID = 30005

adjMatrix = [[INF for _ in range(MAX_N)] for _ in range(MAX_N)]
costs = [INF for _ in range(MAX_N)]
isMade = [False] * MAX_ID
isCancel = [False] * MAX_ID

N, M = 0, 0
class Product():
    def __init__(self):
        self.id = 0
        self.revenue = 0
        self.dest = 0
        self.cost = 0

    def __lt__(self, obj):
        if self.cost == obj.cost:
            return self.id < obj.id
        return self.cost > obj.cost

products = []

def dijkstra(start):
    for i in range(N):
        costs[i] = INF
        

    visited = [False] * N
    costs[start] = 0

    min_heap = []
    # weight, vertex
    heappush(min_heap, (0, start))
    while min_heap:
        weight, v = heappop(min_heap)
        if visited[v]:
            continue

        visited[v] = True
        for u in range(N):
            if adjMatrix[v][u] != INF:
                costs[u] = min(costs[u], weight + adjMatrix[v][u])
                heappush(min_heap, (costs[u], u))

if __name__ == '__main__':
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))
        T = query[0]
        if T == 100:
            N, M = query[1:3]
            for i in range(N):
                adjMatrix[i][i] = 0

            for i in range(3, len(query), 3):
                u, v, w = query[i], query[i+1], query[i+2]

                adjMatrix[u][v] = min(adjMatrix[u][v], w)
                adjMatrix[v][u] = min(adjMatrix[v][u], w)
                
            dijkstra(0)
        elif T == 200:
            # id, revenue, dest
            productId, revenue, dest = query[1:]
            isMade[productId] = True

            product = Product()
            product.id = productId
            product.revenue = revenue
            product.dest = dest
            product.cost = revenue - costs[dest]
            # heappush
            heappush(products, product)

        elif T == 300:
            targetId = query[1]
            if isMade[targetId]:
                isCancel[targetId] = True
        elif T == 400:
            # 판매를 한큐에 끝내야됨. 무지 많기 때문!

            while products:
                best_product = products[0]

                if best_product.cost < 0:
                    print(-1)
                    break

                heappop(products)
                if not isCancel[best_product.id]:
                    print(best_product.id)
                    break
            else:
                print(-1)

        elif T == 500:
            dijkstra(query[1])
            tmp_products = []
            while products:
                product = heappop(products)
                product.cost = product.revenue - costs[product.dest]
                heappush(tmp_products, product)
            products = tmp_products