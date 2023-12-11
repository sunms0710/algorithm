'''
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 
진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 
응급도가 높은 순서대로 진료 순서를 정한 배열을 
return하도록 solution 함수를 완성해주세요.

emergency	            result
[3, 76, 24]	            [3, 1, 2]
[1, 2, 3, 4, 5, 6, 7]	[7, 6, 5, 4, 3, 2, 1]
[30, 10, 23, 6, 100]	[2, 4, 3, 5, 1]
'''

# %%
def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(sorted_emergency.index(i)+1)
    return answer

print(solution([3, 76, 24]))
print(solution([1, 2, 3, 4, 5, 6, 7]))
print(solution([30, 10, 23, 6, 100]))



# %%
print([1,2,3].index(3) +1)