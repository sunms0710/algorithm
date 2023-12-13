'''
문자열 my_string이 매개변수로 주어질 때, 
my_string 안에 있는 숫자만 골라 오름차순 정렬한 리스트를 
return 하도록 solution 함수를 작성해보세요.

my_string	    result
"hi12392"	    [1, 2, 2, 3, 9]
"p2o4i8gj2"	    [2, 2, 4, 8]
"abcde0"	    [0]
'''

# %%
def solution(my_string):
    answer = []
    number = ['0','1','2','3','4','5','6','7','8','9']
    for x in my_string:
        if x in number:
            x = int(x)
            answer.append(x)
    answer.sort()
    return answer

print(solution("hi12392"))
print(solution("p2o4i8gj2"))
print(solution("abcde0"))




