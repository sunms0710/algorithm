'''
정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 
return하도록 solution 함수를 완성해주세요.

n	    result
24	    [1, 2, 3, 4, 6, 8, 12, 24]
29	    [1, 29]
'''
# %%
import math

def solution(n):
    answer = []
    for x in range(1, int(math.sqrt(n)+1)):
        if n % x == 0:
            t = n // x
            if x == t:
                answer.append(x)
            else:
                answer.append(x)
                answer.append(t)
    answer.sort()
    return answer

print(solution(24))
print(solution(29))

