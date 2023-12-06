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