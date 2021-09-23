def solution(shirt_size):			#함수 만들기
	answer = [0 for _ in range(6) ]
	for i in shirt_size:
		if i == "XS":
			answer[0] += 1
		elif i == "S":
			answer[1] += 1
		elif i == "M":
			answer[2] += 1
		elif i == "L":
			answer[3] += 1
		elif i == "XL":
			answer[4] += 1
		elif i == "XXL":
			answer[5] += 1
	return answer

shirt_size = ["XS", "S", "L", "L", "XL", "S"]
ret = solution(shirt_size);

print("solution 함수의 반환 값은", ret, "입니다.")
