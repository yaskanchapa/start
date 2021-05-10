number1 = input("数字入力＞　")
#　数字入力＞の後に入力バー出力　　
number2 = float(number1)
# number1、文字列が ⇒　小数点になる

print()
print(number2,"inch")
print((number2*2.54),"cm")
# 小数点であるnumber2を使用する

#会話文を作ってみる　input format
name1=input("名前を入力して下さい：")
name2=input("名前を入力して下さい：")
# これで名前を全部登録
print()
print("おはよう俺の名前は{}です。.format(name1)")
# 間違っている。　format関数は"の外
print("初めまして俺の名前は{}です。".format(name2))
#　正しい使い方
