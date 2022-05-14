# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
import requests
import json

city = "Busan"
apiKey = "f94c58fb695ce20e76a14647d27a584a"
lang = "kr"
api = f"""https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&lang={lang}"""

result=requests.get(api)
data = json.loads(result.text)
#print(result.text)  응답값 확인
# print(type(result.text))  응답값의 자료형확인
# print(type(data))  json형태로 변환한 응답값의 자료형확인

print(data["name"],"의 날씨입니다.")
print("날씨는",data["weather"][0]["main"],"입니다.")
print("현재 온도는",data["main"]["temp"],"입니다.")
print("하지만 체감 온도는 ", data["main"]["feels_like"],"입니다")
# 최저 기온 : main - temp_min
print("최저 기온은 ",data["main"]["temp_min"],"입니다")
# 최고 기온 : main - temp_max
print("최저 기온은 ",data["main"]["temp_max"],"입니다")
# 습도 : main - humidity
print("습도는",data["main"]["humidity"])
# 기압 : main - pressure
print("기압은",data["main"]["pressure"])
# 풍향 : wind - deg
print("풍향은",data["wind"]["deg"])
# 풍속 : wind - speed
print("풍속은",data["wind"]["speed"])