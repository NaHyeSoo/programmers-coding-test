'''
3 8 7 9 5 reverse 
5 9 7 8 3 / 5 4 7 8 3 / 5 4 3 8 3 / 5 4 3 4 3 
5 4 3 2 3 / 5 4 3 2 1 reverse 1 2 3 4 5 

'''

import math 
testcase = int(input())
answer = []

for _ in range(testcase):
    seq_length = int(input())
    seq = list(map(int,input().split()))
    seq.reverse() #원본 배열이 바뀜
    for i in range(seq_length-1):
        while seq[i+1] > seq[i] : 
            seq[i+1] = math.floor(seq[i+1]/2)
    seq.reverse()        
    answer.append((' '.join(map(str,seq))))  

for j in answer:
    print(j)       

'''
드디어 타노스는 인피니티 건틀렛을 손에 넣었고, 타노스 정렬을 시행하려고 합니다. 타노스 정렬은 세상에서 두번째로 빠른 정렬 알고리즘입니다. 길이가 N인 수열 A[1], A[2], ... , A[N]이 주어졌을 때 이 수열을 타노스 정렬하는 과정은 다음과 같습니다.
A[i] > A[i + 1] (1 ≤ i ≤ N - 1)를 만족하는 원소 A[i]를 인피니티 건틀렛을 이용해 절반으로 줄입니다. 즉, A[i] = floor(A[i] / 2) 를 적용합니다. 이를 만족하는 원소가 여러 개 있다면 가장 앞서는 것을 처리합니다.
더 이상 처리할 수 있는 원소가 없을 때까지 1번 과정을 반복합니다.
주어진 수열 A를 타노스 정렬해서 출력하세요.

첫째 줄에 테스트 케이스의 개수 T가 주어집니다.
각 테스트 케이스의 첫째 줄에 수열의 길이 N (1 ≤ N ≤ 50)이 주어집니다.
둘째 줄에 수열의 원소 A[1], A[2], ..., A[N]이 주어집니다. 수열의 i번째 원소는 정수 A[i] (1 ≤ A[i] ≤ 1 000)입니다.

input
5
5
3 8 7 9 5
3
5 3 1
4
4 3 4 3
3
2 1 1
1
7

output
1 2 3 4 5
1 1 1
1 1 2 3
1 1 1
7
'''