'''
어떤 자연수를 제곱했을 때 나오는 정수를 제곱수라고 합니다. 
정수 n이 매개변수로 주어질 때, 
n이 제곱수라면 1을 아니라면 2를 return하도록 solution 함수를 완성해주세요.

n	    result
144	    1
976	    2
'''
# %%
def solution(n):
    answer = 0
    for x in range(1, n):
        if n // x == x and n % x == 0:
            answer = 1
            break
        else:
            answer = 2
    return answer

print(solution(144))
print(solution(976))
print(solution(3969))
print(solution(1522))
