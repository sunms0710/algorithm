'''
문자열 my_string이 매개변수로 주어집니다. 
my_string안의 모든 자연수들의 합을 
return하도록 solution 함수를 완성해주세요.

my_string	        result
"aAb1B2cC34oOp"	    10
"1a2b3c4d123"	    16
'''

# %%
def solution(my_string):
    answer = 0
    number = ['0','1','2','3','4','5','6','7','8','9']
    for x in my_string:
        if x in number:
            x = int(x)
            answer += x
    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))
