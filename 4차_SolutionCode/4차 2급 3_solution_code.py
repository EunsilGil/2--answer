def func_a(cards, start):
    return cards[start::2]

def func_b(score1, score2):
    if score1 > score2:
        return [1, score1]
    elif score2 > score1:
        return [2, score2]
    else:
        return [0, score1]

def func_c(cards):
    answer = 0
    score_per_cards = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4,
        'e': 5
    }
    for card in cards:
        answer += score_per_cards[card]
    return answer
        
def solution(n, bundle):
    a_cards = func_a(bundle, 0)[:n]     # 빈칸 채우기
    b_cards = func_a(bundle, 1)[:n]     # 빈칸 채우기
    a_score = func_c(a_cards)           # 빈칸 채우기
    b_score = func_c(b_cards)           # 빈칸 채우기
    return func_b(a_score, b_score)     # 빈칸 채우기

n = 4
bundle = "cacdbdedccbb"
ret = solution(n, bundle)

print("solution 함수의 반환 값은", ret, "입니다.")