# 학생 리스트를 선언합니다.
students = [
    {"name":"danaka","math":87,"English":81,"science":94},
    {"name":"sato","math":47,"English":91,"science":84},
    {"name":"ikeda","math":67,"English":71,"science":74},
    {"name":"koike","math":97,"English":61,"science":64},
    {"name":"yamada","math":57,"English":51,"science":54}
    ]

# print(students[1]) 이렇게 하면 리스트에서 1번째 요소를 출력함

print("이름","총점","평균",sep="@@")  # 각각 사이에 @@을 넣는다는말
print("이름","총점","평균",end="@@")  # 이어서 @@을 넣는다는말
print("이름","총점","평균",sep="\t")  # 이거도 end 영향 받아서 이어서 출력됨.
print("이름","총점","평균",sep="\t")

for student in students: #학생 리스트에 요소 하나하나를 student에 넣어가며 반복한다.
    # 현재 student 에는 {"name":"danaka","math":87,"English":81,"science":94} 같은 딕셔너리가 들어있는 상황
    # 딕셔너리 호출 할때는 A : B 라면 A를 호출해야 B가 출력됨 예로 print(student["math"])라고해야 점수 출력됨
    # 정수의 총합과 평균을 구합니다.
    sum_1 = student["math"] + student["English"] + student["science"] # 87 + 81 + 94
    avg_1 = int(sum_1 / 3)
    print(student["name"],sum_1,avg_1,sep="\t")



