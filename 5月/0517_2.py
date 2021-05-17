numbers = [1,2,3,4,5,6]
total = 0

# len(numbers) 는 numbers리스트의 길이이므로 6이나옴
# range(len(numbers)) 는 range(6)이란 의미가 됨
# range(6)이기 때문에 i에 0부터 5까지 6번 반복시킴
# numbers[i]이기 때문에 각 리스트 첫번째 부터 6번째까지 하나하나대입됨
for i in range(len(numbers)):
    total += numbers[i]

print(total)
total = 0

# 동일한 예
for i in range(0,len(numbers)):
    total += numbers[i]

print(total)
total = 0

# 동일한 예
for i in numbers:
    total += i

print(total)
total = 0

# 동일한 예
print(sum(numbers))

# 리스트  자동생성
sample = list(range(10)) # list(10)이라하면 에러 뜸
print(sample)

# range(a,b,c)
# a= 시작 숫자
# b = b-1이 마지막 숫자
# c = 몇 단위씩 건너 뛸건지

sample2 = range(10)
print(sample2)
