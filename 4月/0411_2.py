# 예외의 상황에도 어떻게 대처 하라고 프로그래밍을 해줘야 한다.
# 그런대 if문을 사용해서 예외를 다 지정해주기면 뭐가 어떻게 일어날 지 전부 예상하긴 힘들다.
# 그래서 사용하는게 try except 구문이다.
# try 안의 구문은 예외가 일어 날 수 있는 구문이고 예외가 일어날 시에는 except()구문쪽을 실행 하란 의미.

#<예제1>
# number_input_a = int(input("원의 반지름을 입력해주세요 :")) 
# 인풋으로 입력된걸 인트(숫자)로 바꿔줍니다.
# 이상태면 정수 아닌거 입력하면 인트화가 안되면서 여기서 바로 에러뜸

number_input_a = input("원의 반지름을 입력해주세요 :")
print("타입은 {}입니다.".format(type(number_input_a)))
# input으로 들어온 숫자는 현재 문자열 상태임을 알 수 있다.

# if number_input_a == int: <--이거는 인풋으로 받은건 문자열 상태이기때문에 필터 효과가 없다.
print("타입{}을 int로 변환합니다.".format(type(number_input_a)))
if number_input_a.isdigit(): # 입력이 숫자로만 구성되었을 경우
    number_input_a = int(number_input_a)
    print("원의 반지름", number_input_a)
    print("원의 둘레", 2*3.14*number_input_a)
    print("원의 넓이", 3.14*number_input_a**2)

else:
    print("입력한 값은 숫자 또는 정수가 아닙니다.")


# isdigit()함수는 해당값이 숫자면 True 아니면 False를 나타낸다.
print()
print("isdigit함수를 테스트 해봅니다.")
input_b = input("값을 입력해줍시오:")
x = input_b.isdigit()
print(x)

