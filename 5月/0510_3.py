# 10진수 입력 받고 16진수로 출력
list_a=[]
n = int(input())


def change16(n):
    for i in range(int(n/16)): # 입력한 숫자 나누기 16 한 수 갯수만큼 반복
        list_a.append(n%16)    # 입력한 숫자 나머지 리스트에 저장
        n = n/16                # 입력한 숫자 16나눈 몫의 값으로 대체
        if n < 16:              # 만일 그 값이 16보다 작으면 
            list_a.append(int(n))# 그냥 그값을 리스트에 넣음
            return               # 그리고 끝내
        

change16(n)
print(list_a)




