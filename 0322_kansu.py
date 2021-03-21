# tuple = (1,2,3,4) 一度決まった要素は変更不可
# 一つのみなら(1,)で入力
# ()省略可能
# dictionary = {3:1,4:5}　3の時は1
# list = [1,2,3,4]


# map(関数,リスト)
# filter(関数,リスト)
# lambda 함수를 간단하게 설정 가능. 일부러 함수를 지정하지 않고 그자리에서 바로 사용할 수 있기에 나중에 읽을때도 위로 안올려봐도 되기 떄문에 편하다.

#　関数を指定します。
def power(item):
    return item*item
# power = lambda x: x*x で処理するのも可能
def under_3(item):
    return item < 3
# unter_3 = lambda x: x<3 で処理するのも可能

#　変数を宣言します。
input_a = [1,2,3,4,5]

#　map()関数を使います。
output_a = map(power,input_a)
#output_a = map(lambda x:x*x ,input_a)でも可能
print("# map()の実行結果")
print("map(power,input_a):",output_a)
print("map(power,input_a):",list(output_a))
print()

#　filter()関数を使います。
output_b = filter(under_3,input_a)
print("# filter()の実行結果")
print("filter(under_3,input_a):",output_b)
print("mfilter(under_3,input_a):",list(output_b))
print()

