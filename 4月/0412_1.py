# try except 구문으로 예외를 처리합니다. 
try:
    #숫자로 변환합니다.
    number_input_a = int(input("정수를 입력하세요:"))
    #출력합니다.
    print("원의 반지름:",number_input_a)
    print("원의 둘레:",number_input_a*2*3.14)
    print("원의 넓이:",number_input_a*3.14*number_input_a)
except Exception as e:
    #예외 객체를 출력해봅니다.
    print("type(exception):",type(e)) # e의 타입을 검색해봅니다.
    print("e:",e)

# ValueError가 뜬다는 걸 알 수있기 때문에 값이 틀렸다는걸 알 수 있다.
# 그럼 각 에러에 따른 출력문을 구별해 볼 수 있다.

