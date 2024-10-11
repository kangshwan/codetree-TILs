class Query():
    def __init__(self, cmd, t, x, name, n):
        self.cmd = cmd
        self.t = t
        self.x = x
        self.name = name
        self.n = n
    def __repr__(self):
        if self.name != None:
            return f"Cmd: {self.cmd}, Time: {self.t}, Name: {self.name}"
        else:
            return f"Cmd: {self.cmd}, Time: {self.t}"
querys = []
L, Q = 0, 0

peopleData = {}
exit_time = {}
def updateQuerys():
    # 일단 다 앉히기
    for query in querys:
        if query.cmd == 200:
            peopleData[query.name] = [query.t, query.x, query.n]
            exit_time[query.name] = 0
    
    # 이제 초밥 언제 빠지는지 계산하기
    for i in range(Q):
        query = querys[i]
        if query.cmd == 100:
            sitTime, sitLoc, eatAmount = peopleData[query.name]
            dist = 0
            if query.t < sitTime:
                # 초밥이 먼저 만들어진 경우
                curLoc = (query.x + (sitTime - query.t))%L
                if curLoc > sitLoc:
                    dist = L - (curLoc - sitLoc)
                else:
                    dist = sitLoc - curLoc

            elif query.t > sitTime:
                # 초밥이 나중에 만들어진 경우
                curLoc = query.x
                if curLoc > sitLoc:
                    dist = L - (curLoc - sitLoc)
                else:
                    dist = sitLoc - curLoc
            eatAmount -= 1
            peopleData[query.name][2] -= 1
            querys.append(Query(101, max(sitTime, query.t) + dist, -1, query.name, -1))

            # if eatAmount == 0:
            #     querys.append(Query(202, max(sitTime, query.t) + dist, -1, query.name, -1))
            exit_time[query.name] = max(exit_time[query.name], max(sitTime, query.t) + dist)

    for name, time in exit_time.items():
        querys.append(Query(202, time, -1, name, -1))

    querys.sort(key=lambda x: (x.t, x.cmd))

if __name__ == '__main__':
    L, Q = map(int, input().split())
    for _ in range(Q):
        cmd, t, x, name, n = -1, -1, -1, None, -1

        query = input().split()
        T = int(query[0])
        if T == 100:
            t, x = map(int, query[1:3])
            name = query[3]
        elif T == 200:
            t, x = map(int, query[1:3])
            name = query[3]
            n = int(query[4])
        elif T == 300:
            t = int(query[1])
        querys.append(Query(T, t, x, name, n))

    updateQuerys()
    sushi = 0
    people = 0
    for query in querys:
        if query.cmd == 100:
            sushi += 1
        elif query.cmd == 200:
            people += 1
        elif query.cmd == 101:
            sushi -= 1
        elif query.cmd == 202:
            people -= 1
        else:
            print(people, sushi)