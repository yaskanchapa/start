# 딕셔너리를 리턴하는 함수를 선언합니다.
# 학생 정보를 생성하도록 한다는 말입니다.
def creat_student(name,math,english,science): # name, math, english, science의 요소를 갖는 함수입니다.
    #함수의 내부 구문입니다.
    #리턴이므로 딕셔너리를 생성 후 함수는 종료됩니다.
    #문자열name과입력한요소값 name이 매칭되어 딕셔너리에 보존됩니다. 나머지도 동일합니다.
    return {
        "name":name,
        "math":math,
        "english":english,
        "science":science
    }
#-----------------------------함수 정의------------------------------------------------------#

# {"name":"danaka","math":87,"english":99,"science":13} 란 딕셔너리가 생성될 거고 students의 리스트에 들어갈 겁니다.
# students = [creat_student(danaka,87,99,13)] 이경우 danaka를 문자열로 안해주면 에러가 나기 떄문에 "danaka"로 해줘야된다.
students = [
    creat_student("danaka",87,99,13),
    creat_student("kato",47,59,22),
    creat_student("naga",57,79,43),
    creat_student("honda",67,89,63),
]
# {"name":"danaka","math":87,"english":99,"science":13} 이런식으로 딕셔너리가 각각 생성되어 리스트에 들어가있게됨

# 학생을 한 명씩 반복합니다.
print("이름","총점","평균",sep="\t")
for student in students:
    # 점수의 총합과 평균을 구합니다.
    sum_1 = student["math"] + student["english"] + student["science"]
    avg_1 = int(sum_1 / 3)
    print(student["name"],sum_1,avg_1,sep="\t")
