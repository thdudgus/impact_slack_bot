# 상담 완료율
def completeRate():
    # TODO 상담 완료율 계산
    # 예시 데이터
    total_consultations = 100  # 총 상담 건수
    completed_consultations = 80  # 완료된 상담 건수
    if total_consultations == 0:
        return 0  # 총 상담 건수가 0이면 완료율은 0
    completion_rate = completed_consultations / total_consultations
    return completion_rate * 100  # 퍼센트로 반환