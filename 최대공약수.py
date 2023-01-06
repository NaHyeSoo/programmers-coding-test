'''
유클리드 호제법 : 큰 값을 작은 값으로 나누어 떨어지면 작은 값이 최대공약수
나누어 떨어지지 않으면 작은 값과 나머지에 대해 같은 과정을 나누어 떨어질 때까지
재귀적으로 반복 
ex) 12 10
12 % 10 = 2
10 % 2 = 0  최대공약수 2 

'''

a,b = map(int,input().split())
big = max(a,b)    # x
small = min(a,b)  # y 

def func(x,y):
    rest = x % y
    if rest == 0 : return y
    else : 
        return func(y,rest)

print(func(big,small))