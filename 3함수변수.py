'''
num1=input("경기장은 어디입니까?")
num2=input("이긴 팀은 어디입니까?")
num3=input("진 팀은 어디입니까?")
num4=input("우수 선수는 누구입니까?")
num5=input("스코어는 몇대몇입니까?")
print("")
print("===========================================================")
print("오늘" ,num1 ,"에서 야구 경기가 열렸습니다.")
print( num2,"과", num3, "은 치열한 공방전을 펼쳤습니다.")
print( num4,"의 맹활약으로" ,num2 ,"가" ,num3, "를" ,num5 ,"로 이겼습니다.")
print("===========================================================")
'''
'''
f=input("파운드1(b)를 입력하세요 :")
kg = p
print(f,"파운드는" ,kg,"입니다.")
k=input("킬로그램(kg)를 입력하세요:")
print(k,"킬로그램은", fo, "입니다.")
'''
'''
num = int(input("세 자리 정수를 입력하세요:"))
hun = num // 100
ten = ( num % 100) // 10
one = num % 10

print("백의자리:", hun)
print("십의자리:",  ten)
print("일의자리:" , one)
'''
'''
num=int(input("초를 입력하세요:"))
hou= num //3600
min= (num % 3600) // 60
se= num % 60

print(hou,"시",min,"분",se,"초")
'''
total = 0
total -= 900*10
total -= 3500*5
total += 1000*2
total += 4000*4
total += 1500
total += 2000*4
total += 1000*5

print("오늘 총 매출액은", total, "원입니다")
