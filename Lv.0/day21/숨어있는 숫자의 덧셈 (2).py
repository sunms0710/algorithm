'''
문자열 my_string이 매개변수로 주어집니다. 
my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

my_string	        result
"aAb1B2cC34oOp"	    37
"1a2b3c4d123Z"	    133
'''
# %%
def solution(my_string):
    for x in my_string:
        if x.isalpha():
            my_string = my_string.replace(x, " ")
    my_string = my_string.split()
    return sum(list(map(int, my_string)))


print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123Z"))


