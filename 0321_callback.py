def callback(f): # callback関数はcallback中の関数を変数1から10まで繰り返す関数
    for i in range(10): # 10回繰り返し
        f(i) #関数fが何かわからなくてもとりえずこれは、callback関数は中の関数の変数を1から10まで繰り返すとのこと。
             # 関数fの代わりにtest_print関数を入れても実行できた理由

def test_print(number):   #fの意味としてこの関数をcallback関数に入れて見る予定
    print("hello",number) # hello number を出力する関数

callback(test_print) #callback関数実行　test_print関数を変数1から10まで繰り返す。


# test_print関数はhello, numberを出力する関数

# test_print(0)
  # hello 0
# test_print(1)
# hello 1
# test_print(2)
# hello 2
# test_print(3)
# hello 3
# ...
# hello 9

#もうちょっとわかりやすく書くと
def callback(g): # callback関数指定
    for i in range(10): # 10回繰り返し
        g(i) # iを1から10まで関数gに入れ替えながら繰り返す
        # 関数gはなんだ？？

def g(num): #関数gを指定
    print("bye",num) #bye,numを出力する関数

callback(g) #関数gの変数を1から10まで入れながらbye,変数(num)を出力する


# もっと簡単にする方法＝lambda
def callback2(t): # callback2関数指定
    for i in range(10): # 10回繰り返し
        t(i) # iを1から10まで関数gに入れ替えながら繰り返す
        # 関数tはなんだ？？

# def t(number): #関数tを指定
#    print("byebye",number) # tはbye,numberを出力する関数

# 上記42,43の代わりに以下のlambdaを使う
callback2(lambda number : print("byebye",number))

