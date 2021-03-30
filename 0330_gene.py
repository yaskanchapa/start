# 함수를 선업합니다. 
def test():
    print("함수가 호출되었습니다.")
    yield "test"

# 함수를 호출합니다.
print("A지점 통과")
test()

print("B지점 통과")
test()
print(test())

# 원래 test함수 실행 했다면 함수가 호출 되었습니다.란 말이 출력되어야함. 그냥 넘어갔음
# yield 는 양보하다 란 의미로 이를 사용하면 함수가 제네레이트 함수가 되고 일반 함수와는 달리
# 함수를 호출해도 함수 내부의 코드가 실행되지 않는다.

# 제네레이터 함수(함수 내부 코드에 yield 사용한 경우) next()함수를 사용해서 내부 코드를 실행 시킨다.

# 함수를 선언합니다.
def test():
    print("A지점 통과")
    yield 1
    print("B지점 통과")
    yield 2
    print("C지점 통과")

# 함수를 호출합니다.
output = test()

# next() 함수를 호출합니다.
print("D지점 통과")
a = next(output)           #현재 output은 test()를 실행시킨다는게 들어가 있음 
print(a)                   #즉 next 함수로 test()함수를 실행시킨게 a임 -> yield 1 까지실행됨

print("E지점 통과")
b = next(output)           #print(a)에서 yield 1까지 실행됐으니까 그이후부터 실행 yield 2 까지 실행되고 그뒤는 실행안됨
print(b)

print("F지점 통과")
c = next(output)           ##print(b)에서 yield 2까지 실행됐으니까 그이후부터 실행 그 뒤는 실행안됨
print(c)

# 한 번 더 실행합니다.
next(output)

#yield를 내부 코드에 실행해서 해당 함수를 제네레이터 함수로 만드는 이유는 위와 같이 함수코드를 조금씩 실행시키기 위해서
#메모리 효율이 좋다.

