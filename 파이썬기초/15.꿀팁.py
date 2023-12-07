# %%

'''구조 분해 할당'''

a = [1,2,3]
x, y, z = a
print(x,y,z)

# %%

'''리스트 컴프리헨션'''

a = [1,4,5,6,7,10]
b = [x * 2 for x in a]
# for x in a:
#     b.append(x * 2)
print(b)

pivot = 5
c = [x for x in a if x > pivot]
# for x in a:
#     if x > pivot:
#         c.append(x)
print(c)
        

# %%

'''언패킹'''

a = 1,2,3

def f(x,y,z):
    return x + y + z

print(f(*a)) #print(f(a[0],a[1],a[2]))


x = '1','2','3','4'

# y = list(map(int,x))
y = [*map(int, x)] 

print(y)

z = {1 : '손', 2 : '흥', 3 : '민', 1999 : '최고'}
w = {**z}

z[1] = '갓'
print(z)
print(w)
# %%

'''람다'''

# def A(x):
#     return x*x + x+1

def B(key, x):
    return key(x)

# print(A(1))
# print(B(A, 1))
print(B(lambda x : x*x + x+1, 1))

# %%

'''global'''

glo = 0 

def function(a,b,c,d):
    print(a,b,c,d)
    print(glo)
    local = 0

print(function(1,2,3,4))
# %%

'''enumerate'''

a = [111,222,333,444,555]

#[(0,111),(1,222),(2,333)..]
b = []

# for i in range(len(a)):
#     b.append((i, a[i]))
# print(b)

print([*enumerate(a)])

