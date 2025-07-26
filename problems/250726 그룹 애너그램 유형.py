# 리트코드 no.49 애너그램 그루핑
import collections

items = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

import numpy as np

def anagram_grouping(words) :
    for i in range(len(words)) :
        inner = []

        if np.unique((list(words[i])))  :
            # 개별 단어에 어떻게 접근해야 할지 감이 안 온다..
          pass

# 책이 제시한 풀이
def group_anagram(words) :
    anagrams = collections.defaultdict(list)
    # collections.defaultdict()로 속이 빈 깡통 딕셔너리 제작
    # 초기 값을 list로 지정해 새 키가 추가되면 자동으로 깡통 리스트가 만들어지도록 설정

    for word in words :
        # sorted로 접근한 개별 문자의 알파벳 순서를 오름차순으로 정렬한 뒤
        # 개별 단어를 딕셔너리의 빈 키 공간에 추가
        # 깡통 리스트가 만들어진 뒤 바로 해당 단어가 원소로 추가
        anagrams[''.join(sorted(word))].append(word)
        # 순서가 달라도 구성 원소가 같으면 그만이라는 점을 활용해 순서대로 나열 후 키로 추가하는 방식 채택
        # 중복 시 리스트에 원소가 추가돼 구성 알파벳만 같으면 한 리스트에 포함

    return list(anagrams.values())


# 리트코드 no.5 가장 긴 팰린드롬
chunk = 'babad'
#... 이건 도대체 어떻게 풀라는 건지;

# 책이 제시한 풀이
def longest_palindrome(things) :
    # 길이가 1이면 무조건 팰린드롬이므로 바로 반환
    # 주어진 문자열이 거꾸로 봐도 같은 문자열이면 바로 반환(기본 팰린드롬 조건)
    if len(things) < 2 or things == things[::-1] :
        return things

    def expand(left, right) :
        while left >= 0 and right < len(things) and things[left] == things[right] :
            left -= 1
            right += 1

        return things[left + 1 : right]
    #
    result = ''
    for i in range(len(things) - 1) :
        result = max(result, expand(i, i+1), expand(i, i+2), key=len)

    return result

# 리트코드 no.1 다시 본 두 수의 합
nums = [2, 7, 11, 15]
target = 9

# 5분 안에 떠오른 유일한 방법.. 브루트 포스
def twosum(items, target) :
    for i in range(len(items)) :
        for j in range(1, len(items)) :
            if items[i] + items[j] == target :
                return i, j

# 다시 써보는 효율적인 풀이
def sum_combo(items, target) :
    for i, n in enumerate(items) :
        # 보수 개념을 도입
        complement = target - n

        # 보수가 남은 리스트 구간에 있다면 그곳의 인덱스를 반환하도록 하는 방식
        # 개인적으로 생각해낼 수 있는 방식의 한계선
        if complement in nums[i+1 :] :
            return [items.index(n), items[i+1 : ].index(complement) + (i + 1)]

# 딕셔너리를 이용한 특이한 풀이법
def sum_combi(numbers, aim) :
    nums_map = {}

    # 딕셔너리에 숫자를 key로, 인덱스를 value로 저장
    for i, num in enumerate(numbers) :
        nums_map[num] = i

        # 만약 보수가 딕셔너리의 key에 있다면 타깃으로 만들 두 수가 정해진 것이므로 그 둘의 인덱스를 바로 반환
        if aim - num in nums_map :
            return [nums_map[aim - num], i]