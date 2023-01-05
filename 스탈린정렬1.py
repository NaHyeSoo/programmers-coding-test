''' 
수열을 스탈린 정렬하는 과정은 다음과 같습니다.
A[i-1] > A[i] (2 ≤ i ≤ |A|)를 만족하는 원소 A[i]를 수열 A에서 제거합니다. 
이를 만족하는 원소가 여러 개 있다면 가장 앞서는 것을 제거합니다.
더 이상 제거할 수 있는 원소가 없을 때까지 1번 과정을 반복합니다.
주어진 수열 A를 스탈린 정렬해서 출력하세요.

첫째 줄에 테스트 케이스의 개수 T (1 ≤ T ≤ 100)가 주어집니다.
각 테스트 케이스의 첫째 줄에 수열의 길이 N (1 ≤ N ≤ 200000)이 주어집니다.
둘째 줄에 수열의 원소 A[1], A[2], ..., A[N]이 주어집니다. 
수열의 i번째 원소는 정수 A[i] (1 ≤ A[i] ≤ 10000000000)입니다.
모든 테스트 케이스의 N의 합은 200 000을 넘지 않습니다.

입력
1
6
3 1 2 4 3 5

출력
3 4 5 
'''

testcase = int(input())
answer = []

for _ in range(testcase):
    seq_length = int(input())
    seq = list(map(int,input().split()))
    pop = seq[0] #비교대상 
    ans = [seq[0]] #스탈린 수열 

    for i in range(1,seq_length):
        if pop < seq[i] :
            pop = seq[i] #비교대상 업데이트 
            ans.append(pop) #수열에 추가 
        elif pop == seq[i]:
            ans.append(pop)
            
    answer.append((' '.join(map(str,ans))))

for j in answer:
    print(j)
