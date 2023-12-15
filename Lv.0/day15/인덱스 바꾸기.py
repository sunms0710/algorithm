'''
문자열 my_string과 정수 num1, num2가 매개변수로 주어질 때, 
my_string에서 인덱스 num1과 인덱스 num2에 해당하는 문자를 바꾼 문자열을 
return 하도록 solution 함수를 완성해보세요.

my_string	    num1	num2	result
"hello"	        1	    2	    "hlelo"
"I love you"	3	    6	    "I l veoyou"
'''
# %%
def solution(my_string, num1, num2):
    lst_my_string = list(my_string)
    temp = lst_my_string[num1]
    lst_my_string[num1] = lst_my_string[num2]
    lst_my_string[num2] = temp
    answer = "".join(lst_my_string)
    return answer


print(solution("hello", 1, 2))
print(solution("I love you", 3, 6))

