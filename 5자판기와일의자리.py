'''
python = 3 *3.5
mobile = 2 * 4.0
ex = 1 *4.5


#A = 4.5 이런식을 만들고 avg=(py *b) 이런식으로 해주고
#나눠주면됨 파이썬 이 로직말고도 ㅇㅇ
#print("평균학점:",avg

total= python+mobile+ex
total2= 3 + 2 + 1

gpa = total / total2

print(gpa)
'''
'''
kg = float(input("몸무게를 kg 단위로 입력하시오:"))
m = float(input("키를 미터 단위로 입력하시오:"))
bmi = kg /(m **2)
print("당신의 bmi=", bmi)
'''
'''
mon = int(input("투입한 돈:"))
pay = int(input("물건값:"))
change = mon - pay
coin500 = change // 500
change = change  % 500 
coin100 = change // 100
print("거스름돈:", mon - pay)
print("500원 동전의 갯수:" , coin500)
print("100원 동전의 갯수:" , coin100)
'''      
'''
j = int(input("세 자리 정수를 입력하세요:"))
one =j % 10
ten = (j % 100 ) // 10
h = j // 100
print("일의자리:",one)
print("십의자리",ten)
print("백의자리", h)
'''
'''
var1 = input("첫 번째 문자열 > ")
var2 = input("두 번째 문자열 > ")

len1 = len(var1)
len2 = len(var2)

diff = len1 - len2
print("두 문자열의 길이 차이는",diff,"입니다")
'''
'''
ss= "트와이스"
print(ss[3],ss[2],ss[1],ss[0])
'''
'''
ss="트와이스"
print(ss[3], end='')
print(ss[2], end='')
print(ss[1], end='')
print(ss[0], end='')
'''
'''
ss="Pyshon"
result = ss[0].lower() + ss[1:].upper()
print(result)
'''

