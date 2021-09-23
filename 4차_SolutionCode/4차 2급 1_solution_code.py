def solution(schedule):
    answer = []
    for idx, i in enumerate(schedule):
        if i == "X":                # 빈칸 채우기
            answer.append(idx+1)    # 빈칸 채우기
    return answer

schedule = ["O", "X", "X", "O", "O", "O", "X", "O", "X", "X"]
ret = solution(schedule)

print("solution 함수의 반환 값은", ret, "입니다.")