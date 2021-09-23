def func_a(arr):
    counter = [0 for _ in range(1001)]
    for x in arr:
        counter[x] += 1
    return counter

def func_b(arr):
    ret = 0
    for x in arr:
        if ret < x:
            ret = x
    return ret

def func_c(arr):
    ret = 1001
    for x in arr:
        if x != 0 and ret > x:
            ret = x
    return ret

def solution(arr):              
    counter = func_a(arr)           # 빈칸 채우기
    max_cnt = func_b(counter)       # 빈칸 채우기
    min_cnt = func_c(counter)       # 빈칸 채우기
    return max_cnt // min_cnt

arr = [1, 2, 3, 3, 1, 3, 3, 2, 3, 2]
ret = solution(arr)

print("solution 함수의 반환 값은", ret, "입니다.")