# 리트코드 no.334
## 전구체인 이터레이터를 만드는 reversed와 in-place 메서드 reverse의 차이
import collections


def reverse_d(x) :
    xr = reversed(x)
    return list(xr)

def reverse(x) :
    xr = x.reverse()
    return xr

# print(reverse_d(['h', 'e', 'l', 'l', 'o']))
# print(reverse(['h', 'e', 'l', 'l', 'o']))

## 책이 제시하는 또 다른 풀이
def reversedstring(x) :
    left, right = 0, len(x) - 1
    # 배열 속 글자의 인덱스로 쓸 수를 사전 정의

    while left < right :
        x[left], x[right] = x[right], x[left]
        left += 1
        right -= 1
    # 맨 첫 글자와 맨 끝 글자, 2번째 글자와 n-1번째 글자를 트레이드하도록 강제
    # 허ㅓ..

# 리트코드 no.937 복잡한 순서 재배열
logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']

# 자력 풀이
def ordering(elements) :
    list_alpha = []
    list_digit = []

    for element in elements :
        if element[5].isalpha() :
            list_alpha.append(element)
        else :
            list_digit.append(element)

    # 람다 조건 구체화에 실패
    list_alpha.sort(key=lambda x : x[5])
    final_list = list_alpha + list_digit

    return final_list

# 책이 제시한 풀이
def reorder(stuffs) :
    letters, digits = [], []

    for stuff in stuffs :
        if stuff.split()[1].isdigit() :
            digits.append(stuff)
        else :
            letters.append(stuff)

    letters.sort(key=lambda x : (x.split()[1:], x.split()[0]))
    # lambda에서는 튜플 형태로 값을 묶어서 정렬 순서를 1,2,3순위로 정하거나
    # 동시에 여러 값을 반환하고자 할 때 쓰임

    return letters + digits

# 리트코드 no.819 특정 값을 제외하고 가장 많이 나온 단어 맞히기
paragraph = 'Bob hit a ball, the hit BALL flew far after it was hit'
banned = ['hit']

import re
import collections

# 내 의견 90%, 챗gpt 의견 10%
def return_mode(sentences) :
    words_list = sentences.split()

    new_list = []

    for word in words_list :
        if word and word not in banned :
            # not in... in 조건도 잘 떠올리면서 써야 한다는 교훈을 얻었다
            word = re.sub('[^a-zA-Z0-9]', '', word).lower()
            # re.sub('[^a-zA-Z0-9]', '', x) 패턴으로 특수문자, 공백 지우기 좋았음
            new_list.append(word)

    counter = collections.Counter(new_list)

    return counter.most_common()[0][0]

# 책에 나와 있는 풀이
def find_most_common(sentence, banned) :
    words = [word for word in re.sub('[a-zA-Z0-9]', '', sentence)
             .lower().split() if word not in banned]
    # ㅏ........


    counts = collections.Counter(words)

    return counts.most_common()[0][0]

