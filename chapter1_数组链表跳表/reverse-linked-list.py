
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


def reverse_list(head: ListNode) -> ListNode:
    """
    :type head: ListNode
    :rtype: ListNode
    """
    cur, prev = head, None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next  # see down
        # 记录当前节点的下一个节点
        # tmp = cur.next
        # 然后将当前节点指向pre
        # cur.next = prev
        # pre和cur节点都前进一位
        # prev = cur
        # cur = tmp
    return prev
# cur, prev, cur.next = cur.next, cur, prev
# The order to run an expression like a, b, c = b, c, a is 4th, 5th, 6th = 1st, 2nd, 3rd in Python.
# So on the left side of your equation cur, prev, cur.next = cur.next, cur, prev,
# cur updates before cur.next so the 'cur' in cur.next has been changed in 4th operation


def reverse_list1(head):

    if head is None or head.next is None:
        return head

    cur = reverse_list1(head.next)
    head.next.next = head
    head.next = None
    return cur


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

r = reverse_list1(node1)
while r:
    print(r.val)
    r = r.next


