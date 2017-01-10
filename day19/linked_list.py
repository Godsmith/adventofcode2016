import math


class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.previous = None

    def __init__(self, values):
        previous_node = None
        self.length = len(list(values))
        for i, value in enumerate(values):
            node = LinkedList.Node(value)
            if previous_node is None:
                self.first = node
            else:
                previous_node.next = node
            node.previous = previous_node
            previous_node = node

            if i == math.floor(self.length / 2):
                self.opposite_first = node
        node.next = self.first
        self.first.previous = node

    def __str__(self):
        list_ = []
        node = self.first
        while node.next is not self.first:
            list_.append(node.value)
            node = node.next
        list_.append(node.value)
        return str(list_)

    def remove(self, index):
        if index > 0:
            node = self.first
        else:
            node = self.first.previous
            self.first = self.first.next
        for _ in range(index - 1):
            node = node.next
        node.next = node.next.next
        node.next.next.previous = node

    def rotate(self):
        # if self.length == 1:
        #     return
        self.first = self.first.next

    def remove_opposite_and_rotate(self):
        old_opposite_first = self.opposite_first
        old_opposite_first.previous.next = old_opposite_first.next
        old_opposite_first.next.previous = old_opposite_first.previous

        if self.length % 2 == 0:
            self.opposite_first = old_opposite_first.next
        else:
            self.opposite_first = old_opposite_first.next.next

        self.length -= 1
        self.rotate()
