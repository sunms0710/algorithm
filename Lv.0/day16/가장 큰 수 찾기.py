'''
정수 배열 array가 매개변수로 주어질 때, 
가장 큰 수와 그 수의 인덱스를 담은 배열을 
return 하도록 solution 함수를 완성해보세요.

array	        result
[1, 8, 3]   	[8, 1]
[9, 10, 11, 8]	[11, 2]
'''
# %%
def solution(array):
    maxNum = -1
    for x in array:
        maxNum = max(maxNum, x)
    idx = array.index(maxNum)
    answer = [maxNum, idx]
    return answer


print(solution([1, 8, 3]))
print(solution([9, 10, 11, 8]))
