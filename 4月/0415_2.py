# 클래스 내부의 함수를 메소드라고 한다.
# 선언방법은 이하와 같다.
# class 클래스 이름:
#     def 메소드 이름(self,추가적인 매개변수):
#         pass
#-------------------------------------------------#

# 클래스를 선언합니다.
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_avg(self):
        return self.get_sum() / 4
    def to_string(self):
        return "{}\t{}\t{}".format(self.name, self.get_sum(), self.get_avg())
#----------------------------------------------------------------------------#

#리스트를 선언합니다.
students = [
    Student("김태환",87,98,88,95), # {name:김태환, math:87,....}이러한 딕셔너리가 생성될 거임
    Student("이반석",47,44,56,96),
    Student("소정환",57,33,73,94),
    Student("하정우",67,48,83,93),
    Student("김태희",77,88,84,92)
]

#학생을 한명씩 반복시킵니다.
print("이름","총점","평균",sep="\t")
for student in students: #리스트안에 있는 딕셔너리를 하나식 student에 넣어가며 반복함
    #출력합니다.
    print(student.to_string())

# 클래스는 객체를 위한 설계도
# 이러한 클래스(설계도)를 기반으로 만들어진 객체를 인스턴스라고함
# Student(인스턴스or객체라고도함) 설계도가 class 임