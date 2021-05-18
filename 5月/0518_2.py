# 텍스트와 엔트리 만들기
from tkinter import*

# 텍스트문 출력 시키는 함수
def btncmd():
    print(txt.get("1.0", END))  # 1 = 라인 1부터 가져가라, 0 = 컬럼(문장)기준 0번째위치에서  처음부터 END 끝까지
    print(e.get())

    txt.delete("1.0", END)      # 1= 1번째줄의, 0=왼쪽시작부터, END=끝까지
    e.delete(0, END)            # 0부터(왼쪽시작부터) 끝까지
    
root = Tk()                     # 기본 창 만들기
root.title("GUI 연습하기")      # 창 제목
root.geometry("640x480+300+300")        # 가로 x 세로 + x축위치 + y축위치

txt = Text(root, width=30, height=5)    # 텍스트창 만들기
txt.pack()
txt.insert(END, "글자를 입력하세요")    # 텍스트창에 기본문 띄우기 END라고해야 됨

e = Entry(root, width=30)               # 줄바꾸기 안됨
e.pack()
e.insert(0,"한줄만 입력")

btn = Button(root, text="출력", command = btncmd) # command로 함수 실행
btn.pack()

root.resizable(True, False)     # 창크기 조절 가능여부 x축, y축
root.mainloop()                 # 창 안닫히도록 하는 것