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
