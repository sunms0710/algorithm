# %%
'''bisect'''
import bisect
import random
'''
이분탐색
정렬된 배열x, logN
'''

a = [random.randint(0,100) for _ in range(10)]
print(a)
print(a[bisect.bisect_left(a,10)] == 10)