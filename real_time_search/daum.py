import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = "http://www.daum.net/"
response=requests.get(url)
#print(response.text[:200])
soup = BeautifulSoup(response.text,"html.parser")
rank = 1
# 새로운 파일에 html 문서를 가져와서 실시간검색어 데이터 공통점 찾아봄
# file =open("daum.html","w",encoding="utf-8") # 파일 생성
# file.write(response.text)
# file.close()


# print(soup.title)
# print(soup.title.string)
# print(soup.span)
# print(soup.findAll("span"))

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다."))

# html 문서에서 모든 a태그이면서 link_favorsch 클래스가진태그 가져오는 코드 작성
# 실시간검색어 다음에 없으니까 다른 검색어 찾아서 혼자 해보기
results = soup.findAll("a","link_favorsch")
search_rank_file = open("rankresult.txt","w",encoding="utf-8")

# 받아온 실시간검색어 태그들 중에서 내용만 꺼내오기
for result in results:
    search_rank_file.write(rank,"위: ",result.get_text(),"\n")
    #print(rank,"위: ",result.get_text(),"\n")
    rank +=1

