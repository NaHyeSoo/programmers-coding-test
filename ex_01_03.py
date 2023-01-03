

bread_1 = input()
cost_1 = int(input())
bread_2 = input()
cost_2 = int(input())

menu = {bread_1 : cost_1, bread_2 : cost_2}
print(menu)
print(max(menu, key = menu.get))

'''
key는 immutable(불변), value는 mutable(가변)이다.
## 주의 1 : Key 값에 사용가능한 자료형
(사용가능) : str, int, tuple, float, bool ,..
(사용 불가능) : set, list, dict ,..

dict.get(key) -> value 
dict[key] -> value 

'''
#expensive = max(menu, key=dict.get) #값이 최대인 키를 찾아줘 

