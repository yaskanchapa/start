#from random import*
#random() 0ー１まで

#import random
#a=[r,c,d]
#random.choice(a)

import random
choices=["ぐう","ちょき","ぱあ"]
print("[ぐう、ちょき、ぱあ]")
player = input("上記の中で一つ選択してください：")
count = 1
while player != "end":  #　:　←　忘れないように
    computer=random.choice(choices)
    print("{}回目の勝負です".format(count))
    #print("player:"+player+"computer:"+computer)
    print("plyaer:{} computer:{}".format(player,computer))
    if player==computer: # : ←　忘れないように
        print("引き分けです。")
    elif player=="ぐう": # : ←　忘れないように
        if computer=="ちょき": # : ←　忘れないように
            print("win")
        else: # : ←　忘れないように
            print("lose")
    elif player=="ちょき": # : ←　忘れないように
        if computer=="ぱあ": # : ←　忘れないように
            print("win")
        else: # : ←　忘れないように
            print("lose")
    elif player=="ぱあ": # : ←　忘れないように
        if computer=="ぐう": # : ←　忘れないように
            print("win")
        else: # : ←　忘れないように
            print("lose")
    else:# : ←　忘れないように
        print("入力が正しくありません。")
    print()
    count += 1    
    print("[ぐう、ちょき、ぱあ]修了はend")
    player = input("上記の中で一つ選択してください：")
