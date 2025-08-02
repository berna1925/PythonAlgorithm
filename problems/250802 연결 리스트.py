# inputs = input('insert numbers or alphabets :')

def isPalindrome(stuffs) :
    if stuffs != stuffs[::-1] or not stuffs :
        return False
    else :
        return True


# ListNode 자료형
class ListNode() :
    def __init__(self, val=0, next=None):
        self.val = val
        # 자기 자신에게는 val로 값을 부여해 객체화하고
        # next를 써서 자식 노드와 연결할 수 있도록 설정
        self.next = next

class solution() :
    def ispalindrome(self, head : ListNode) :
        q = []

        if not head :
            return True

        node = head

        while node is not None :
            q.append(node)
            node = node.next

        while len(q) > 1 :
            if q.pop(0) != q.pop() :
                return False

        return True

# deque 자료형 풀이
from collections import deque
def check_if_palindrome(head) :
    q = deque()

    if not head :
        return True

    node = head
    while node is not None :
        q.append(node.val)
        node = node.next

    while len(q) > 1 :
        if q.popleft() != q.pop() :
            return False

    return True

node_third = ListNode('lock')
node_second = ListNode('martin', node_third)
node_init = ListNode('bobby', node_second)

print(check_if_palindrome(node_init))

# print(node_init.next.next.val)

class Solution() :
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, l1, l2) :
        if not l1 or (l2 and l1.val > l2.val) :
            l1, l2 = l2, l1

        if l1 :
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1

