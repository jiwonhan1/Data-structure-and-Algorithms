class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)
    #
    def get_kth_node_from_last(self, k):
        node = self.head
        node_k = self.head
        for i in range(k):
            node_k = node_k.next

        while node_k:
            node = node.next
            node_k = node_k.next
        return node

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(5)
linked_list.append(4)


# print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last(2).data)


