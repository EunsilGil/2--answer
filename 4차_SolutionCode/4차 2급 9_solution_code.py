def solution1(height):               # 함수 만들기
    count = 0
    dx = [ -1, 1, 0, 0 ]
    dy = [ 0, 0, -1, 1 ]
    for i in range(4):
        for j in range(4):
            is_danger = True
            for k in range(4):
                if 0 <= i+dx[k] and i+dx[k] < 4 and 0 <= j+dy[k] and j+dy[k] < 4:
                    if height[i+dx[k]][j+dy[k]] <= height[i][j]:
                        is_danger = False
            if is_danger:
                count += 1
    return count

def solution2(height):
    count = 0
    for x in range(4):  # 0~3 인덱스 반복
        for y in range(4):  # 0~3 인덱스 반복
            # [x][y]가 위쪽보다 크면 pass
            if x > 0 and height[x-1][y] < height[x][y]:
                pass
            # [x][y]가 아래쪽보다 크면 pass
            elif x < 3 and height[x+1][y] < height[x][y]:
                pass
            # [x][y]가 왼쪽보다 크면 pass
            elif y > 0 and height[x][y-1] < height[x][y]:
                pass
            # [x][y]가 오른쪽보다 크면 pass
            elif y < 3 and height[x][y+1] < height[x][y]:
                pass
            # 조건을 만족하지 못하고 작은 경우, count가 1 증가
            else:
                count += 1
    return count

height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
ret1 = solution1(height)
ret2 = solution2(height)

print("solution1 함수의 반환 값은", ret1, "입니다.")
print("solution2 함수의 반환 값은", ret2, "입니다.")