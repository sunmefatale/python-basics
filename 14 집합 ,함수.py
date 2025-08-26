
'''
집합 만들기  #중가로 해야됨 {}

num = {2,1,3}  
num
{1, 2, 3}


set({1,2,3,2,1})#리스트로부터 집합을 생성함
{1, 2, 3}

set("abcdf")  #문자열도 집합형으로 변환 가능
{'b', 'a', 'f', 'c', 'd'}


집합 접근 연산

num = {2,1,3}    #조건문
if 1 in num :
    print("집합 안에 1 이 있습니다.")

    
집합 안에 1 이 있습니다.


num = {2,1,3}    # 반복문
for x in num :
    print(x, end="")

    
123


sorted(a_set) # 항목을 정렬하여 리스트를 만든다 집합이므로 중복은 제거됨
[1,2,~,~,]

len(a_set) # 길이재는것도 중복 제외시킴

'''

'''
print("A님 , 두 숫자를 입력하세요")
a = int(input("점수 1 == >"))
b = int(input("점수 2 == >"))
print("결과 : " ,a + b)

print("B님 , 두 숫자를 입력하세요")
a1 = int(input("점수 1 == >"))
b1 = int(input("점수 2 == >"))
print("결과 : " ,a1 + b1)

print("C님 , 두 숫자를 입력하세요")
a2 = int(input("점수 1 == >"))
b2 = int(input("점수 2 == >"))
print("결과 : " ,a2 + b2)
'''
'''
def hapfunc() :    # 위 예제문제를 쉽게 정의 할 수 있는 함수
    num1 = int(input("정수1 ==>"))  #합펑션을 써서 정의하면 나중에 수정이 용의하다
    num2 = int(input("정수2 ==>"))
    return num1 + num2

print("A님 두 숫자를 입력하세요") #반복문 사용하면 더짧게 가능~!
hap = hapfunc()
print("결과 : " , hap )

'''
'''
def plus(v1,v2) :   #plus 라는 함수 정의 (변수)
    result = 0         #
    result = v1 + v2
    return result #결괏값 내보내기

hap = 0

hap = plus(100,200)
print("100과 200의 plus() 함수 결과는",hap) #부르기
'''
'''
def print_hello() : # 얘는 + 나 * 할게 없어서 리턴이 필요없음 그냥 프린트만 하면됨
    print("hello w")    #   변수가들어가야하면 (?,?) 이렇게 들어가는데 그냥 프린트하는거면 변수 없어서 () 만 하면됨 
    print("hello t")

a = 5
if (a > 3) :
    print_hello()

'''
'''
def elem(op,n1,n2) :  #함수를 사용한 계산기 구현
    if op == "+" :           #꼭 if문으로 사칙연산 값을 저장해놔야 컴터가 알아듣는다 주의별표!!
        result = n1 + n2
    elif op == "-" :
        result = n1 - n2
    elif op == "*" :
        result = n1 * n2
    elif op == "/" :
        result = n1 / n2
    else :                                      #여기는 정의구간  이거로 뭐안나옴
        print("잘못된 입력입니다")
        
    return result  #값 내보내기


    
#사용자 입력 시키기
e1 = input("계산 입력 (+,-,*,/) : " ) #문자불러오기는 인트아님!!!!
num1 = int(input("첫번째 숫자 입력 : "))
num2 = int(input("두번째 숫자 입력 : "))

#전역 변수 선언
hap = 0

#출력
hap = elem(e1,num1,num2)

print("##계산기 : " ,num1,e1,num2,"=", hap)  



#반환 값이 없는 함수
def fuc1() :
    print("반환값이 없는 함수 실행")

fuc1()

'''
'''
#반환 값이 하나인 함수

def func2() :
    result = 100
    return result

hap = 0

hap = func2()
print("fucn2()에서 돌려준 값 ==> " ,hap )



#반환 값이 두개인 함수

def func3() :
    result1 = 100
    result2 = 200
    return result1,result2

hap1,hap2 = 0,0

hap1,hap2 = func3()


print("fucn2()에서 돌려준 값 ==> " ,hap1,hap2 )



#숫자 2개의 합과 3 개의 합을 구하는 함수

def p2_func(v1,v2) :
    result = v1 + v2
    return result

def p3_func(v1,v2,v3) :
    result = v1 + v2 + v3
    return result

hap = 0

hap= p2_func(10,20)
print("매개변수 2개 함수 호출 결과 ==>" , hap)

hap= p3_func(10,20,30)
print("매개변수 3개 함수 호출 결과 ==>" ,hap)




