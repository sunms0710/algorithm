'''
문자열 s가 매개변수로 주어집니다. 
s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 
return 하도록 solution 함수를 완성해보세요. 
한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

s	            result
"abcabcadc"	    "d"
"abdc"	        "abcd"
"hello"	        "eho"
'''

# %%
def solution(s):
    answer = ''
    for x in s:
        if s.count(x) == 1:
            answer += x
    return ''.join(sorted(answer))

print(solution("abcabcadc"))
print(solution("abdc"))
print(solution("hello"))