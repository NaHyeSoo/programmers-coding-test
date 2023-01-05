'''
준식이는 길이가 N 인 1차원 세상의 어딘가에 위치해 있고, 1차원 세상의 어딘가에 위치한 탈출구로 이동하려고 한다. 
준식이는 1차원 세상에서 현재 위치한 칸에서 왼쪽 칸이나 오른쪽 칸으로 움직일 수 있다. 
준식이가 가는 길에 벽이 있을 수도 있다. 
준식이는 화가 많이 났기 때문에 주먹으로 최대 M 개의 벽을 부수고 지나갈 수 있다.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스의 첫째 줄에 1차원 세상의 길이 N (2 ≤ N ≤ 8) 와 준식이가 벽을 부술 수 있는 최대 횟수 M (0 ≤ M ≤ N - 2)
둘째 줄에 1차원 세상을 표현한 길이 N 짜리 문자열 S 가 주어진다.
문자열에서 @ 는 단 한 번 등장하며, 준식이를 의미한다.
문자열에서 알파벳 대문자 O 는 단 한 번 등장하며, 준식이가 이동하려는 탈출구를 의미한다.
나머지 위치의 문자는 . 이거나 # 이다. . 은 빈 칸을 의미한다. 준식이는 빈 칸으로 자유롭게 이동할 수 있다. # 은 벽을 의미한다. 
준식이는 벽이 있는 칸으로 이동할 수 없지만, 최대 M 개의 벽은 부술 수 있다.

각 테스트 케이스마다 준식이가 1차원 세상을 탈출할 수 있다면 HAHA! 를 출력한다. 
그렇지 못하다면 HELP! 를 출력한다. 모두 대문자로 출력해야 하는 것에 유의한다.

입력
3
7 1
...@#O.
5 2
#@#.O
4 0
O##@

출력
HAHA!
HAHA!
HELP!

'''

testcase = int(input())
ans = []

for _ in range(testcase):
    length,fight = map(int,input().split())
    s = input()
    my_loca = s.find("@") #해당 위치의 인덱스 반환 
    exit_loca = s.find("O")

    if my_loca > exit_loca :
        road = s[exit_loca+1 : my_loca]
        if road.count("#") > fight :
            ans.append("HELP!")
        else : ans.append("HAHA!")
    else :
        road = s[my_loca+1 : exit_loca]
        if road.count("#") > fight :
            ans.append("HELP!")
        else : ans.append("HAHA!")         

for i in ans:
    print(i)

    
