def f(a,b):
 print("おはよう",a)
 print("おはようどこいくの",b)
# 関数ｆを使う　defは関数fを指定するもの

f(1,3) 
# ｆを１，３を入れて実行
# a=1 b=3で実行

# 上記の関数を利用して会話文は関数で実行してみる
def f1(name1,name2):
 print(name1,":おはよう　안녕")
 print(name2,":おう、どこ行くの　어 어디가")
f1("田中","中村")

# 関数を連続で2つしてしておいて実行するのもできるのか
def f2(name3,name4):
 print(name3,":ためしてみたらどうだった？")
 print(name4,":今実行中だから最後までみて")
def f3(name5,name6):
 print(name5,":関数を複数しておいて必要な時だけ拾って使えればいいね")
 print(name6,":これでそれがわかった")
f2("鈴木","佐藤")
f3("鈴木","佐藤")

# 因数は重複でつかったらどうなるのか
def f2(name3,name4):
 print(name3,":ためしてみたらどうだった？")
 print(name4,":今実行中だから最後までみて")
def f3(name3,name4):
 print(name3,":関数を複数しておいて必要な時だけ拾って使えればいいね")
 print(name4,":これでそれがわかった")
f2("鈴木","佐藤")
# f2のname3,name4に鈴木と佐藤を入れる
f3("tanaka","koike")
# f3のname3,name4にtanakaとkoikeを入れる

