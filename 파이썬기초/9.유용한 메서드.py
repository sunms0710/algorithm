# %%
import math

'''format'''

'{}'.format(1)

'{}, {}'.format(1, 2)

'{1}. {0}'.format(1, 2)

'{:.2f}'.format(math.pi)
'{:.3f}'.format(math.pi)
# %%

'''split'''
'''
1. 띄어쓰기를 기준으로 나누어서 리스트로 반환한다.
2. 결과물의 원소는 반드시 문자열이다.
'''

'1 2 3 4 5 6 7 8'.split()
a = '1,2,3,4,5,6,7,8'.split(',')
b = list(map(int, a))
print(b)

# %%
