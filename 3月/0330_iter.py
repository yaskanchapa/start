# 이터레이터란?

# 이터러블 : for 반복자(i) in 반복할 수 있는 것 <- 여기서 반복할 수 있는 것이 이터러블
# 이터러블 : 내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체 (리스트, 딕셔너리, 문자열 튜플 등 [] {} ())
# 이터레이터 : 이런 이터러블([],{},())중 next()함수 적용해 하나하나 꺼낼 수 있는 요소를 이터레이터

#변수선언
numbers = [1,2,3,4,5,6]
r_num = reversed(numbers) 
# reversed를 사용하면 이터레이터가 된다. 
# 거꾸로 출력하기 [6,5,4,3,2,1] 를 만드는게 아니라 기존거에서 거꾸로 뽑아갈거임 <-이터레이터가 됐기 때문.

#reversed_numbers를 출력합니다.
print("numbers를 거꾸로 출력합니다.:",r_num) # <list_reverseiterator object at 0x03996250>가 출력됨 
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

print(next(numbers)) # TypeError: 'list' object is not an iterator 즉 next함수는 이터레이터만 실행가능.
