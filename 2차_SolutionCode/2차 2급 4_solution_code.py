def solution(words):        # 함수 만들기
    answer = ""
    for w in words:
        if len(w) >= 5:
            answer += w
    if len(answer) < 1:
        answer = "empty"
    return answer

words1 = ["my", "favorite", "color", "is", "violet"]
ret1 = solution(words1);

print("solution 함수의 반환 값은", ret1, "입니다.")

words2 = ["yes", "i", "am"]
ret2 = solution(words2);

print("solution 함수의 반환 값은", ret2, "입니다.")