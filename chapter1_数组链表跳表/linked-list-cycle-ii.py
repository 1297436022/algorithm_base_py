class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

def has_cycle_ii(head):
    walker = head
    runner = head

    while runner.next is not None and\
            runner.next.next is not None:
        walker = walker.next
        runner = runner.next.next
        if walker == runner:
            q = head
            while q != walker:  #
                walker = walker.next  #
                q = q.next  #
            return walker

    return None


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n3

print(has_cycle_ii(n1))


