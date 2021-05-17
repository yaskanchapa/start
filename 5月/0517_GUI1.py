# tkinter 모듈 사용 (GUI 모듈)
from tkinter import *

root = Tk()             # 제목
# 창 내부 구조
root.title("GUI TAST")  # 제목바 설정
root.geometry("640x480+100+300") # 창 크기와 생성위치 (넓이 높이 x축좌표 y축좌표)
                                 # 이 때 y=300의 의미는 아래로 내려오는 의미임 수학과 조금 다름
                                 # 화면 기준 왼쪽 상단에서 오른쪽으로 100(x축좌표) 가고 아래로 300(y축좌표)란 의미
root.resizable(False,False)      # 창 크기 변경 안되도록 (x,y)고정시킴
# 창 고정 시키기(닫히지 않도록 하는 것)
# 마지막에 해줘야함 위에 해버리면 각종 창 설정이 반영 안됨
root.mainloop()



