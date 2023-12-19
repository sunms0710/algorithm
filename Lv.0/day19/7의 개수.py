'''
머쓱이는 행운의 숫자 7을 가장 좋아합니다. 
정수 배열 array가 매개변수로 주어질 때,
7이 총 몇 개 있는지 return 하도록 solution 함수를 완성해보세요

array	        result
[7, 77, 17]	    4
[10, 29]	    0
'''
# %%
def solution(array):
    answer = []
    for x in array:
        while x != 0:
            answer.append(x % 10)
            x //= 10  
    return answer.count(7)

def solution2(array):
    return str(array).count('7')

print(solution([7, 77, 17]))
print(solution([10, 29]))

print(solution2([7, 77, 17]))
print(solution2([10, 29]))

