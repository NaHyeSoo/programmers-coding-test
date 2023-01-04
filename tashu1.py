'''
입력 
2 테스트 케이스 개수

4 대여소 개수 
1 0 0 0 대여소애 위치한 자전가 개수 
3 이용기록 개수 
1 2 -> 1번째 대여소에서 빌려 2번째 대여소에 반납 / 0 1 0 0
2 3 -> 0 0 1 0 
3 4 -> 0 0 0 1 

4
1 1 0 2
5
1 3 -> 0 1 1 2
4 2 -> 0 2 1 1
3 3 -> 0 2 1 1
3 1 -> 1 2 0 1
1 4 -> 0 2 0 2 

출력 
0 0 0 1 
0 2 0 2 
'''

testcase = int(input())
answer = []

for _ in range(testcase):
    num = int(input())
    tashu = list(map(int,input().split()))
    usecase = int(input())
    for _ in range(usecase):
        a,b = map(int,input().split())
        tashu[a-1] -= 1 
        tashu[b-1] += 1 
    answer.append(tashu)

# answer = [[0, 0, 0, 1], [0, 2, 0, 2]]



