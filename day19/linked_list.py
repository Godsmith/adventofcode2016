class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, values):
        previous_node = None
        for value in values:
            node = LinkedList.Node(value)
            if previous_node is None:
                self.first = node
            else:
                previous_node.next = node
            previous_node = node
        self.last = node

    def __str__(self):
        list_ = []
        node = self.first
        while node.next is not None:
            list_.append(node.value)
            node = node.next
        list_.append(node.value)
        return str(list_)

    def remove(self, index):
        if index == 0:
            self.first = self.first.next
        else:
            node = self.first
            for _ in range(index - 1):
                node = node.next
            try:
                node.next = node.next.next
            except AttributeError:
                raise IndexError("Index %s does not exist")

    def rotate(self):
        old_first = self.first
        self.first = old_first.next
        old_first.next = None
        self.last.next = old_first
        self.last = old_first
