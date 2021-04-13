 # class 특징
 # class 내부 함수는 반듯이 self가 들어감 self 말고 다른 거 넣어도 됨
 # self.식별자(요소)로 접근함

#class 내부 함수를 선언합니다.
class student:
    def creat(self,name,math,english,science):
        self.name = name
        self.math = math
        self.english = english
        self.science = science

#학생 리스트를 선언합니다.
students = [
    student("danaka",87,99,13),
    student("kato",47,59,22),
    student("naga",57,79,43),
    student("honda",67,89,63),
]

#student 인스턴스의 속성에 접근하는 방법
students[0].name
students[0].math
students[0].english
students[0].science
