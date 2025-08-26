'''

import random
choices = ["가위","바위","보"]

#횟수 변수 지정
drew = 0
win_a = 0
win_b = 0

#결과값 리스트 지정
resultList = []


#만번 반복
for i in range(10000) :
    com1 = random.choice(choices)
    com2 = random.choice(choices)

    
#가위바위보 조건
    if com1 == '보' and com2 == '보' :
        drew += 1
        resultList.append("비김")
        
    elif com1 == '가위' and com2 == '보' or com1 == '바위' and com2 == '가위' or com1 == '보' and com2 == '바위' :
        win_a += 1
        resultList.append("컴1이김")
        
    else :
        win_b += 1
        resultList.append("컴2이김")
        
    
print("10000번 중 컴퓨터 A의 승리 :",win_a)
print("10000번 중 컴퓨터 B의 승리 :",win_b)
print("10000번 중 총 비긴 경기 :",drew)

'''
'''
#리스트 함축

a= ['welcom','to','the']  #문자열공식
    
f_a = [s[0].upper() for s in a ] #s 인덱스 없으면 전체가 대문자로 되고, 1하면 1번째 문자가~
    
print(f_a)
    
답 : ['W', 'T', 'T']

,[x**2 for x in range(10) if x % 2 ==0] # 10번반복할 때 , 짝수만 구하기
답 : [0, 4, 16, 36, 64]

s = ['ho','123','df','444']
nun = [x for x in s if x.isdigit()]  #isdigit = 숫자인가?
print(num)
답:['123', '444']
[int(x) for x in input('정수를 여러개 입력하세요 : ').split()]   # .split() 분리
[int(x) for x in input('정수를 여러개 입력하세요 : ').split() if x.insdigt] #숫자만 가져오라

'''
'''
list1 = [3,5,7]
list2 = [2,3,4,5,6]

for i in range(len(list1)) :
    
    for k in range(len(list2)) :
        
        print(list1[i]*list2[k])  # i, '*',k,'=',i*k
        
'''
'''
#튜플의 개념 답은 괄호로 나옴 쓰든 안쓰든

numTup1 = 10, #반점을 써줘야 일반값이 아니라 튜플로 인식

#딕셔너리 예제
empDict = {'사번':1000,'이름':'홍길동'}
print(empDict)
답{'사번': 1000, '이름': '홍길동'}
empDict['연락처']='010-1111-1111'
print(empDict)
답{'사번': 1000, '이름': '홍길동', '연락처': '010-1111-1111'}
 
'''
'''
empDict = {'이름':'트와이스' , '구성원수': 9 , '데뷰':'서바이벌식스틴', '대표곡': 'CRY' ,}
for key in empDict :
    print(key, '==>',empDict[key])

'''

#편의점 재고 관리하기


myDict = {}

while True :
    item = input('입력 물품==>')

    if item == 'z' :
        break
    stock = int(input('재고량==>'))
    myDict[item] = stock
    

print('***물품의 재고량 확인 ***')
print(myDict)


while True :
    item1 = input('찾을 물품==>')
    if item1 == 'g' :
        break
    if item1 in myDict :
        print(myDict[item1],'개 남았어요')
    else:
        print("그 물품은 없어요")

