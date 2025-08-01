# 리트코드 no.238 배열의 곱
# 시간이 조금 초과됐으나 자력 해결
nums = [1, 2, 3, 4]

def comb_multiplier(numbers) :
    l = []

    for i in range(len(numbers)) :
        m = 1
        for j in range(len(numbers)) :
            if i != j :
                m *= numbers[j]

        l.append(m)

    return l

# print(comb_multiplier(nums))

# 책이 제시한 풀이
def products(numbers) :
    out = []
    p = 1

    for i in range(len(numbers)) :
        out.append(p)
        p *= numbers[i]

    p = 1

    # 인덱싱을 역순으로 거는 -1에 끝 인덱스를 -1로 거는 창의성
    for i in range(len(numbers) -1, -1, -1) :
        out[i] *= p
        p *= numbers[i]

    return out

# print(products(nums))

#=======================================================================

# 리트코드 no.121
# 자력 해결 실패
nums = [7, 1, 5, 3, 6, 4]

# 책이 제시한 풀이 - 브루트 포스
def max_profit(prices) :
    max_price = 0

    for i, price in enumerate(prices) :
        for j in range(i, len(prices)) :
            max_price = max(prices[j] - price, max_price)

    return max_price

# print(max_profit(nums))

# 2단 구성
import sys

def maxprofit(price) :
    profit = 0
    min_price = sys.maxsize

    for p in price :
        # min 함수와 max 함수로 기존 설정 값을 계속 갱신하도록 하는 방식
        # 반복문 인자를 i, j 튜플로 받아 전개하는 것만큼 자주 나오는 패턴
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)

    return profit

print(maxprofit(nums))
