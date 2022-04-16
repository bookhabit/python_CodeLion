total_list = []

while True :
    question = input("질문을 입력해주세요 : ") 
    if question == "q":
        break
    else :
        total_list.append({"질문" : question , "답변" : ""})  # 키는 "질문" 값은 변수로 지정

for i in total_list :    # 리스트 안에 있는 딕셔너리를 하나씩 꺼냄
    print(i["질문"])     # i는 딕셔너리라서 [" 키 "] 키를 활용하면 값을 바로 가져올 수 있음
    answer = input("답변을 입력해주세요 : ")
    i["답변"] = answer   
    print(i["답변"])
print(total_list)
