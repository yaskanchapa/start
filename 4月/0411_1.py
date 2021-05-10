with open("test.txt","w") as file:
    # writeline()기본 사용
    file.writelines(["1","2","3","4"])
    # writeline() 매개변수의 리스트는 여러 자료형을 가질 수 있을까?
    file.writelines([True, 273, "문자열"])
    # 문자열만 가능하단 걸 알 수 있다.
    