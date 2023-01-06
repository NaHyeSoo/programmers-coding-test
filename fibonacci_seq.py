'''
비효율적 : 한 번 계산된 값도 다시 구해야 됨 
-> 해결'메모화' : 딕셔너리에 한 번 계산된 값을 저장  

[재귀만을 이용한 피보나치 수열]
def fibonacci(i):
    if i == 0:
        return 0 
    elif i == 1:
        return 1 
    else :       
        return fibonacci(i-2) + fibonacci(i-1)
'''

# 재귀와 매모화를 이용한 피보나치 수열 
n = int(input())
dic = {0:0,1:1} 

def fibonacci(i):    
    if i in dic : return dic[i]
    else : 
        output = fibonacci(i-2) + fibonacci(i-1)
        dic.update({i:output}) #dic[i]=output
        return dic[i]

print(fibonacci(n))        


