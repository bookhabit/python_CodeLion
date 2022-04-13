# for x in range(30): #range는 0부터 30까지 반복
#     print(x)

foods = ["된장찌개","피자","제육볶음"]
print(foods[0])
print(foods[1])
print(foods[2])
for x in foods : #리스트에 있는 값을 하나씩 반복시킴
    print(x)

information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
for x,y in information.items() : #딕셔너리로 for을 사용하면 key와 value 인자 두개 필요   items()함수필요(key와 value를 가져오는 함수)
    print(x)
    print(y)
