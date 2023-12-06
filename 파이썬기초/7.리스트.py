# %%

'''
리스트

배열

'''

a = [1, 2, 3, 4]
print(a)

b = ['1', True, 12, 1.5]
print(b)

print(a[0])
a[0] = '다른거'
print(a[0])
print(a)

a.append(5)
print(a)

a.insert(2,'인서트')
print(a)

print(a.pop())
print(a)

print(a.pop(2))
print(a)

del a[0] #자주 이용x
print(a)
# %%

'''배열 인덱싱'''

b = [0,1,2,3,4]

print(b[len(b) - 1])
print(b[-1])

c = 'abcd'
print(c[-1])


# %%

'''if 문에서 리스트'''

a = []
if a:
    print('있음')
else:
    print('없음')
# %%

'''배열 슬라이싱'''

a = [0,1,2,3,4,5,6,7,8,9]
print(a[2:6])  #begin <= x < end
print(a[:6])
print(a[6:])
print(a[::2])
print(a[:-1])
print(a[::-1])

#팰린드롬
a = 'abba'
print(a == a[::-1])

# %%

'''리스트의 얕은 복사'''

'''
a -> 메모리 주소 -> [0,1,2,3]
b = a[:] -> 새로운 메모리 주소 -> [0,1,2,3,'마지막 원소']
b.append('마지막 원소')
'''

a = [0,1,2,3]
b = a[:]
print(b)
b.append('마지막 원소')
print(b)
print(a)

# %%

'''다차원 리스트'''

list = [[1,2,3], [4,5,6], [7,8,9]]

'''
[1,2,3]
[4,5,6]
[7,8,9]
'''
print(list[2][2])
# %%

'''리스트 연산'''
print([1,2,3] * 3)
print([1,2,3] + [4,5])