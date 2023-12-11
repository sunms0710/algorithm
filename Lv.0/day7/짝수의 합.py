'''
정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 
return 하도록 solution 함수를 작성해주세요.

n	    result
10	    30
4	    6
'''

# %%
def solution(n):
    answer = 0
    for x in range(0, n+1, 2):
            answer += x
    return answer

print(solution(10))
print(solution(4))

