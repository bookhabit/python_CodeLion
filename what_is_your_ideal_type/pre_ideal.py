# 먼저 코드 짜보기
# 리스트 딕셔너리 사용  
que_list = []
toatl_list = {}
while True:
    que=input("질문을 입력해주세요 : ")
    if que == "q" :
        break
    else:
        que_list.append(que)
    

for i in range(len(que_list)):
    print(que_list[i])  # 질문 출력해주기
    ans = input(">> 답변을 입력해주세요 : ")
    
    toatl_list[que_list[i]] = ans  # 딕셔너리 키에 = 사용자가 답변한 값 추가
print(toatl_list)


