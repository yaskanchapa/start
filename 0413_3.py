# 딕셔너리를 리턴하는 함수를 선언합니다.
# 이함수를 실행하면 딕셔너리하나 만들고 종료 될겁니다.
def creat_student(name,math,english,science):
    return {"name":name, "math":math, "english":english, "science":science}

#학생을 처리하는 함수를 만듭니다.
def sum_1(student):
    return student["math"]+student["english"]+student["science"]
def avg_1(student):
    return int(sum_1(student) / 3)
def end_1(student):
    return "{}\t{}\t{}".format(student["name"],sum_1(student),avg_1(student))
#-----------------------------------------------------------------------------#
# 학생 리스트 선언
students = [
    creat_student("danaka",87,99,13),
    creat_student("kato",47,59,22),
    creat_student("naga",57,79,43),
    creat_student("honda",67,89,63),
]
# 각각 딕셔너리 형태
# {"name":name, "math":math, "english":english, "science":science}로 리스트에 들어가 있을 거임

# 학생을 한명 씩 반복합니다.
print("이름","총점","평균",sep="\t")
for student in students: # 이지점에서 student는 students의 각 딕셔너리가 순서대로 들어가 처리될 거임
    # {"name":name, "math":math, "english":english, "science":science} 이런 각각의 형태
    print(end_1(student)) # end_1함수안에는 sum_1 함수와 avg_1 함수들도 실행하게 되어 있기 때문에 요거하나면됨
