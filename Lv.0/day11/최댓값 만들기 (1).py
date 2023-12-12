'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 
return하도록 solution 함수를 완성해주세요.

numbers	                    result
[1, 2, 3, 4, 5]	            20
[0, 31, 24, 10, 1, 9]	    744
'''

# %%
def solution(numbers):
    sorted_numbers = sorted(numbers,reverse=True)
    return sorted_numbers[0] * sorted_numbers[1]

print(solution([1, 2, 3, 4, 5]))
print(solution([0, 31, 24, 10, 1, 9]))


