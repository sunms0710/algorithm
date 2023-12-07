# %%

'''
문법 에러 -> 실행 전에 알 수 있는 에러
런타임 에러 -> 실행 중에 발생하는 에러
'''

if True:
    pass

a = None # 명시적으로 아무것도 없다. null

# a.split()

b = [1,2,3,4]
print(b[4])
# %%

'''try except'''

try:
    raise IndexError() # 에러
    print('실행구문')
except:
    print('예외발생')
else:
    print('정상실행')
finally:
    print('무조건 실행')
# %%

'''raise 응용'''

try:
    for i in range(10):
        for j in range(10):
            if j == 5:
                raise
            print(i,j)
except:
    pass

# %%

'''함수 내에서 finally'''

def f():
    try:
        return
    except:
        pass
    else:
        print('else')
    finally:
        print('finally')

f()