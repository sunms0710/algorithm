'''
정수 배열 array와 정수 n이 매개변수로 주어질 때, 
array에 들어있는 정수 중 n과 가장 가까운 수를 
return 하도록 solution 함수를 완성해주세요.

array	            n	    result
[3, 10, 28]	        20	    28
[10, 11, 12]	    13	    12
'''
# %%
def solution(array, n):
    array.sort()
    answer = array[0]
    min = abs(array[0] - n)
    for x in array:
        if min > abs(x-n):
            min = abs(x-n)
            answer = x
    return answer

print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))

