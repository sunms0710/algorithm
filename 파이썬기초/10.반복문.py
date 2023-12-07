# %%

'''반복문 for'''

a = [1,2,3,4]

sum = 0
for x in a:
    sum += x
    
print(sum)

'''최솟값을 구하라'''

min = 10101010
for x in a:
    if x < min:
        min = x
print(min)
# %%

'''range'''

# for x in range(10):
#     print(x)
    
# for x in range(100):
#     print(x)

# for x in range(1,10):
#     print(x)
    
# for x in range(1,10,2):
#     print(x)
    
for x in range(10,0,-2):
    print(x)

# %%
'''
리스트 내부에 어떠한 원소가 있는지?
'''
arr = [0,3,6,8,10]

# check = False
# for x in arr:
#     if x == 3:
#         check = True
#         break
# print(check)

print(3 in arr)

string = '12345'
print('234' in string)


# %%

'''리스트, range, 순차적접근'''
'''튜플, 딕셔너리, 셋'''

a = (1,2,3,4,5)
for x in a:
    print(x)

# %%

'''반복문 while'''

i = 0
while i < 10:
    print(i)
    i += 1
    
while True:
    menu = input('좋아하는 메뉴를 입력하세요')
    if menu == '김치':
        print("good")
    elif menu == '나가자':
        break
    else:
        print('bad')
        

# %%
lst = list(range(100))

while lst:
    a = lst.pop()
    print(a)
# %%

'''반복문 else'''
for i in range(10):
    print(i)
else:
    print('완료')

i = 0
while i<10:
    print(i)
    i += 1
else:
    print('완료')