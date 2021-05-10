a=[5,4,3,2,1]
for i in a:
    print(i)

b=[3,3,3,2,1]
for i in b:
    print(i)

# c=[q,w,e,r,a]는 에러가 난다. ""로 문자열 이란걸 지정해줘야됨
c=["q","w","e","r","a"]
# 반복문에선 꼭 i 가 아니여도 된다.
# : 까먹기 쉬우니까 조심할것
for t in c:
    print(t)

# # 함수를 지정하는것
# def kakeru(n):
#     print(n)
# #이 함수를 실행하면 n에 10이 들어가고 n을 출력하니까 10이나옴
# kakeru(10)

def kansu2(n):
    # for i in n: 이러면 에러남 n에 숫자 5를 넣기 떄문에 에러가나는거임
    # range쓰면 n횟수만큼 반복해줌 단 0부터카운트감
    for i in range(n):
        print(i)
kansu2(5)

# 문제1. 변수를 제곱하는 함수를 만들고 실행시켜라. 결과도 출력이 가능하도록 할 것
first = 0
def jegob(n):
  # global first: :넣을 필요 없음 함수지정시 외부 변수 가져올땐 global을 사용함
    global first
    first = n*n
    print(first)
  # print(number) 이러면 number은 지정된게 없기 때문에 에러남
jegob(10)


