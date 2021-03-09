from random import *
#ランダムの数字を出すように設定

#ランダムで数字をつくる　1から10まで
# print(int(random()*10)+1) 
# print(randrange(1,10)) 

# じゃん　けん　ぽん　を入力してもらいます。
# 入力したのは a に入ります
a = input("가위,바위,보 중 하나를 입력해주세요 :")
print("player: "+a)

# 랜덤 숫자를 b 에 넣는다.
# 0 1 2 出力
# c=int(random()*10) % 2も同じ
b=int(random()*2) 


# 랜덤 숫자 0 1 2 를 각각 가위 바위 보로 지정
# 0=가위 1=바위 2=보
if b==0:
    b="가위"
    print("bot: "+b) 
    
elif b==1:
    b="바위"
    print("bot: "+b)
    
else:
    b="보"
    print("bot: "+b)
    
#비교
if a==b:
    print("무승부입니다.")
elif a=="가위" and b=="바위":
    print("bot의 승리입니다.")
elif a=="가위" and b=="보":
    print("player의 승리입니다.")
elif a=="바위" and b=="가위":
    print("plyaer의 승리입니다.")
elif a=="바위" and b=="보":
    print("bot의 승리입니다.")
elif a=="보" and b=="가위":
    print("bot의 승리입니다.")
elif a=="보" and b=="바위":
    print("plyaer의 승리입니다.")
else:
    print("입력이 올바르지 않습니다.")








