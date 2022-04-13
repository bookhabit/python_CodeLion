set_lunch = set(["된장찌개", "피자", "제육볶음", "짜장면"])
item = "짜장면"  
#집합은 집합끼리만 연산가능함   집합-문자열 x p
set_lunch = set_lunch-set([item]) #집합자료형으로 할 때는 리스트로 묶어줌
print(set_lunch)
