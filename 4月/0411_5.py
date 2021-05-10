
π = 3.14

try:
    r = int(input("원의 반지름을 정수로 입력해주십시오:"))
    print("원의반지름:", r)
    print("원의둘레:", 2*π*r)
    print("원의넓이:", π*r**2)
except Exception as e: # 에러메세지를 e 에 넣어놓고
    print(e) # 그 e를 출력한것.

# except:
#     print("에러가 발생했다.") 라고 해놓는것도 가능하긴한데 위에방식이 정확하고 편함