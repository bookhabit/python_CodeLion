# smtplib  라이브러리 사용
import smtplib
from email.message import EmailMessage
import imghdr
import re

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # gmail에서 지정한 포트번호

def sendEmail(addr):  # 이메일 보내는 함수
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$"  # 정규표현식
    if bool(re.match(reg,addr)):  # 정규표현식에 부합한 주소(문자열)인지 검사 
        smtp.send_message(message)  # 부합하면 메일 보내기
        print("정상적으로 메일이 발송되었습니다.")
    else:
        print("유효한 이메일 주소가 아닙니다.")


message = EmailMessage() # 이메일 메시지 기능  클래스 (통)
message.set_content("코드라이언 파이썬심화교육 중입니다. ")

message["Subject"] = "코드라이언 파이썬심화교육 메일보내기" # 메일제목
message["From"] = "ckeh08270827@gamil.com" # 발신자
message["To"] = "dlguswls0619@naver.com" # 수신자

# photo=open("codelion.png","rb")
with open("codelion.png","rb") as image : 
    image_file = image.read()

image_type= imghdr.what('codelion',image_file)
# print(image_type)
message.add_attachment(image_file,maintype="image",subtype=image_type)

smtp = smtplib.SMTP_SSL(SMTP_SERVER,SMTP_PORT)
smtp.login("ckeh08270827@gmail.com","ho08270827")
sendEmail(message["To"]) # 메일 보내는 sendEmail 함수 호출
smtp.quit()