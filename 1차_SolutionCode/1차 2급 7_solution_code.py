def solution(scores):
    count = 0
    for i in scores:
        if 650 <= scores[i] < 800:          # 한줄 수정
            count += 1
    return count

scores = [650, 722, 914, 558, 714, 803, 650, 679, 669, 800]
ret = solution(scores)

print("solution 함수의 반환 값은", ret, "입니다.")