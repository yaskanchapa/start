# test() 함수를 선언합니다.
def test():
    print("test()함수의 첫 줄입니다.")
    try:
        print("try구문이 실행되었습니다.")
        return print("리턴 키워드는 함수를 실행했던 위치로 돌아가 또는 함수를 여기서 끝내라는 의미를 갖습니다.")
        print("try구문의return키워드 뒤입니다.")
    except:
        print("except구문이 실행되었습니다.")
    else:
        print("else구문이 실행되었습니다.")
    finally:
        print("finally구문이 실행되었습니다.(리턴으로 인해 함수가 종료되어도 finally 구문은 실행됩니다.)")
    print("test()함수의마지막줄입니다.")

#test() 함수를 실행(호출)합니다.
test()
