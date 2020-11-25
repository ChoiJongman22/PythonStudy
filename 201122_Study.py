#List Comprehension
#기존 리스트를 기반으로 새로운 리스트를 만들어내는 구문.
#파이썬 다운 생각
#람다 표현식 + map이나 filter를 섞어서 사용하는 것에 비해 가독성이 엄청 높다!
#내가 알려준다고 했던 List의 내장 함수를 사용한다. 지금 부터 시작!

#list Comprehension을 사용하지 않는 방법

a=[]
for n in range(1,11):
    if n%2==1:
        a.append(n*2)
print(a)

#list Comprehension을 사용하여 하는 방법
b=[n*2 for n in range(1,11) if n % 2==1]
print(b)
#완전 쉽지??

#짝수를 담는 ListComprehension
evens = [x * 2 for x in range(11)]
print(evens)

#list의 합을 나타내는 함수 sum
vals = [32, 12, 96, 42, 32, 93, 31, 23, 65, 43, 76]
amount = sum(vals)
print(amount)

#리스트의 값을 나누는 리스트
RealValues = [(x / amount) + 1 for x in vals]
print(RealValues)

#제곱사용하기
from math import sqrt
#완전제곱수가 아닌 숫자를 모으자!
non_square=[x for x in range(101) if sqrt(x)**2!=x]
print(non_square)

#튜플을 사용한 list comprehension
epithets = ['sweet', 'annoying', 'cool', 'grey-eyed']
names = ['john', 'alice', 'james']
epithet_names = [(e, n) for e in epithets for n in names]
print(epithet_names)
#마치 다항식의 곱셈처럼 다 전개해서 나오는 거 보여?? 

#피타고라스 한번 해볼까? (삼각비알지??) - 몰라도 상관없지!
solutions = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
print(solutions)

#이번엔 모음을 제외하고 해볼래?
word='mathematics'
no_moum=''.join([c for c in word if c not in['a','e','i','o','u']])
print(no_moum)
#지금까지 완전 재밌지??


#행렬! 설명필요하겠지??
matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9, 10, 11, 12],
]
flatten = [e for r in matrix for e in r]
print([r for r in matrix])
print(flatten)



#dict comprehension
subjects = ['math', 'history', 'english', 'computer engineering']
scores = [90, 80, 95, 100]
score_dict = {key: value for key, value in zip(subjects, scores)}
print(score_dict)


# 튜플 리스트를 dict 형태로 변환하는 DC
score_tuples = [('math', 90), ('history', 80), ('english', 95), ('computer engineering', 100)]
score_dict2 = {t[0]: t[1] for t in score_tuples}
print(score_dict2)



#list 과제

a=["아직도","어디에나","멀리있는","어리고","지속적으로","바라보지마라","빛이나는","배고프다","아무곳도","어리바리","바보같은","어지간한","멋있는","야호","늙어버린","애교쟁이","꼰대","종만이짱짱","그레이트"]
b=[c for c in a if len(c)%2!=0]
print(b)