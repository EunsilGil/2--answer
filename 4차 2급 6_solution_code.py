def solution(point):
	answer = 0
	if point >= 1000:
		answer = point - point%100
	return answer

## 오답