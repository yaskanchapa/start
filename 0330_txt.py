# 1000명 이름 키 몸무게 등 만들기
import random
hanguls = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
with open("info.txt","w") as file:
    for i in range(1000):                                  # 0부터 999까지 1천번 i에 넣어가면서 반복시켜
        name = random.choice(hanguls) + random.choice(hanguls) # 반복내용은 for안에서돌아야됨 들여쓰기 주의
        weight = random.randrange(40,100)                  # 랜덤하게 범위 생성 40부터 100까지
        height = random.randrange(140,200)                 # 랜덤하게 범위 생성 140부터 200까지
        file.write("{},{},{}\n".format(name,weight,height))

# 반복문으로 파일 한 줄 씩 읽기
with open("info.txt","r") as file:
    for line in file:                                  # file횟수만큼 반복합니다. line에 넣어가면서
        (name,weight,height) = line.strip().split(",") # 변수를 선언합니다.
        if(not name) or (not weight) or (not height):  # 문제가 있다면 지나감
            continue
        
        # 결과를 계산합니다.
        bmi = int(weight) / ((int(height)/100)**2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"
        
        #출력합니다.
        print('\n'.join(["이름:{}","몸무게:{}","키:{}","BMI:{}","결과:{}"]).format(name,weight,height,bmi,result))
        print()

