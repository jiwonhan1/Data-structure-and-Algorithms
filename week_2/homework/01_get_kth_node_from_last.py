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
        # length = self.get_length_of_linked_list() - k
        # node = self.head
        # for i in range(length):
        #     node = node.next
        # return node
        node = self.head
        node_k = self.head
        for i in range(k):
            node_k = node_k.next

        while node_k is not None:
            node = node.next
            node_k = node_k.next
        return node

    def get_length_of_linked_list(self):
        node = self.head
        length = 1
        while node.next is not None:
            length += 1
            node = node.next
        return length

linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(5)
linked_list.append(4)


# print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
print(linked_list.get_kth_node_from_last(1).data)


