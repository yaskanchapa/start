# map(함수,리스트): 리스트의 요소를 함수에 넣고 새로운 리스트를 구성
# filter(함수,리스트): 리스트의 요소를 함수에 넣고 True인 것으로 새로운 리스트 구성

#변수를 선언합니다.
list_input_a = [1,2,3,4,5]
#map함수 사용합니다. #람다는 자동으로 리턴처리됨
output_a = map(lambda x: x*x, list_input_a) # map(함수,리스트) 리스트 요소를 함수에 넣고 새로운 리스트 작성
print("# map()함수의 실행결과")
print("map(power, list_input_a):",output_a) # 리스트로 안묶어주면 리스트 작성은 안함. map함수는 기존리스트에서 해당함수에 넣고 변형시켜 꺼내오는것. 즉 이터레이터
# next로 꺼내보면 어떨까?
print(next(output_a))
print(next(output_a))
print(next(output_a))
print(next(output_a))
print(next(output_a))
print("map(power, list_input_a):",list(output_a)) # next로 하나씩 꺼냈더니 이경우 리스트에 하나도 안남아 있게 되네
#filter함수 사용합니다.
output_b = filter(lambda x: x < 3, list_input_a)
print("# filter()함수 실행결과")
print("filter(under_3, list_input_a:", output_b)
print("filter(under_3, list_input_a:", list(output_b))