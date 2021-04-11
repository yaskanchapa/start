# try except 구문을 사용합니다.
try:
    # 파일을 엽니다.
    file = open("info.txt","w")
    # 여러가지 처리를 수행합니다.
    예외.발생해라()
    # 파일을 닫습니다.
    file.close()
except Exception as e: # 예외를 e로써 사용한다는 말 에러내용을 출력하려면 이방식이 편함. 그냥 except:로끝내고 프린트에 내가 에러코드 쓰는것도 방법이긴함
    print(e) # name '예외' is not defined란 에러를 출력함. 

finally:
    #파일을 닫습니다.
    file.close()

print("파일 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)

# 위의 경우 예외란 이름의 파일이 없기 때문에 에러가 날거고 그러다보니 파일이 닫히기 전에 에러나서 제대로 안닫힘
# .closed는 파일이 제대로 닫혔다면 True  아니면 False 값을 리턴한다.

# finally 구문을 사용해 반드시 파일닫기를 실행시키면된다.

# try:
#     예외가 발생 할 가능성이 있는 코드
# except:
#     예외가 발생했을 때 실행할 코드
# else:
#     애외가 발생안했을 때 실행할 코드
# finally:
#     무조건 실행할 코드
# 반드시 위의 순서로 실행하여야 한다.