from random import *
#ランダムの数字を出すように設定

#ランダムで数字をつくる　1から10まで
# print(int(random()*10)+1) 
# print(randrange(1,10)) 

# ぐう　ちょき　ぱあ　を入力してもらいます。
# 入力したのは a に入ります

a = input("ぐう,ちょき,ぱあ の内一つを入力してください。 :")
print("player: "+a)

#ｂにランダム数字を入れる
# 0 1 2 出力
# c=int(random()*10) % 2も同じ
while a != "quit" :
    b=int(random()*2) 

 
# 0 1 2にそれぞれじゃん、けん、ぽんをマッチング
# 0=ちょき 1=ぐう 2=ぱあ
    if b==0:
        b="ちょき"
        print("bot: "+b) 
    elif b==1:
        b="ぐう"
        print("bot: "+b)
    else:
        b="ぱあ"
        print("bot: "+b)
        
    #비교
    if a==b:
        print("引き分けです。")
    elif a=="ちょき" and b=="ぐう":
        print("botの勝利です。")
    elif a=="ちょき" and b=="ぱあ":
        print("playerの勝利です。")
    elif a=="ぐう" and b=="ちょき":
        print("playerの勝利です。")
    elif a=="ぐう" and b=="ぱあ":
        print("botの勝利です。")
    elif a=="ぱあ" and b=="ちょき":
        print("botの勝利です。")
    elif a=="ぱあ" and b=="ぐう":
        print("playerの勝利です。")
    else:
        print("入力が正しくありません。")
    a = input("ぐう,ちょき,ぱあ の内一つを入力してください。 :")