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
input = sys.stdin.readline
L, Q = map(int, input().split())
sushi = {}
table = {}
people, total_sushi = 0, 0

def indexExtractor(x, t):
    return (x-(t%L))%L

def eatsushi(index, name, to_eat):
    global total_sushi, people
    # 해당 index에 스시 먹을 수 있다면
    # print(index, name, to_eat)
    try:
        available_sushi = sushi[index][name]
        if available_sushi == to_eat:
            del sushi[index][name]
            del table[name]
            to_eat -= available_sushi
            total_sushi -= available_sushi
            people -= 1
        elif available_sushi < to_eat:
            del sushi[index][name]
            to_eat -= available_sushi
            total_sushi -= available_sushi
        
        # 해당 index 위에 스시가 없다면
        if len(sushi[index].keys()) == 0:
            del sushi[index]
    except:
        pass
    return to_eat

for _ in range(Q):
    order = input().split()
    cur_t = int(order[1])
    if order[0] == '100':
        # 초밥을 만드는 경우
        num, cur_t, x, name = order
        cur_t,x = map(int, [cur_t,x])
        # 해당 위치에 이미 초밥이 있는지 확인
        try:
            sushi[indexExtractor(x, cur_t)]
        except:
            sushi[indexExtractor(x, cur_t)] = {}
        try:
            # 해당 위치에 맞는 사람의 초밥을 추가한다.
            sushi[indexExtractor(x, cur_t)][name] += 1
        except:
            # 그 자리에 초밥이 없었으면, 초밥을 생성한다.
            sushi[indexExtractor(x, cur_t)][name] = 1
        # 전체 스시 카운트 출력
        total_sushi += 1
    # 일단 t일 때 모두 식사한 뒤, 남은 사람을 출력하면 된다!
    else:
        if order[0] == '200':
            # 사람이 착석하는 경우
            num, cur_t, x, name, to_eat = order
            cur_t, x, to_eat = map(int, [cur_t, x, to_eat])
            # 일단 착석시킨다.앉은자리/남은먹을개수/앉은시각/먹은(을)index 로 저장하자.
            table[name] = [x, to_eat, cur_t, indexExtractor(x, cur_t)]
            # 전체 사람 추가
            people += 1
    # 모든 table의 사람들을 순회하며, 먹을 수 있는 초밥이 있었는지 확인한다!
    # t시간이 많이 지났을 수도 있기 때문에, 여기에도 주의하자.
    # print(table.keys())
    for customer in table.keys():
        # print(customer)
        seat, left, eaten_t, eatenIndex = table[customer]
        cur_eatdex = indexExtractor(seat, cur_t)
        # eatenIndex: 2, cur_eatdex: 4 2,1,0,4 순으로 순회할 수 있게 어떡할까?
        if cur_t - eaten_t < L:
            while eatenIndex != cur_eatdex:
                left = eatsushi(eatenIndex, customer, left)
                if left == 0:
                    break
                eatenIndex = (eatenIndex-1)%L
            left = eatsushi(eatenIndex, customer, left)
            # print(left)
            if left == 0:
                break
        else:
            for idx in range(L):
                left = eatsushi(idx, customer, left)
                if left == 0:
                    break
            if left == 0:
                break
        
        table[customer] = [seat, left, cur_t, cur_eatdex]
    # print("="*30)
    # print(table)
    # print(sushi)
    # print(table.keys())
    if order[0] == '300':
        print(people, total_sushi)