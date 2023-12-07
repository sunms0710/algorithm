# %%

'''표준 모듈'''

import math

print(math.pi)
print(math.log(2))

from math import pi, log

print(pi)
print(log(2))

from math import *

print(sqrt(4))
# %%

'''외부 모듈'''
import sum
print(sum.sum_two(3,4))