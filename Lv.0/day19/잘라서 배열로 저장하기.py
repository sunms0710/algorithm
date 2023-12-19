'''
문자열 my_str과 n이 매개변수로 주어질 때, 
my_str을 길이 n씩 잘라서 저장한 배열을 
return하도록 solution 함수를 완성해주세요.

my_str	            n	result
"abc1Addfggg4556b"	6	["abc1Ad", "dfggg4", "556b"]
"abcdef123"	        3	["abc", "def", "123"]
'''
# %%
def solution(my_str, n):
    answer = []
    while len(my_str) != 0:
        answer.append(my_str[:n])
        my_str = my_str[n:]
    return answer

print(solution("abc1Addfggg4556b", 6))
print(solution("abcdef123", 3))

