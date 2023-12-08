'''
정수 n이 매개변수로 주어질 때, n 이하의 홀수가 오름차순으로 담긴 배열을 
return하도록 solution 함수를 완성해주세요.

n	   result
10	   [1, 3, 5, 7, 9]
15	   [1, 3, 5, 7, 9, 11, 13, 15]
'''
def solution(n):
    return [x for x in range(n + 1) if x % 2 != 0]


print(solution(10))
print(solution(15))