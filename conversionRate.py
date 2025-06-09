# 신규 고객 전환율
def conversationRate():
    # TODO 신규 고객 전환율 구하기
    # 신규 고객 전환율 = 신규 고객 수 / 전체 방문자 수
    new_customers = 1000  # 예시: 신규 고객 수
    total_visitors = 5000  # 예시: 전체 방문자 수
    if total_visitors == 0:
        return 0  # 방문자가 없으면 전환율은 0
    conversion_rate = new_customers / total_visitors
    return conversion_rate * 100  # 퍼센트로 반환