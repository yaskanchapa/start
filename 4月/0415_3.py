# 객체가 어떤 클래스로 부터 만들어졌는지 확인할수 있는 함수 = isinstance(인스턴스, 클래스)
# 인스턴스가 해당 클래스를 기반으로 만들어졌다면 True 아니면 False를 리턴함
#----------------------------------------------------------------------------------------#

# 클래스를 선언합니다.
class Student:
    def __init__(self):
        pass

# 학생을 선언합니다.
student = Student()

# 인스턴스 해당 클래스로 만들어 진건지 확인하기
print("isinstance(student, Student)", isinstance(student, Student))