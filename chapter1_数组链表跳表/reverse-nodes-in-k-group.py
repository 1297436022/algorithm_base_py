class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

def reverseKGroup(head: ListNode, k: int) -> ListNode:
    dummy = ListNode(0)
    dummy.next = head
    pre, end = dummy, dummy
    while end.next:
        for i in range(k):
            if end:
                end = end.next
        if not end: break
        ##把子链表孤立出来
        start = pre.next
        next = end.next
        end.next = None
        # 进行反转单链表，连接头尾
        pre.next = reverseList(start)
        start.next = next
        # 反转完的start成为下一个pre，end也重置为与pre相同的指针
        pre = start
        end = pre
    return dummy.next

def reverseList(head: ListNode) -> ListNode:
    pre = None
    cur = head
    while cur:
        cur.next, pre, cur = pre, cur, cur.next
    return pre


def reverseKGroup1(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:  # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next

# Notice:
# This is useful when you want to update some values.
# For example, if new value of y needs to be incremented by x,
# and x takes the value of y:
# x, y = y, y + x
# Python does not create temporary variables. It is all done on the stack


def reverseKGroup2(self, head, k):
    # 对 reverseKGroup1 的一个改写
    # Dummy node initialization
    dummy = jump = ListNode(-1)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:
            count += 1
            r = r.next
        if count == k:
            pre, cur = r, l
            for _ in range(k):
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            jump.next = pre
            jump = l
            l = r
        else:
            return dummy.next

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

n = reverseKGroup(n1, 2)
while n:
    print(n.val)
    n = n.next


