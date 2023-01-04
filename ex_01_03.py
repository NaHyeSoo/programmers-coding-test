'''
bread_1 = input()
cost_1 = int(input())
bread_2 = input()
cost_2 = int(input())

menu = {bread_1 : cost_1, bread_2 : cost_2}
print(max(menu, key = menu.get))
'''

## 홀은 빵이름, 짝은 빵가격으로 입력
dic = {} # 해시는 파이썬에서 딕셔너리 
for i in range(4):
    if i % 2 == 0 :
        name = input()
    else :
        price = input()
        dic[name] = price 

ans = max(dic.keys(), key = (lambda a : dic[a]))
print(ans)


'''
key는 immutable(불변), value는 mutable(가변)이다.
## 주의 1 : Key 값에 사용가능한 자료형
(사용가능) : str, int, tuple, float, bool ,..
(사용 불가능) : set, list, dict ,..

dict.get(key) -> value 
dict[key] -> value 

'''
