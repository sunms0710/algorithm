'''
정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

numbers	                                        result
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	                5.5
[89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]	94.0
'''

# %%
def solution(numbers):
    sum = 0
    for x in numbers:
        sum += x
    avg = sum / len(numbers)
    return avg


test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]	
test2 = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

print(solution(test1))
print(solution(test2))

