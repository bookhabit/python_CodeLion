information = {"고향":"수원", "취미":"영화관람","좋아하는 음식":"국수"}
foods = ["된장찌개", "피자", "제육볶음"]

information["특기"] = "피아노"
information["사는 곳"] = "서울"
print(information)
print(len(information))
del information["좋아하는 음식"] #딕셔너리 key value 삭제하기
print(information)
print(foods[0])
print(foods[-2])
foods.append("김밥")
print(foods)
del foods[1]  #리스트에서 값 삭제하기
print(foods)