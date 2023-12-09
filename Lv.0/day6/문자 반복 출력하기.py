'''
문자열 my_string과 정수 n이 매개변수로 주어질 때, 
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 
return 하도록 solution 함수를 완성해보세요.

my_string	n	    result
"hello"	    3	    "hhheeellllllooo"
'''

# %%
def solution(my_string, n):
    answer = ''
    for i in range(len(my_string)):
        answer += my_string[i] * n
    return answer

print(solution("hello", 3))




