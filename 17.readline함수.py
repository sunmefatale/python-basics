
'''
infile = None #입력 파일 논은 초기화의 의미 안써도됨

instr = "" #읽어온 문자열 

inFile = open("myData1.txt", "r" , encoding= "UTF-8") #파일열기

instr = inFile.readline()
print(instr)

instr = inFile.readline()
print(instr)

instr = inFile.readline() 
print(instr) #, end=''

inFile.close()


'''

infile = None #입력 파일 논은 초기화의 의미 안써도됨

instr = "" #읽어온 문자열 

inFile = open("myData1.txt", "r" , encoding= "UTF-8") #파일열기

while True :
    instr = inFile.readline()
    if instr == "" :
        break
    print(instr,end = '')


inFile.close()
