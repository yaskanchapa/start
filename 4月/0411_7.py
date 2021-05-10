# 함수를 선언합니다.
def write_text_file(filename, text): # filename이랑 text를 변수로 갖는 함수 write_text_file
    # try except 구문을 사용합니다.
    try:
        # 파일을 엽니다.
        file = open(filename,"w") # 쓰기용으로 파일을 엽니다.
        #여러가지 처리를 수행합니다.
        return # 함수를 종료합니다.
        #파일에 텍스트를 입력합니다.
        file.write(text)
    except Exception as e : # 에러 내용을 e에 담아 놓습니다.
        print(e) # 에러 내용을 출력합니다.
    finally:
        #파일을 닫습니다.
        file.close()
    

# 함수를 호출합니다.
write_text_file("test0411.txt","hello")
