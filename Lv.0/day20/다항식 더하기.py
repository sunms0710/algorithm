'''
한 개 이상의 항의 합으로 이루어진 식을 다항식이라고 합니다. 
다항식을 계산할 때는 동류항끼리 계산해 정리합니다. 
덧셈으로 이루어진 다항식 polynomial이 매개변수로 주어질 때, 
동류항끼리 더한 결괏값을 문자열로 return 하도록 solution 함수를 완성해보세요. 같은 식이라면 가장 짧은 수식을 return 합니다.

polynomial	        result
"3x + 7 + x"	    "4x + 7"
"x + x + x"	        "3x"
'''
# %%
def solution(polynomial):
    answer = ""
    xnum = 0
    const = 0
    for x in polynomial.split(" + "):
        if x.isdigit():
            const += int(x)
        else:
            xnum = xnum + 1 if x == 'x' else xnum + int(x[:-1])
    if xnum == 0:
        answer = str(const)
    elif xnum == 1:
        answer = 'x + ' + str(const) if const != 0 else 'x'
    else:
        answer = str(xnum) + 'x + ' + str(const) if const != 0 else str(xnum) + 'x'
            
    return answer


print(solution("3x + 7 + x"))
print(solution("x + x + x"))
print(solution("x + 3"))


