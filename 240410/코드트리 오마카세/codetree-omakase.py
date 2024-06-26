"""
"원형"의 초밥 벨트, L개의 의자.
x=0 ~ x=L-1까지.
처음에는 초밥과 의자 둘 다 비어있음 --> 초밥과 의자 list가 필요할 지도?

Ground Rule: 먼저 벨트가 회전한 뒤, 1,2,3 명령이 발생한다.
과정 1. 주방장은 시각 t에 위치 x앞에 있는 벨트 위에 name 초밥을 올려둔다.
        같은 위치에 여러 초밥이 올라갈 수 있다.
과정 2. 이름이 name인 사람이 시각 t에 위치 x에 있는 의자로 가서 앉는다.
        이때부터 위치 x 앞으로 오는 초밥 중 자신의 이름이 적힌 초밥을 정확히 n개 먹고 떠난다.
        시각 t에 x에 착석햇을 경우 바로 초밥을 먹기 시작한다.
과정 3. 오마카세 집 모습을 촬영한다.
        순서는 중요하다. 
        1. 벨트가 회전한다.
        2. 초밥을 먹는다
        3. 촬영한다.
우선...
T = 10억. 10초정도 걸리게 될 것이다.
문제의 시간제한이 15초기 때문에, T만큼 loop를 도는 방법을 우선적으로 생각할 수 있다.
하지만 여기서 Cycle Queue의 경우, L = 10억이고, 한번 벨트를 돌릴 때 10억만큼 걸리기 때문에,
엄청나게 시간이 오래걸린다.
따라서 T만큼 벨트를 회전시키면서 구현하는것은 15초인 제한조건을 만족할 수 없다.

시간을 어떻게 줄일 수 있을까?
T만큼 회전시키는 것이 아니라, t일 때 그 차이만큼 회전시키고, 그때의 차이에 맞게 초밥을 놓고
그 떄 어떤 행위를 진행한다.
Q가 10만이기 때문에, 아슬아슬...하게 될 수도 있지 않을까?
우선은 이 방법으로 진행하는것이 올바르다고 생각된다.
t=0
01234

t=1
40123
x=1에 sam 초밥 설치, x=1은 index=0, index=0에 초밥 설치.

t=2
34012
x=2에 teddy 초밥 설치, x=2는 index = 0, index=0에 초밥 설치.

t=3
23401
x=2에 june 초밥 설치, x=2는 index = 4, index=4에 초밥 설치.

t=4
12340

t=5
01234

t=6
40123
t=6일 때 촬영 찰칵. 사람 0, 초밥 3

t=7
34012
x=4인 곳에 june 착석. 2개 먹어야함. 
Eating Table은 고정으로 있고, x=4에 june 착석. t=7일 때, x=4인 경우 x-(t%L)에 해당 초밥이 있다면 먹으면 된다
4-(7%5) =4-2 => index = 2, index2에 설치된 초밥은 없다.

t=8
23401
x=3인 곳에 teddy 착석. 1개 먹어야 함.
x-(t%L) = 3-(8%5) = 3-3 = 0, index=0의 초밥 먹으면 됨. index = 0에 teddy 초밥 있으므로 냠냠, 냠냠 후 떠남.
남은 사람:june, june의 냠냠은? 4-(8%5) = 1, index=1에는 아직 요리 없음.

t=9
12340
사람 1명, 음식 2개

t=10
01234
x=3인 곳에 sam 착석, 1개 먹어야함.
x-(t%L) = 3-(10%5) = 3, index3에 음식 있나? 없음 못먹어.
남은 사람: june, june 냠냠? 4-0 = 4, index4에 june의 초밥이 있음. 잇는거 다먹어! (1개 있으므로 1개 다 냠냠, 남은 냠냠개수 1개)

t=11
40123
x=4인 곳에 june 초밥 설치.
x-(11%L) = 4-1=3, index=3에 초밥 설치.
남은사람: sam, june 하지만 index 순서대로 정렬해두자.
sam먼저.
3-1=2, index2에 요리 있? 없. 못먹어.
다음 june
4-1=3, index3에 초밥 있? 있어. 냠냠. 다먹어서 나가

t=12
34012

t=13
23401
sam 냠냠?
3-(13%5)=0, index=0에 요리 있어. 냠냠떠나.
사람 0, 초밥 0

t가 중간에 펄쩍 뛰어버리는 경우는 어떡하지?
t=13일 때 사진찍는게 아니고, t=14일때 찍는다고 하면 어떻게 해결하지?
t=14일 때 sam의 냠덱스는?
3-(14%5) = 3-4 = -1 -> 5-1=4, index가 4가됨.
이전 index가 2였기에, 2, 1, 0, 4 순서로 순회하며 냠냠할 게 있는지 확인한다
있다면 이미 냠냠하고, 떠나기에 충분하다면 이미 떠내보낸다!!
이렇게 한번 구현해보자.

sushi도 list로 관리하는 것이 아니고, dict로 관리하자!
어차피 이미 index로 관리하기 때문에, dict로 하는 것이 유리할 것이다.
"""
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

# index Extractor는 위치 x와 시간 t일 때 고정 index를 반환한다.
def indexExtractor(x, t):
    return (x-t)%L

# Q 만큼 반복한다. Q의 최대: 100,000
for _ in range(Q):
    order = input().split()
    # print(order)
    cur_t = int(order[1])
    del_seat = []
    del_table = []

    # 먹을 수 있는 사람이 있으면 먹는다 -> seats를 순회하며 먹을 것이 있는지 확인한다!
    for customer in seats.keys():
        # 최신 식사 정보를 불러온다.
        x, n, eatStart, t = seats[customer]
        
        # t일 때 x는 eatStart였다.
        eatEnd = indexExtractor(x, cur_t)
        # print(customer)
        # print(eatEnd, eatStart)
        # 그렇다면 이제 eatStart부터 eatEnd 사이동안 냠냠 먹으면 된다!
        # 하지만 회전이 덜 되서 eatEnd가 eatStart보다 작다면
        # eatEnd~eatStart 사이에 초밥이 있는지 확인하면 되고,
        # 회전이 많이 되서 eatEnd가 eatStart보다 크다면
        # 0~eatStart, eatEnd~L-1 사이에 있는 경우 먹으면 된다!
        # 있는 것은 모두 게걸스럽게 먹어버리자.
        if cur_t-t >= L:
            # 한바퀴를 넘었다면
            # 있는 스시를 다 먹어치우자!
            if sushi_status[customer] != {} and sushi_status[customer] != 0:
                del_table.append(customer)
                n -= sushi_status[customer]
                total_sushi -= sushi_status[customer]
                sushi_status[customer] = 0
        else:
            # 한바퀴를 넘지 않았다면, 위 eatEnd와 eatStart 조건에 맞는 eatdex만 먹는다.
            for eatdex in table[customer].keys():
                if eatEnd > eatStart:
                    if eatdex < eatStart or eatdex >=eatEnd:
                        n = eatSushi(eatdex, customer, n)
                elif eatEnd == eatStart:
                    if eatdex == eatEnd:
                        n = eatSushi(eatdex, customer, n)
                else:
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

        # 스시를 놓자마자 바로 먹을 수 있는지 확인

    elif order[0] == '200':
        _, t, x, name, n = order
        t, x, n = map(int, [t, x, n])
        # 이때 저장해야 할 것은 다음과 같다.
        # 앉은 자리/남은 먹은 개수/식사를 시작하는 자리/앉은 시각 순서로 저장한다.
        # seats[name] = [x, n, indexExtractor(x, t), t]
        extractIndex = indexExtractor(x, t)
        people += 1

        # 현재 위치한 index에 먹을 수 있는 초밥이 있는지 확인한다!
        for eatdex in table[name].keys():
            if eatdex == extractIndex:
                n = eatSushi(eatdex, name, n)
        if n == 0:
            people -= 1
            continue
            
        seats[name] = [x, n, extractIndex, t] 
    # if order[0]=='300'
    else:
        print(people, total_sushi)
    # print(table)
    # print(seats)
    # print()