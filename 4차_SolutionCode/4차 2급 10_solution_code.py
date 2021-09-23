def solution(scores, cutline):      # 함수 만들기
    answer = 0
    for s in scores:
        if s >= cutline:
            answer += 1
    return answer

scores = [80, 90, 55, 60, 59]
cutline = 60
ret = solution(scores, cutline)

print("solution 함수의 반환 값은", ret, "입니다.")