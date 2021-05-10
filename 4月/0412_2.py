# 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외처리
try:
    # 숫자 입력
    number_input = int(input("0-4까지중 정수를 입력해주십시요:"))
    # 리스트의 요소 출력
    print("{}번째 요소:{}".format(number_input,list_number[number_input]))
# 모든 에러를 e로 처리함.
except Exception as e: 
    # 예외 출력해봅니다.
    print("tyupe(e):",type(e))
    print("e:",e)

# except뒤에 각종 구문을 넣어서 예외 종류 구분이 가능하다. Exception은 가장 포괄적인 구문