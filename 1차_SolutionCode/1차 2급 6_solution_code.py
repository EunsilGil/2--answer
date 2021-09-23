def solution(number):
    count = 0
    for i in range(1, number + 1):
        current = i
        while current != 0:
            if current % 10 == 3 or current % 10 == 6 or current % 10 == 9:     # 빈칸 채우기
                count += 1
            current = current // 10
    return count

number = 40
ret = solution(number)

print("Solution: return value of the function is", ret, ".")