from bs4 import BeautifulSoup
import requests
from datetime import datetime

# 로봇이 아니라고 말해주기 위한 구문
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36'}
url = "https://www.naver.com/"
response = requests.get(url,headers=headers)
#print(response.text)


# test_file = open("test.html","w",encoding="utf-8")
# test_file.write(response.text)
# test_file.close()



# soup = BeautifulSoup(response.text, 'html.parser')
# rank = 1
# # span - item_title
# results = soup.findAll('li',"data-rank")
# print(results)
# # print(response.text)

# search_rank_file2 = open("rankresult2.txt","w",encoding="utf-8")

# print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

# for result in results:
#     search_rank_file2.write(str(rank)+"위:"+result.get_text()+"\n")
#     print(rank,"위 : ",result.get_text(),"\n")
#     rank += 1