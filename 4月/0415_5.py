# 학생 클래스 선언
class Student:
    def study(self):
        print("공부를 합니다.")

# 선생 클래스 선언
class Teacher:
    def teach(self):
        print("학생을 가르칩니다.")
    

# 교실 내부의 객체 리스트를 생성합니다.
classroom = [Student(),Student(),Student(),Student(),Teacher()]

#반복 정용해서 적절한 함수호출
for person in classroom:            #교실 내부 객체리스트에서 하나하나 person에 넣어가며 비교
    if isinstance(person, Student): #person에 넣은 인물이 Student()에 의한 값이라면 True가되어 아래 실행
        person.study()              #study메소드(함수라고도함)실행되어 공부를 합니다 출력될거임
    elif isinstance(person, Teacher):
        person.teach()

# 결과값
# 공부를 합니다.
# 공부를 합니다.
# 공부를 합니다.
# 공부를 합니다.
# 학생을 가르칩니다.