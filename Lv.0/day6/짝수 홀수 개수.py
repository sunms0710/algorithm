'''
정수가 담긴 리스트 num_list가 주어질 때, 
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 
return 하도록 solution 함수를 완성해보세요.

num_list	            result
[1, 2, 3, 4, 5]     	[2, 3]
[1, 3, 5, 7]	        [0, 4]
'''

# %%
def solution(num_list):
    cnt1 = 0
    cnt2 = 0
    for x in num_list:
        if x % 2 == 0:
            cnt1 += 1
        else:
            cnt2 += 1
    answer = [cnt1, cnt2]
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 5, 7]))

