# 클래스를 선언
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        #인스턴스 변수 초기화
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        #클래스 변수 설정
        Student.count += 1 # self.count 는 안되는건가? #내부 외부 에서 동시에 사용 하기 위해선 Student.으로 하는게 맞다.
                            # 외부에서 self 라면 못가져 오기 때문이다.
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

#학생리스트 선언
students = [
    Student("김태환",87,98,88,95), # {name:김태환, math:87,....}이러한 딕셔너리가 생성될 거임
    Student("이반석",47,44,56,96),
    Student("소정환",57,33,73,94),
    Student("하정우",67,48,83,93),
    Student("김태희",77,88,84,92)
]

#출력합니다.
print()
print("현재 생성된 총 학생 수는 {}명입니다.".format(Student.count))