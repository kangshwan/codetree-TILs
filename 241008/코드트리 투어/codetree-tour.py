# 2024.10.08 18:56 시작
from heapq import heappush, heappop, heapify

MAX_N = 2005
MAX_M = 10005
INF = 100*MAX_M + 5
MAX_ID = 30005

adjMatrix = [[INF for _ in range(MAX_N)] for _ in range(MAX_N)]
costs = [INF for _ in range(MAX_N)]
N, M = 0, 0
class Product():
    def __init__(self):
        self.id = 0
        self.revenue = 0
        self.dest = 0
        self.exist = False

    def __bool__(self):
        return self.exist

products = [Product() for _ in range(MAX_ID)]

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
            for i in range(3, len(query), 3):
                u, v, w = query[i], query[i+1], query[i+2]
                adjMatrix[u][u] = 0
                adjMatrix[v][v] = 0
                
                adjMatrix[u][v] = min(adjMatrix[u][v], w)
                adjMatrix[v][u] = min(adjMatrix[v][u], w)
                
            dijkstra(0)
        elif T == 200:
            # id, revenue, dest
            productId, revenue, dest = query[1:]
            products[productId].id = productId
            products[productId].revenue = revenue
            products[productId].dest = dest
            products[productId].exist = True

        elif T == 300:
            products[query[1]].exist = False

        elif T == 400:
            best_id = -1
            best_price = -1
            for i in range(1, MAX_ID):
                if products[i]:
                    price = products[i].revenue - costs[products[i].dest]
                    if price > best_price:
                        best_id = i
                        best_price = price
                        
            if best_id != -1:
                products[best_id].exist = False

            print(best_id)
        elif T == 500:
            dijkstra(query[1])