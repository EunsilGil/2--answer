def solution(temperature, A, B):
    answer = 0
    for i in range(A+1, B):     # 한줄 수정
        if temperature[i] > temperature[A] and temperature[i] > temperature[B]:
            answer += 1
    return answer

temperature = [3, 2, 1, 5, 4, 3, 3, 2]
A = 2
B = 7
ret = solution(temperature, A, B)

print("solution 함수의 반환 값은", ret, "입니다.")