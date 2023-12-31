'''
정수 n이 매개변수로 주어질 때 n의 각 자리 숫자의 합을 
return하도록 solution 함수를 완성해주세요

n	        result
1234	    10
930211	    16
'''
# %%
def solution(n):
    answer = 0
    while n != 0:
        answer += n % 10
        n //= 10
    return answer

print(solution(1234))
print(solution(930211))
print(solution(100001))
