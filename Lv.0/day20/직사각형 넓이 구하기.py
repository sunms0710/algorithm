'''
2차원 좌표 평면에 변이 축과 평행한 직사각형이 있습니다. 
직사각형 네 꼭짓점의 좌표 [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]가 
담겨있는 배열 dots가 매개변수로 주어질 때, 
직사각형의 넓이를 return 하도록 solution 함수를 완성해보세요

dots	                                result
[[1, 1], [2, 1], [2, 2], [1, 2]]	    1
[[-1, -1], [1, 1], [1, -1], [-1, 1]]	4
'''
# %%
def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    w = max(x) - min(x)
    h = max(y) - min(y)
    return w * h


print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))
print(solution([[1, 3], [3, 0], [3, 3], [1, 0]]))
print(solution([[0, 3], [0, 0], [4, 3], [4, 0]]))



