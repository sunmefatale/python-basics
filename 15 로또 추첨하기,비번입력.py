'''#로또 추첨하기


import random


def pick_rotto () :
    while len(num_rotto) < 6 :  #6번 반복
    
         num = random.randint(1,45) #1~45중에

         if num not in num_rotto:   ## 이미 뽑은 숫자인지 확인
          num_rotto.append(num)


    num_rotto.sort() #오름차순 정렬
    return num_rotto  #내보내기
    
    


print("**로또 추첨을 시작합니다**")
print("오늘의 로또 번호 ==> ", pick_rotto() )


'''
'''
#하나씩나오게

import random

pick = []

def lottofunc() :  #함수정의
    return random.randint(1,45)


#메인

print("##로또 추첨 시작##")

while len(pick) < 6 :
    num = lottofunc()
    if num not in pick :
        pick. append(num)

#출력
pick.sort()
print("오늘의 로또 번호:" , pick)
'''
'''
#지역 변수와 전역변수 이름이 같은 경우

#지역이 우선됨


def fu1() :
    a = 10
    print("fu1()에서 a의 값 " , a)


def fu2() :
    print("fu2()에서 a의 값", a)


a = 20

fu1()
fu2()

'''

#함수정의

#규칙1. 8글자 이상 규칙2. 영문자 및숫자로만,ㅡ 기호는 불가능


def chak(name):# name 그릇이름 
    
    if len(name) < 8: # 8글자이하면
        return False  # 잘못됐다고 내보낸다
    for ch in name :  #ch는 그냥 문자열 지정한거 
        if not ch.isalnum():  #isalnum은 숫자랑 영문만 추출 
            return False    #만약에 숫자영문만 쓰지 않으면 잘못됐다고
    return True  #맞는걸 내보냄 

#메인 코드생성 ( 정의를 이미해서 코드가 짧아짐)
 

while True :
    newbb = input("새로운 비밀번호를 입력하세요:") #사용자정의
    if chak(newbb):
        #실제 담을  물건  newbb가 name 자리에 쏙 들어감 
        print("good ~비밀번호가 올바르게 생성 되었어요")
        break #아까정의한 함수로 프린트 

    else :
        print("오류! 비밀번호가 규칙에 맞지 않습니다")

        
    

 

 


 
