def solution(score):
    answer = [0] * len(score)
    for i in range(len(score)):
        answer[i] = sum(map(lambda x:x > score[i], score))+1
    return answer

def another_solution(score):
    rank = [0] * len(score)

    sort_score = rank.sort()

    for i in range(len(score)):
        for j in range(len(score)):
            if(score[i] == sort_score[j]):
                rank[i] = j
    return rank

score1 = [90, 87, 87, 23, 35, 28, 12, 46]
ret1 = solution(score1)
test1 = another_solution(score1)

print("solution 함수의 반환 값은", ret1, "입니다.")
print("another solution 함수의 반환 값은", test1, "입니다.")

score2 = [10, 20, 20, 30]
ret2 = solution(score2)
test2 = another_solution(score2)

print("solution 함수의 반환 값은", ret2, "입니다.")
print("another solution 함수의 반환 값은", test2, "입니다.")

