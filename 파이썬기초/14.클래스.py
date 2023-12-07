# %%

'''
클래스

객체지향

객체, 인스턴스

다형성, 캡슐화
'''

class A:
    def __init__(self, name, number, score) -> None:
        self.name = name
        self.number = number
        self.score = score
    
    def toString(self):
        return 'name : {} , number : {} , score : {}'.format(self.name, self.number, self.score)

    def example(a,b): #static 함수
        return a.score < b.score
    
a = A('욱',3,100)
print(a.name, a.number, a.score)

b = A('승',4,0)
print(b.toString())

print(A.example(a,b))
