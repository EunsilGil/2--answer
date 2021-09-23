def solution(N, M):             # 함수 만들기
    total = 0
    for x in range(N, M + 1):
        if x % 2 == 0:
            total += x*x
    return total

N = 4
M = 7
ret = solution(N, M)

print("solution 함수의 반환 값은", ret, "입니다.")