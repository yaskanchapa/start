# map(함수,리스트): 리스트의 요소를 함수에 넣고 새로운 리스트를 구성
# filter(함수,리스트): 리스트의 요소를 함수에 넣고 True인 것으로 새로운 리스트 구성

# 함수를 선언합니다.
def power(item):
    return item*item
def under_3(item):
    return item < 3

# 변수를 선언합니다.
list_input_a = [1,2,3,4,5]

# map()를 사용
output_a = map(power,list_input_a) #리스트a요소를 power함수에 넣음
print("# map()함수의 실행결과")
print("map(power,list_input_a):",output_a)
print("map(power,list_input_a):",list(output_a)) #list로 해줘야 리스트를 만듬. map함수는 이터레이트 같이 기존 리스트를 사용하는거라서
print()

# filter()를 사용
output_b = filter(under_3,list_input_a)
print("# filter()함수의 실행결과")
print("filter(under_3,list_input_a):",output_b)
print("filter(under_3,list_input_a):",list(output_b))