'''
i = 0
hap = 0

for i in range(1, 11, 1) :
    hap = hap + i
    #print("i=",i, 'hap = ' ,hap)
print("1에서 10까지의 합 : " , hap)
'''
'''
i=0
hap=0
for i in range(1001,2001,2):
    hap = hap + i
    
print("1000에서 2000까지 홀수의 합:",hap)
'''
'''
for i in range (3) :
    for k in range(2) :
        print("난생처음 (i값:",i,",k값:",k,")")
'''
'''
#구구단계산기
for i in range(2,10,1) :
    for k in range(1,10,1) :
        print(i,"*",k ,"=",i*k)
    print("")
'''
'''
#while문 #횟수모를때
i=0
while (i<3) :
    print(i,": 난생처음")
    i = i+1
'''
'''
for i in "hello" :
    print("i=",i)
'''
'''
#무한반복 컨트롤 c로종료
#break 쓰면 무한반복 빠져나옴 무조건

while True :
    print("ㅎ",end = '')
'''
'''
while True :
    num1 = int(input("숫자1:"))
    num2 = int(input("숫자2:"))
    print(num1 + num2 , end='')
    print("")
'''
'''
while True :
    num1 = int(input("숫자1:"))
    if  num1 == 0 :
           break
    num2 = int(input("숫자2:"))
    print(num1 + num2 , end='')
    print("")
print("0을 입력해서 계산을 종료합니다.")
'''
'''
#처음으로 돌아가는continue문
i , hap = 0,0
for i in range(1,101,1) :
    if i / 4 == 0 :
        continue
    hap += 1

    
print("1~100의 합계 (4의배수 제외) : ",hap)


i, hap=0,0
for i in range(1,11,1) : #횟수가정해져있을때
    print("i=",i)
    if i / 4 == 0 :
         coutinue
    hap+=i
print("hap=",hap)

'''
'''#주사위던지기게임
import random
count = 0 #반복횟수
num1,num2,num3 = 0,0,0

while True : 
    num1= random.randint(1,6) # 랜덤공식
    num2= random.randint(1,6)
    num3= random.randint(1,6) 
    count += 1
    print("주사위1:",num1,"주사위2:",num2,"주사위3:",num3, "횟수",count)

    if num1 == num2 == num3 :#3개값 동일반복중단
        break
    
print("3개주사위는 모두" ,num1, "입니다")
print("같은 숫자가 나오기까지", count , "번 던졌습니다")
'''

import random
i = 0
count = 0


for i in range(0, 11, 1) :
    com= random.randint(1,5)
    print("컴퓨터:?")
    me=int(input("컴퓨터가 생각한 숫자를 맞춰봐! >"))
    count+=1
    
    if me == com :
        print("맞췄다 >_<!!")

        break
    elif me < com :
        print("ㄴㄴ 더 큰수를 입력해봐")
    else :
        print("틀렸어용~~~ㅠ 더 작은 수야~")

if me !=com:
    print("10번이 지났습니다 ......우우우" )
