class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        # return str(self.cargo)
        return self.data


# print(Node("text"))
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        node = Node(data, self.head)
        self.head = node
        return node


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


def print_list(node):
    while node:
        print(node)
        node = node.next


# print(print_list(node1))


def print_backward(lists):
    if lists is None:
        return
    print_backward(lists.next)
    print(lists)


# print_backward(node1)
