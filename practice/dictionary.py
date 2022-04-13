# ~는 ~다
information = {"고향":"수원","취미":"영화관람","좋아하는 음식":"국수"}
print(information["고향"])  #key로 값을 가져오는법 1
print(information.get("취미")) ##key로 값을 가져오는법 2
information["좋아하는운동"] = "헬스"  #딕셔너리에 key와 value를 추가하는법
print(information)

