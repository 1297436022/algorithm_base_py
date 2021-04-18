class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __str__(self):
    #     return str(self.val)


def swap_pairs(head):
    dummy = pre = ListNode(0)
    pre.next = head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, a.next, b.next = b, b.next, a
        pre = a
    return dummy.next


def swap_pairs1(head):
    # 递归关键点
    # 1.返回值
    # 2.调用单元做了什么
    # 3.终止条件
    if head is None or head.next is None:
        return head

    next = head.next
    head.next = swap_pairs1(next.next)
    next.next = head
    return next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

r = swap_pairs1(node1)
while r:
    print(r.val)
    r = r.next
