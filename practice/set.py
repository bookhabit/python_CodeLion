#집합    
#데이터가 중복되는 것을 방지하기 위함 > 순서가 없고 중복을 제거해준다
menu1 = set(["된장찌개", "피자", "제육볶음"])
menu2 = set(["된장찌개", "떡국", "김밥"])


#합집합 (집합+집합) > 중복은 없음
menu3 = menu1 | menu2
print(menu3)
#차집합 (집합에서 겹치는 부분을 뺴준 나머지)
menu4 = menu1 - menu2
print(menu4)
#교집합 (겹치는 부분만)
menu5 = menu1 & menu2
print(menu5)
