'''
age = int(input("나이를 입력하세요:"))
if age<=18 :
          print("집에 갈 시간이네요!")
print("협조감사합니다")
'''
'''
id = input("아이디를 입력하시오:")
ps = input("패스워드를 입력하시오:")


ddd= "ilovepython"
ppp= "mypass1234"

if id == ddd :
    if ps == ppp :
        print ("환영합니다")
        
    else:
        print("비밀번호를 찾을 수 없습니다.")
else:
        print("아이디를 찾을 수 없습니다.")

#다른방법

        id='ilovepython'
        pw='mypass1234'
        string1 = input("아이디입력하세요:")
        strinf2 = input("비번을입력하세요:")

        if string1 == id and string2 == pw:
            print("환영함다")
        elif string1 != id:
            print("아이디를 찾을수없음")
        else:
            print("비밀번호가틀렸습니다")

'''
'''
#랜덤 초이스 쓰는법


import random #남이해놓은거 젤처음 import 
choices = ['가위','바위','보']


me= input("나의 가위 바위 보 !: ")
computer = random.choice(choices)

#print("컴퓨터의 가위/바위/보 ==>", computer 간결 , 이문제는 한문장으로 ~
print("나: " + me)
print("컴돌이:" + computer)


if me == '보' and computer == '보' :
    print("비겼습니다~!")

elif me =='가위' and computer == '보' or me== '바위' and computer == '가위' or me=='보' and computer =='바위':
    print("대단해용~!~!")

else :
    print("졌대요 메롱~!")

'''

'''
year = int(input("연도를 입력하시오:"))

if year / 4 and year / 400 :
           print(year , "년은 윤년입니다.")
elif year / 100 :
           print(year , "년은 윤년이아닙니다.")

else :
    ("윤년이 아닙니다.")

#한번에 하는법

#if (year / 4 == 0 and year / 100 != 0) or year / 400 == 0:
#프린트 윤년 출력
#else : 프린트 윤년 no 출력

'''







