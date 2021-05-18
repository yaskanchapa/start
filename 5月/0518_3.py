# 리스트 박스 만들어보기
from tkinter import *

root = Tk()
root.title("GUI테스트")
root.geometry("640x480")

def btncmd():
    # 삭제
    listbox.delete(END)     # 맨뒤 삭제
    # 삭제
    listbox.delete(0)       # 0은 맨 위 부터 삭제
    # 갯수 확인
    print("리스트에는",listbox.size(),"개가있어요") # .size로 리스트 갯수
    # 항목 확인
    print("첫번째부터 세번째 까지의 항목:", listbox.get(0,2)) # 0,1,2 번째 출력
    # 선택된 항목 확인 (위치로 반환 ex) (0,1,2))
    print("선택된 항목:", listbox.curselection())       # curselection 선택항목이 몇번째인가


listbox = Listbox(root, selectmode="extended", height = 0) # selectmode는 싱글도있음 height = 0이면 전부다 보여줌 3이면 3개까지만 보여줌
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"포도")
listbox.insert(END,"수박")  # END입력시 맨뒤에 추가됨
listbox.insert(END,"사과")
listbox.pack()

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()