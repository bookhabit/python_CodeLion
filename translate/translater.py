from googletrans import Translator

translator = Translator()

# sentence = "안녕하세요"
sentence = input("번역을 원하는 문장을 입력하세요 : ") # 어떤 언어인지 감지할 문장
detected = translator.detect(sentence)  # 어떤 언어인지 응답값

# print(detected.lang)
print("ex) 한국어:ko 영어:en 프랑스어:fr 베트남어:vi 스페인어:es 힌두어:hi")
ctr = input("번역을 원하는 나라를 선택해주세요 : ")
result = translator.translate(sentence,ctr) # 어떤 언어로 번역해줌 

print("=======출력결과=======")
print(detected.lang,":",sentence)  # 감지할 문장  언어 : 문장
print(result.dest,":",result.text) # 번역한 문장  언어 : 문장
print("======================")
