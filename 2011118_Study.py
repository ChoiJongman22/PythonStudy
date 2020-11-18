#기본적인 자료형은 무엇일까요?

moim="StartUF"
desc="당신의 가족같은 StartUF. Start: 공부 -> Ur 창업 Family"


#아니 포인터의 개념이라고??

a=10
# a라는 건 이름, 10은 정수(자료)형 그러면 어떻게 되냐면 a는 10이라는 자료형을 참조하는거야. 이건 파이썬이 해준다
# 파이썬에서 a는 이제부터 정수형이라고 딱 해주는거야. 우리는 잘 모르지? 이런걸 추상화라고 이해해도 좋을거같아.
# 추상화는 뭐야또...

print(a)
print(moim)


#신기한 문자열
a="strawberry"
b='strawberry'

print(a)
print(b)
print(a[0])
print(a[2])
print(a[1:4])

#다양한걸 지원하는 문자열~
hobby="축구"
age=21
score=4.5
msg1="너의 취미는 %s" % hobby
msg2="너의 취미는 {}".format(hobby) #우와 이것도 돼 ㅋㅋㅋ
msg3="너의 나이는 {} 희망학점은 {}".format(age,score)
print(msg1)
print(msg2)
print(msg3)

#리스트
big3=[]
lotto=[23,45,11,4,22,15]
big4=["제이플라","감스트","대도서관","종만TV"]
combi=["종만",1]

print(combi)

print(lotto[1])
lotto[2]=19
print(lotto)

#딕셔너리(map)
map={"최종헌:개발자","정승훈:개발자?","유수안:디발자"}
print(map)


#집합(set)
s1={1,2,3}
s2={2,3,4,5}
s3=s1.union(s2)
s4=s1.intersection(s2)
s5=s1-s2

print(s3)
print(s4)
print(s5)


#사칙연산
a=5
b=2
print(a//b)
print(a/b)
print(a**b)

#in과 not in 사용해보기
'a' in 'banana' #True
'seed' in 'banana' #False

A=[0,1,1,2,3,5,8,13]
if 3 in A:
    print("Yes")
else :
    print("No")

while 4 in A:
    print("Yes")


#입력하기

name=input("당신의 이름은 무엇입니까?")
print(name)

age=int(input("당신이 가장 좋아하는 숫자는 뭡니까?"))
print(age)


print("game over")

print("print", end=" ")
print("over")


#조건문
value=5
if value%2==0:
    print("짝수입니다.")

else:
    print("홀수입니다.")

score=99
if score>=90:
    print("합격입니다.")
    print("축하해~")

if score>99:
    print("합격입니다.")
print("불쌍하다.")


#반복문
dan=int(input("구구단 입력: "))

n=1
while n<10:
    print("{}X{}=".format(dan,n),dan*n)
    n+=1


dan=int(input("구구단 입력: "))
for a in range(1,10,1):
    print("{}X{}=".format(dan,a),dan*a)


for a in range(10,3,-2):
    print(a)

for item in [12,33,55,44,11]:
    print(item)

for c in "Game Over":
    print(c)

#리스트 컴프리헨션 맛보기
a=[n*2 for n in range (1,10) if n%2==1]
print(a)