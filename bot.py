import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
from consultation import consultaion
from sales import sale
from sales import pureSals
from consultedCustomer import consultedCustomer
from fee import feePerPerson
from fee import feePerCase
from signupNum import signupNum
from conversionRate import conversionRate
from completeRate import completeRate
from datetime import datetime


# .env 로드
load_dotenv()

token = os.getenv("SLACK_BOT_TOKEN")
channel = os.getenv("SLACK_CHANNEL_ID")
client = WebClient(token=token)

def combine(consultaion, sale, pureSals, consultedCustomer, feePerPerson, feePerCase, signupNum, conversionRate, completeRate):
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day - 1
    return (
        f"{year}년 {month}월 {day}일 소울톡 지표\n"
        f"상담 건수: {consultaion}건\n"
        f"매출: {sale}쿠키\n"
        f"순매출: {pureSals}쿠키\n"
        f"상담 고객 수: {consultedCustomer}명\n"
        f"인당 상담료: {feePerPerson}쿠키\n"
        f"건당 상담료: {feePerCase}쿠키\n"
        f"가입 회원: {signupNum}명\n"
        f"신규 고객 전환율: {conversionRate}%\n"
        f"상담 완료율: {completeRate}%\n"
        f"오늘도 즐거운 하루 보내봐요!😊\n"
    )

def send_daily_message():
    try:
        combineResult = combine(consultaion(), sale(), pureSals(), consultedCustomer(), feePerPerson(), feePerCase(), signupNum(), conversionRate(), completeRate())
        response = client.chat_postMessage(
            channel=channel,
            text=combineResult
        )
        print("메시지 전송 성공:", response["ts"])
    except SlackApiError as e:
        print("Error sending message:", e.response["error"])

if __name__ == "__main__":
    send_daily_message()
