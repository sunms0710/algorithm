# %%

d = {} # 맵, 딕셔너리

d['left'] = '왼쪽'
d['right'] = '오른쪽'
d['3'] = 3
print(d)

# 숫자 범위는 큰데, 자료 갯수는 많지 않을 때

# 문자열에 이것저것 대응이 될 때

d = {1 : 'a', 2 : 'b', 3 : 'c'}
print(d)

for x in d.items():
    print(x)
    
for k, v in d.items():
    print(k, v)
    
# 어떤 숫자가 딕셔너리 안에 key로서 존재하는가?
print(4 in d)
print(3 in d)

#value
print('a' in d.values())


# %%

'''set'''

S = set([1,1,3,3,5,6,7,8,8]) # 집합
print(S)

for x in S:
    print(x)

# 리스트에 비해 탐색 속도 빠름