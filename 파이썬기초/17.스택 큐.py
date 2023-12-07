# %%
from collections import deque


'''stack 뒤에 넣고 뒤에서 빼는 자료 구조'''

a = []
a.append(0)
a.pop


'''queue 뒤에 넣고 앞에서 빼는 자료 구조'''

c = deque()
c.append(1)
print(c)
c.appendleft(2)
print(c)
c.pop()
print(c)
c.popleft()
print(c)