# # 방법 1
# y, m, d = input().split('.') #.을 입력하면 그걸 기준으로 나눠서 y m d에 입력값 들어감
# print("{}-{}-{}".format(d,m,y))

# # 방법 2
# y, m, d = input().split('.')
# print(d,m,y,sep='-') # 공백 제거 위해

# s = input()
# for i in range(0,1000):
    # print(s[i])

s = input()
print(s[0:2],s[2:4],s[4:6])