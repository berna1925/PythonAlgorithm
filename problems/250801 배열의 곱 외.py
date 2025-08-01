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
