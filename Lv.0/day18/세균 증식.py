'''
어떤 세균은 1시간에 두배만큼 증식한다고 합니다.
처음 세균의 마리수 n과 경과한 시간 t가 매개변수로 주어질 때
t시간 후 세균의 수를 return하도록 solution 함수를 완성해주세요.

n	    t	    result
2	    10  	2048
7	    15  	229,376
'''
# %%
def solution(n, t):
    answer = n
    for _ in range(t):
        answer *= 2
    return answer

print(solution(2,10))
print(solution(7,15))
