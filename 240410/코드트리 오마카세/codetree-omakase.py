import sys
from collections import defaultdict
input = sys.stdin.readline
# L, Q 입력 받음
L, Q = map(int, input().split())
table = defaultdict(dict)
sushi_status = defaultdict(dict)
seats = defaultdict(dict)
people, total_sushi = 0, 0

# 스시를 맛있게 먹어치운다. 반환은 입력받은 name의 남은 스시 개수를 반환한다.
# index가 존재할 때 eatSushi로 들어오기 때문에, index는 반드시 존재한다.
def eatSushi(index, name, to_eat):
    global total_sushi
    available_sushi = table[name][index]
    # 현재 index에 있는 스시와 먹을(to_eat) 스시가 같은 경우
    # if available_sushi == to_eat:
    #     table[name][index] = 0
    #     total_sushi -= available_sushi
    #     to_eat -= available_sushi
    # 그렇지 않은 경우는 반드시 available이 to_eat보다 적은 경우다!
    # 문제 조건에 모든 초밥을 먹기 때문에 반드시 그렇다.
    # else:
    #     table[name][index] = 0
    #     total_sushi -= available_sushi
    #     to_eat -= available_sushi

    # 애초에 조건문이 필요가 없다! available_sushi는 반드시 to_eat보다 작거나 같다.
    # 그러니 가지고 있는 스시만큼 total에서 제외하고, to_eat에서 제외하여
    # 반환하자!
    table[name][index] = 0
    total_sushi -= available_sushi
    to_eat -= available_sushi
    sushi_status[name] -= available_sushi
    return to_eat

# index Extractor는 위치 x와 시간 t일 때 설치해야하는 index를 반환한다.
def indexExtractor(x, t):
    return (x-t)%L

# Q 만큼 반복한다. Q의 최대: 100,000
for _ in range(Q):
    order = input().split()
    # 명령어가 100인 경우, table에 초밥을 추가한다.
    if order[0] == '100':
        _, t, x, name = order
        t, x = map(int, [t, x])
        # 사람 이름을 key로 하는 dict를 만든다.
        # 해당 dict의 value는 다시 dict를 구성하는데,
        # 초밥의 위치를 key, 초밥의 개수를 value로 한다.
        try:
            table[name][indexExtractor(x, t)] += 1
            
        except:
            table[name][indexExtractor(x, t)] = 1
        try:
            sushi_status[name] += 1
        except:
            sushi_status[name] = 1
        total_sushi += 1

    # 명령어가 200인 경우, seat에 사람을 추가한다.
    elif order[0] == '200':
        _, t, x, name, n = order
        t, x, n = map(int, [t, x, n])
        # 이때 저장해야 할 것은 다음과 같다.
        # 앉은 자리/남은 먹은 개수/식사를 시작하는 자리/앉은 시각 순서로 저장한다.
        seats[name] = [x, n, indexExtractor(x, t), t]
        people += 1
    elif order[0] == '300':
        # 먹을 수 있는 사람이 있으면 먹는다 -> seats를 순회하며 먹을 것이 있는지 확인한다!
        cur_t = int(order[1])
        del_seat = []
        del_table = []
        for customer in seats.keys():
            x, n, eatStart, t = seats[customer]
            
            # t초 때 먹는 위치를 계산한다.
            eatEnd = indexExtractor(x, cur_t)

            # 그렇다면 이제 eatStart부터 eatEnd 사이동안 냠냠 먹으면 된다!
            # 하지만 회전이 덜 되서 eatEnd가 eatStart보다 작다면
            # eatEnd~eatStart 사이에 초밥이 있는지 확인하면 되고,
            # 회전이 많이 되서 eatEnd가 eatStart보다 크다면
            # 0~eatStart, eatEnd~L-1 사이에 있는 경우 먹으면 된다!
            # 있는 것은 모두 게걸스럽게 먹어버리자.
            if cur_t-t > L:
                # 한바퀴를 넘었다면
                # 있는 스시를 다 먹어치우자!    
                if sushi_status[name] != 0:
                    del_table.append(name)
                    n -= sushi_status[name]
                    total_sushi -= sushi_status[name]
                    sushi_status[name] = 0
            else:
                # 한바퀴를 넘지 않았다면, 위 eatEnd와 eatStart 조건에 맞는 eatdex만 먹는다.
                if eatEnd > eatStart:
                    for eatdex in table[customer].keys():
                        if eatdex <= eatStart or eatdex >=eatEnd:
                            n = eatSushi(eatdex, customer, n)
                else:
                    for eatdex in table[customer].keys():
                        if eatEnd <= eatdex <= eatStart:
                            n = eatSushi(eatdex, customer, n)
                # 먹어야할 스시를 다 먹었다면
            if n == 0:
                # 지우기 리스트에 저장한다. (없어도 될 것 같긴한데, loop 돌 떄 부담이 될까 두려워~)
                del_seat.append(customer)
                continue
            seats[customer] = [x, n, eatEnd, cur_t]
        for gone in del_seat:
            del seats[gone]
            people -= 1
        for empty in del_table:
            del table[empty]
        print(people, total_sushi)