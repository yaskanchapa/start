# 클래스를 선언
class Human:
    def __init__(self):
        pass
class Student(Human):
    def __init__(self):
        pass

#학생선언
student = Student()

#인스턴스 확인
print("isinstance(student, Human", isinstance(student, Human))
print("type(student) == Human",type(student) == Human)

# 결과문
# isinstance(student, Human True
# type(student) == Human False

#Student클래스는 Human클래스를 상속받아 만들어진거임.
#isinstance는 상속관계까지 파악해서 T/F 결과값을 냄
#type으로 비교하는 방식으로는 상속관계 까지는 파악안됨.