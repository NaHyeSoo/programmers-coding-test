'''
문제
준식이는 길이가 N 인 1차원 세상의 어딘가에 위치해 있고, 1차원 세상의 어딘가에 위치한 탈출구로 이동하려고 한다. 준식이는 1차원 세상에서 현재 위치한 칸에서 왼쪽 칸이나 오른쪽 칸으로 움직일 수 있다. 준식이가 가는 길에 벽이 있을 수도 있다. 준식이는 화가 많이 났기 때문에 주먹으로 최대 M 개의 벽을 부수고 지나갈 수 있다.
그런데 어느 날, 1차원 세상에 몬스터가 한 마리 떨어졌다. 준식이가 몬스터가 있는 칸으로 이동하기 위해서는 그 칸에 있는 몬스터와 싸워서 이겨야 한다.
현재 준식이의 공격력을 ATK_J , 체력을 HP_J 라고 하고, 몬스터의 공격력을 ATK_M, 체력을 HP_M 라고 하자. 준식이가 몬스터가 있는 칸으로 이동하면 전투가 시작되고, 전투는 다음과 같이 진행된다.
준식이의 현재 공격력 ATK_J 만큼 몬스터의 현재 체력 HP_M 를 깎는다.
몬스터의 체력이 0 이하이면 몬스터는 사라지고 준식이가 전투에서 이기게 된다.
몬스터의 공격력 ATK_M 만큼 준식이의 현재 체력 HP_J 를 깎는다.
준식이의 체력이 0 이하이면 준식이는 사라지고 몬스터가 전투에서 이기게 된다.
다시 1부터 진행한다.
준식이가 위치한 1차원 세상을 표현한 지도가 주어질 때 준식이는 1차원 세상을 탈출할 수 있을지 구해보자.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에 1차원 세상의 길이 N (3 ≤ N ≤ 8) 와 준식이가 벽을 부술 수 있는 최대 횟수 M (0 ≤ M ≤ N) 가 주어진다.
둘째 줄에 1차원 세상을 표현한 길이 N 짜리 문자열 S 가 주어진다.
문자열에서 @ 는 단 한 번 등장하며, 준식이를 의미한다.
문자열에서 알파벳 대문자 O 는 한 번 이상 등장하며, 준식이가 이동하려는 탈출구를 의미한다.
문자열에서 & 는 단 한 번 등장하며, 몬스터를 의미한다.
나머지 위치의 문자는 . 이거나 # 이다. . 은 빈 칸을 의미한다. 준식이는 빈 칸으로 자유롭게 이동할 수 있다. # 은 벽을 의미한다. 준식이는 벽이 있는 칸으로 이동할 수 없지만, 최대 M 개의 벽은 부술 수 있다.
셋째 줄에 초기 준식이의 공격력 ATK_J (1 ≤ ATK_J ≤ 100) 와 체력 HP_J (1 ≤ HP_J ≤ 100) 가 주어진다.
넷째 줄에 초기 몬스터의 공격력 ATK_M (1 ≤ ATK_M ≤ 100) 와 체력 HP_M (1 ≤ HP_M ≤ 100) 이 주어진다.

예제입력
4
8 1
O&#@##.O
10 10
100 11
3 0
@&O
1 1
1 1
5 0
O#@&O
2 49
1 100
8 3
O#@###&O
1 1
100 100

출력
HELP!
HAHA!
HELP!
HAHA!
'''

testcase = int(input())
ans = []

def monster(a,b,c,d):
    # a = my_atk, b = my_hp, c = mpn_atk, d = mon_hp
    # (나의 체력 - 몬스터 공격력) vs (몬스터 체력 - 나의 공격력) 
    mon_rest_hp = d - a
    my_rest_hp = b - c
    while True :
        if mon_rest_hp <= 0: return("HAHA!")  
        elif my_rest_hp <= 0: return("HELP!")  
        else :
            mon_rest_hp -= a
            my_rest_hp -= c

for _ in range(testcase):
    length,fight = map(int,input().split())
    s = input()
    my_loca = s.find("@") #해당 위치의 인덱스 반환 
    exit_loca = list(filter(lambda x : s[x] == "O", range(len(s)))) #출구는 한 번 이상 등장!
    monster_loca = s.find("&")
    my_atk, my_hp = map(int,input().split())
    mon_atk, mon_hp = map(int,input().split())

    result = []
    for j in exit_loca:
        exit_location = j
        e = max(my_loca,exit_location)
        f = min(my_loca,exit_location)
        road = s[f+1:e]

        if road.count("#") <= fight :
            if "&" in road:
                result.append(monster(my_atk, my_hp, mon_atk, mon_hp))
            else : result.append("HAHA!")    
        else : result.append("HELP!")

    if "HAHA!" in result:
        ans.append("HAHA!")
    else : ans.append("HELP!")     

for i in ans:
    print(i)
