'''
#암호  입력 로그인하기 
pp= "pythonisfun"

while True:

    un = input("암호를 입력하세요 : ")
    
    if un == pp :
        print("**로그인 성공**")

        break
        
 #pp == ""
    #while pp != "pythonisfun":
    #pp = input("암호임력:")
#print("로그인성공")
    
'''



'''
    
'''
'''
num1=int(input("숫자를 입력하세요"))
for i in range(1,num1,1):
         print("*"*i)
'''
'''
num1=int(input("숫자를 입력하세요:"))
for i in range(1,num1,1):
    print(" " *(num1 - i), "*"*i )
'''
'''
i=0
hap=0


s=int(input("시작값>"))
e=int(input("끝값>"))
p=int(input("증가값>"))
for i in range (s,e,p) :
      hap = hap + i
      
print(s,"에서",e,"까지",p,"씩 증가한 값의 합:", hap)
         
'''         
         
         
#사용자 입력 기반 사친연산 
print("숫자 두개를 차례로 입력하세요:")
num1 = float(input())
num2 = float(input())


op=input("원하는 연산 선택 (a:더하기 /b: 빼기 /c: 곱하기/ d:나누기):")


if op == 'a':
       print("결과;" ,num1 + num2)
elif op == 'b':
    print("결과:", num1 - num2)
elif op == 'c':
    print("결과:", num1 * num2)
elif op == 'd':
    print("결과:",num1/num2 )

else:
    print("잘못된 입력")
