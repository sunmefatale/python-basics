'''from tkinter import *
root = Tk() #윈도우창 조절하기

root.title("창 조절 연습")
''
root.geometry("500x200")
''
root.resizable(width=FALSE, height=FALSE)
''
root.mainloop()
'''
'''
from tkinter import * #창만들
root = Tk()

label1= Label(root, text="난생처음~~ 파이썬을")
label1.pack()
label2 = Label(root,text="열심히",font=("궁서체",30), fg="red")
label2.pack()
label3 = Label(root, text="코딩 중입니다." ,bg = "yellow",width =20,
               height=5,anchor=CENTER)
label3.pack()

root.mainloop() 
'''

'''
#버튼

from tkinter import *
from tkinter import messagebox

##함수선언문
def myFunc() :
    messagebox.showinfo("버튼클릭", "버튼을 눌렀군요 ^^")

    ##메인 코드부
root = Tk()
root.geometry('300x100')

button1 = Button(root, text ="클릭하세요",fg="red",command=myFunc)
button1.pack()
root.mainloop()

'''
'''
#체크 버튼 컨트롤

from tkinter import *
from tkinter import messagebox
def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("", "체크버튼 off네요 ^^")
    else :
        messagebox.showinfo("", "체크버튼  on이네요 ~")

root = Tk()
root.geometry('300x100')

chk =IntVar()
cb1 = Checkbutton(root, text= "클릭하세요", variable=chk, command=myFunc)
cb1.pack()
root.mainloop()
'''
'''
#라디오버튼 컨트롤
from tkinter import *

def myFunc() :
    if myVar.get()==1:
        label1.configure(text="벤츠")
    elif myVar.get()==2:
        label1.configure(text="BMW")
    else :
        label1.configure(text="아우디")

root = Tk()
root.geometry('300x200')

myVar = IntVar()
rb1 = Radiobutton(root, text = "벤츠",
variable=myVar, value=1, command=myFunc)
rb1.pack()

rb2 = Radiobutton(root, text = "BMW",
variable=myVar, value=1, command=myFunc)
rb2.pack()

rb3 = Radiobutton(root, text = "아우디",
variable=myVar, value=1, command=myFunc)
rb3.pack()

label1 = Label(root, text="선택한 차량 : ",
               fg="red")
label1.pack()
root.mainloop()
'''
'''
#마우스클릭 이벤트의 개념

from tkinter import *
from tkinter import messagebox

def clickLeft(event) :
    messagebox.showinfo("마우스","왼쪽 마우스가 클릭됨")

root = Tk()

root.bind("<Button-1>",clickLeft)
root.mainloop()
'''                       

''''
#이벤트매게변수

from tkinter import *

def clickMouse(event) :
    if event.num == 1 :
        txt = "왼쪽 버튼 : (" + str(event.x) + "," + str(event. y) + ")"
    elif event.num == 3 :
        txt = "오른쪽 버튼 : (" + str(event.x) + "," + str(event. y) + ")"

        label1.configure(text=txt)


root = Tk()
root.geometry('400x400')

label1 = Label(root, text = "여기가 바뀝니다." , fg = "red" )
label1.pack(expand =1, anchor = CENTER)

root.bind("<Button>",clickMouse)
root.mainloop()

'''
'''
#격자 배치관리자 그리드

from tkinter import *

root = Tk()


l1 = Label(root, text ="화씨")
l2 = Label(root, text ="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)


e1 = Entry(root)
e2 = Entry(root)
e1. grid(row=0, column=1)
e2. grid(row=1, column=1)


b1 =Button(root, text= "화씨->섭씨")
b2 =Button(root, text= "섭씨->화씨")
b1. grid(row=2, column=0)
b2. grid(row=2, column=1)
'''
'''
#절대 위치 배치 관리자

from tkinter import *

window = Tk()

w = Label(window, text= "박스 #1", bg='red', fg="white")
w.place(x=0, y=0)
w = Label(window, text= "박스 #2", bg='green', fg="black")
w.place(x=20, y=20)
w = Label(window, text= "박스 #3", bg='blue', fg="white")
w.place(x=40, y=40)


window.mainloop()
root.mainloop()

'''
'''

#메뉴 파일열기
from tkinter import *
from tkinter import messagebox

def Func_open() :
    messagebox.showinfo("메뉴선택", "열기 메뉴를 선택했습니다")

def func_exit():
    root.quit()
    root.destroy()
    
root = Tk()

mainMenu = Menu(root)
root.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu)
fileMenu.add_command(label="열기")
fileMenu.add_separator()
fileMenu.add_command(label="종료")
root.mainloop()

'''
'''
#대화상자


from tkinter import *
from tkinter.simpledialog import *

root = Tk()
root.geometry('200x200')

label1 = Label(root, text = '입력된 값')
label1.pack()

value = askinteger("숫자입력", "주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

label1.configure(text=str(value))

root.mainloop()

'''
#화면 전환하기

from tkinter import *
root = Tk()
root.geometry("300x200")

#--프레임3개생성ㅇ
frame_home = Frame(root)
frame_settings =Frame(root)
frame_about = Frame(root)

#함수정의

def show_home():
    frame_settings.pack_forget()
    frame_about.pack_forget()
    frame_home.pack()

def show_settings():
    frame_home.pack_forget()
    frame_settings.pack()

def show_about():
    frame_home.pack_forget()
    frame_settings.pack_forget()
    frame_about.pack()

#프레임 홈구성
Label(frame_home,text="홈 화면",font=("Arial",16)).pack(pady=10)
Button(frame_home,text="설정으로 이동",
           command=show_settings).pack(pady=5)
Button(frame_home,text="소개로 이동",
           command=show_about).pack(pady=5)

    #프레임 셋팅구성

Label(frame_settings ,text="설정 화면",font=("Arial",16)).pack(pady=10)
Button(frame_settings,text="홈으로", command=show_home).pack(pady=5)


     #어바웃구성

Label(frame_about,text="소개 화면",
          font=("Arial",16)).pack(pady=10)
Button(frame_about,text="홈으로",
           command=show_home).pack(pady=5)

     #첫화면은 홈


frame_home.pack()
root.mainloop()

     


    

