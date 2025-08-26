'''
import numpy as np  #명령프롬포트에서 설치한 넘파이

mid_s =np.array([10,20,30])

final_s =np.array([60,70,80])

total = mid_s + final_s

print('시험 성적의 합계 :' ,total) # 요소별합계
print('시험 성적의 평균 :' ,total/2) # 모든요소 2로나누기

print(type(total)) #넘파이 타입
'''
'''
a= np.array(range(1,11)) #사칙연산 해보기
b= np.array(range(10,101,10))
a+b,a-b,a*b,a//b

'''
'''
#넘파이 다차원 배열
a = np.array([1,2,3])
a.shap
>>(3,)
a.ndim
>>1
a.dtype
>>dtype('int64')
a.itemsize
>>8
a.size
>>3
'''
'''
#넘파이 연산 
import numpy as np
ary1 = np.array([[1,2,],[3,4]])
ary1 + 10
'''
'''
#넘파이 배열 연산
import numpy as np
salary = np.array([220,250,230])
salary = salary * 2 #두배올려주기
print(salary)
'''
'''

#넘파이 논리적 인덱싱

ages = np.array([10, 19, 25, 30 ,28])
y = ages > 20
>>>array([False, False,  True,  True, False])
ages[ ages > 20 ] #숫자만 뽑아오기

>>>array([25, 30, 28])


'''
'''
#2차원 배열 논리적 인덱싱

~~np_array[:,2]
~~array[[3,6,9,])
--다른문제
ary1 = np.zeros( (2, 2), dtype=np.int8)
ary2 = np.ones((2, 2), dtype=np.int8)
ary1
ary2
np.concatenate( (ary1, ary2 ) ,axis = 0)
np.concatenate( (ary1, ary2 ) ,axis = 1)

'''

#문제

import numpy as np

n = 100 (학생수)

math = np.random.normal(70,10,n)
science = math * 0.5 + np.random.normal(0,5,n)
korean =b np.random.randint(0,101,size= n)
print("통계요약\n")

for subject.
