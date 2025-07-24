# # items로 키와 밸류 동시 반환
# for k, v in {'role1' : 'manager', 'role2' : 'salesman'}.items() :
#     print(k, v)
#
# # 리스트 속 원소의 개수를 세어주는 collections.Counter
# import collections
#
# a = [1, 3, 0, 2, 0, 1, 2, 3]
# count = collections.Counter(a)
# print(count)
import collections

# leetcode Q#125 valid palindrome

x = 'A man, a plan, a canal: Panama'

# 스스로 생각해본 풀이
# def check_palindrome(sentence) :
#     space = []
#
#     for i in range(len(sentence)) :
#         if sentence[i].lower() != sentence[i].upper() :
#             space.append(sentence[i])
#         elif int(sentence[i]) :  # 여기서 에러 나서 진행 안 됨
#             space.append(sentence[i])
#
#     return space

# 책이 제시한 풀이 1

def check_if_palindrome(sentence) :
    space = []

    for char in sentence :
        if char.isalnum() :
            space.append(char.lower())

    if space == space[::-1] :
        return True
    else :
        return False

# 챗gpt가 간소화한 풀이
def isPalindrome(self, s: str) -> bool:
    filtered = [char.lower() for char in s if char.isalnum()]
    return filtered == filtered[::-1]

# 풀이2
def isPalindrome(self, s) :
    strs : Deque = collections.deque()

    for char in s :
        if char.isalnum() :
            strs.append(char.lower())

    while len(strs) > 1 :
        if strs.popleft() != strs.pop() :
            return False

    return True

# 풀이3
import re

def isPalindrome(self, s) :
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

