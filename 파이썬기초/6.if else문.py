# %%
'''조건문'''

A = '이'

if A == '손':
    print('중요한 것은')
elif A == '이':
    print('벤버지')
else :
    print('꺽이지 않는 마음')
    
성적 = 3.7

if 성적 >= 4.3:
    print('과탑')
elif 성적 >= 3.7:
    print('장학금')
elif 성적 >= 2.7:
    print('일반인')
else :
    print('자유를 갈망하는 혁명의 씨앗')
# %%

'''변수'''
if 0:
    print('1')
    
a = 0
if not a:
    print('0 아님')

b = '' #False
b = 'asd' #True
if b:
    print('출력되나')
