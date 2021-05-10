print("問題1．f(n)=f(n-1)+f(n-2)の関数を作ってみます")
print("f(5)は？")
counter = 0
def f(n):
    global counter
    counter += 1

    if n==1 or n==2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(5))

print("【{}回計算を行いました。】".format(counter))
print()

print("問題2．計算回数を減らすように改善してみました")
print("f(5)は？")
memo = {1:1, 2:1}
counter2 = 0
def f(n):
    global counter2
    counter2 += 1
    if n in memo:
        return memo[n]
    else:
        output = f(n-1) + f(n-2)
        memo[n] = output # memorization memoに追加される
        return output
print(f(5))
print(memo) # f(3) -> memo = {1:1,2:1,3:2}
print("【{}回計算を行いました。】".format(counter2))
print()

print("問題3．[]と{}の差は何かtestしてみます。")
test1 = [1,2,3]

test1.append(4)
print("appendを使ったら" + str(test1)) #　test1はstrで文字列にして上げる必要がある！！！ print(test1)の時はstrしなくてOK
test1.insert(4,5) #4番目に5を追加する
print("insertを使ったら" + str(test1))
test1.extend([6,7,8])
print("extendを使ったら" + str(test1))
test1.pop(2) #2番目の要素（3）を削除
print("popを使ったら" + str(test1))
test1.remove(2) #2を削除　2が沢山あっても、一つだけ削除される。
print("removeを使ったら" + str(test1))
print()

test2 = {1:1,2:1}

test2[3] = 4   # 3:4 を追加するとのこと
print("{}に追加してみました。test2[3]=4で　3:4を追加\n"+str(test2))
