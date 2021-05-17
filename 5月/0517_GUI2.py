# tkinter 모듈 사용 (GUI 모듈)
from tkinter import *

def btn():
    print("버튼이 클릭 되었습니다.")

root = Tk()             # 제목
# 창 내부 구조
root.title("GUI TAST")  # 제목바 설정

button1 = Button(root, text="버튼1")
button1.pack()

button2 = Button(root, padx=5, pady=20,text="버튼2")
button2.pack()

button3 = Button(root, padx=20, pady=5, text="버튼3")
button3.pack()

button4 = Button(root, width=20, height=5, text="버튼4")    # pad 문자열 많으면 문자열에 크기 맞춤 width등은 상자크기 고정
button4.pack()

button5 = Button(root, fg="red", bg="blue", text="버튼5")   # fg 글자색 bg 배경색
button5.pack()

photo = PhotoImage(file="5月/btn.png")                      # 이미지버튼
button6 = Button(root, image=photo)
button6.pack()

# button7 = Button(root, text="동작하는버튼",command=btn()) # btn()이거로 하면 클릭안해도 한번만 실행됨
button7 = Button(root, text="동작하는버튼",command=btn)     # 버튼 클릭되면 btn함수 실행
button7.pack()
# 창 고정 시키기(닫히지 않도록 하는 것)
# 마지막에 해줘야함 위에 해버리면 각종 창 설정이 반영 안됨
root.mainloop()
