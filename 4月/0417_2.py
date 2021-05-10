# 클래스 선언
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("-----학생목록-----")
        print("이름\t총점\t평균")
        for student in cls.students: # Student.students 여도 된다.
            print(str(student)) # 문자열화
        print("----- ----- -----")

    #인스턴스 함수
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self) # 리스트에 방금 셀프항목들 다 넣는단 소리

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    def get_avg(self):
        return self.get_sum()/4
    def __str__(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_avg())
#-----------------------------------------------------------------------------------#

#학생리스트 선언
Student("김태환",87,98,88,95) # {name:김태환, math:87,....}이러한 딕셔너리가 생성될 거임
Student("이반석",47,44,56,96)
Student("소정환",57,33,73,94)
Student("하정우",67,48,83,93)
Student("김태희",77,88,84,92)

#현재 생성된 학생 모두 출력
Student.print()