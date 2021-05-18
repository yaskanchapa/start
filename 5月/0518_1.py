from tkinter import *

# 바꿔주는 함수 생성
def change():
    global photo2
    label_1.config(text="또 만나요")        # config(안에 바꿀내용)
    photo2 = PhotoImage(file = "5月/btn2.png")
    label_2.config(image = photo2)

root = Tk()
root.title("GUI 테스트")

label_1 = Label(root, text = "안녕하세요")
label_1.pack()

photo = PhotoImage(file="5月/btn.png")
label_2 = Label(root, image = photo)
label_2.pack()

btn = Button(root, text="클릭하면바뀜",command=change) # command를 써서 함수 실행시킴
btn.pack()

root.mainloop()