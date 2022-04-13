import random
import time

lunch = ["된장찌개","피자","제육볶음","짜장면"]
while True: #메뉴추가
    print(lunch)
    user_menu=input("음식을 추가해주세요 : ")
    if (user_menu == "q"): #q를 입력하면 while문 break
        break
    else :
        lunch.append(user_menu) #입력한 값을 lunch에 추가
print(lunch)

set_lunch = set(lunch) #중복되는 음식 제거 - 집합자료형

while True : #메뉴 삭제
    print(set_lunch) 
    item = input("음식을 삭제해주세요 :")
    if (item =="q"):
        break
    else :
        set_lunch=set_lunch - set([item]) #입력한 값을 차집합 연산으로 삭제
        
print(set_lunch,"중에서 선택합니다")
print("5")
time.sleep(1) 
print("4")
time.sleep(1) 
print("3")
time.sleep(1) 
print("2")
time.sleep(1) 
print("1")
time.sleep(1) 

print(random.choice(list(set_lunch))) #리스트로 변환  random으로 하나 뽑음