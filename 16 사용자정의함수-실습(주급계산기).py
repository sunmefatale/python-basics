

#사용자 정의함수

def print_c_a():
    print('서울시')


print_c_a()

rate시급 hour일한총시간

'''
'''
def weeklyPay(rate,hour) : #정의
    if hour > 30 : #근무시간이 30시간보다 작으면
        overtime = hour - 30 #초과근무는 총시간에서 30시간빼기
        result = (30 * rate) + (overtime * rate * 1.5)
#결과는 시급과 30시간 곱하기 + 초과는 시급에 1.5배 곱하기
    else:
        result = rate * hour

    
    return result

    #내보냄~

r = int(input("시급을 입력하시오:")) #시급입력받기
h = int(input("근무 시간을 입력하시오:")) #근무시간입력받기



print("주급은" ,weeklyPay(r,h) ) #가로는 늘 덮어쓰기로
