# 변수를 선언합니다.
list_number = [52, 273, 32, 72, 100]

# try except 구문으로 예외처리
try:
    # 숫자 입력
    number_input = int(input("0-4까지중 정수를 입력해주십시요:"))
    # 리스트의 요소 출력
    print("{}번째 요소:{}".format(number_input,list_number[number_input]))

except ValueError as e1:
    print("값이 잘못되었습니다. 정수를 입력해주세요")
    print("Error:",e1)
except IndexError as e2:
    print("리스트의 인덱스를 벗어났습니다.")
    print("Error:",e2)
except Exception as e3: # Exception은 모든 예외의 부모격 여기선 반듯이 걸린다.
    print("파악하지 못 한 에러가 발생했습니다.")
    print("Error:",e3)