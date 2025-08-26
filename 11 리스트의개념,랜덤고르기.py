'''

#num1,num2,num3,num4 = 0, 0 ,0,0
hap= 0

num1 =int(input("숫자 : "))
num2 =int(input("숫자 : "))
num3 =int(input("숫자 : "))
num4 =int(input("숫자 : "))

hap = num1 + num2 +num3 +num4
print("합계 ==> ",hap)

'''
'''
numList= [0,0,0,0]
hap = 0

numList[0] = int(input("숫자 :"))
numList[1] = int(input("숫자 :"))
numList[2] = int(input("숫자 :"))
numList[3] = int(input("숫자 :"))

hap = numList[0]+numList[1]+numList[2]+numList[3]
print("합계 ==>",hap)
'''
'''
numList = []
for i in range(0,4,) :
    numList.append(0)

hap = 0
for i in range(0,4) :
    numList[i] = int(input("숫자 : "))

hap = numList[0] + numList[1] + numList[2] + numList[3]
print("합계 ==>",hap)
'''
'''
numList = [10,20,30,40] #리스트불러오기 슬라이싱
print(numList[0:-2])
'''
'''
# : 앞뒤로 건너뛸수있음   [:] 첨부터끝까지, ::2 처음부터끝까지읽고 스텝만큼건너뛰기

numList = [4,5,6,7,8,9]
print(numList[2])
print(numList[1:2])
print(numList[0:3]) #:3
print(numList[1::2])
'''
'''
bts = ['v']
'v' in bts #트루나옴
'v' not in bts #펄스나옴
bts = bts + ['rm'] #리스트 값추가
'''
'''
import random
mList = ["언제나 현재에 집중할 수 있다면 행복할 것이다","히히","나짱"]
#print("오늘의명언==>",random.choice(mList))
#랜덤불러오기 랜덤.초이스(변수)
#혹은 random.randint
#print(mList[0])
#list(range(1))
indax= random.randint(0 ,len(mList)-1)
print("오늘의 명언>>",mList[indax])

'''
'''
pap = ['seoul',9765, 'busan',3441, 'inchon',2954]
print("서울인구>",pap[2])
print("인천인구>",pap[-1])
print("도시 리스트>",pap[::2])
pop = pap[1::2]
print("인구의 합>",sum(pop)) # sum 리스트 숫자 더해주는 함수

numList.insert(1,40)# 위치, 값 추가하기
'''
'''
myList = [10,20,10,10,10]
           
#삭제 del(myList[1])
#길이 len(myList)
#최댓값 max(myList) 알파벳이면 알파벳대로 특수문자도
#최솟값 min(myList)
#오름차순 정렬 myList.sort()
#내림차순 정력 myList.sort(reverse=True)
#그냥 차례반전 myList.reverse()
#복사 새로운변수 = myList.copy()
#bts.index 인덱스 몇번인지 찾기
#응용 if "v" in bts :
#print(bts.indax("v"))
'''
'''
#리스트에 속한 모든 항목 접근 for활용
bts =["v","제이홉","슈가"]
for member in bts:
    print(member)

'''
'''
heights = [178,173,166,164,176]
smallest = heights[0]

for h in heights : #값끼리비교하여 작은값찾기 
    if h < smallest :
        smallest = h

print('리스트 원소들 :',heights)
print("이 중에서 가장 작은 값은 :" ,smallest)

'''
'''

heights = [178,173,166,164,176]
lazest = heights[0]

for h in heights : #값끼리비교하여 큰 값찾기 
    if h > lazest :
        lazest = h

print('리스트 원소들 :',heights)
print("이 중에서 가장 큰 값은 :" ,lazest)
'''
'''
aList = [1,2,3,4],[5,6,7,8],[9,10,11,12]
aList[0][1]  #i는 행 k 는 열
aList[1][3]         #2차원리스트 [행][열] 찾기
bList =[[1,2,3,4],
        [5,6,7,8],
        [9,10,11,12]]
aList = bList

for i in range(0,3) :
    for k in range(0,4) :
        print ("",bList[i][k],end="")
        print("")

'''
''''
#반복문과 리스트 통합

print("홍길동 선수 경기 끝났습니다~짝짝짝")
score_list = []

for i in range(5) :
    score=int(input("평가 점수==>"))
    score_list.append(score)  #리스트에추가
     
    hap = sum(score_list) #hap=0
    bList = hap / 5                #for i in range(5))
                                #hap +=sscore[i]
print("심사위원 평균 점수: ", bList  )  #avg = gap /5

#print("심사위원 평균 점수: " ,avg)

'''

'''
imp


