#비트연산자 bin 정수의 이진수값을 확인하는 함수. 바이너리
#bin(9 & 10) = '0b1001'
# xor  서로 다른 경우에만 1, 이진수 결과값과 십진수 결과값 확인
#9 ^ 10 = 3
#shift 연산 거듭제곱간에 왔다갔다할때  <<  >> 지정된 수만큼 비트를 이동시키는 연산자.

#조건문
'''
num = 99
if num < 100 :
    print("100보다 작습니다.")
'''
"""
num = 200
if num < 100 :
    print("100보다 작군요.")
else :
    print("100보다 크군요.")
    
"""
'''
num = 200
if num < 100 :
    print("100보다 작군요.")
    print("여기는 참입니다.")
else:
    print("100보다 크군요.")
    print("여기는 거짓입니다.")

print("프로그램 끝1")
'''
'''
num = int(input("숫자를 입력==>"))

if num % 2 == 0 :
# 같다는 = 가아니라 == 가 맞다.

    print("짝수입니다.")

else:
    print("홀수입니다.")

#! = 같지않다

'''
'''
num = int(input("숫자를 입력==>"))

if num > 100 :
          if num < 1000 :
             print("100보다 크고 1000보다 작군요.")
          else :
              print("와~ 1000보다 크군요.")

else :
       print("음~ 100보다 작군요.")

'''

'''
num = int(input("점수를 입력 =>"))
if num >= 90 :
    print("a")
elif num >= 80 :
    print("b")
elif num >= 70 :
    print("c")
elif num >= 60 :
    print("d")

else :
    print("f")

print("학점입니다")

'''
'''
num = int(input("점수입력:"))
if num >= 90 :
    print("a")
else:
    if num >= 80:
         print("b")
    else:
        if num >= 70 :
           print("c")
        else :
           print ("d" ,end ="")

print("학점")

# end ="" 인건 이어써짐

'''
'''
num = int(input("점수입력 >"))

if num >= 90 :
    print("a",end="")
elif num >= 80 :
    print("b" ,end="")
elif num >= 70 :
    print("c" , end="")
elif num >= 60 :
    print("d",end="")

else :
    print("f",end="")

print("학점입니다")
'''
