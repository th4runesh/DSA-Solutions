class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

def merge_linked_lists(ll1, ll2):
    dummy = Node(0)
    tail = dummy
    a, b = ll1.head, ll2.head
    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    merged_list = SinglyLinkedList()
    merged_list.head = dummy.next
    return merged_list

if __name__ == "__main__":
    ll1 = SinglyLinkedList()
    ll1.append(1)
    ll1.append(3)
    ll1.append(5)

    ll2 = SinglyLinkedList()
    ll2.append(2)
    ll2.append(4)
    ll2.append(6)

    merged = merge_linked_lists(ll1, ll2)
    print("Merged Linked List:", merged.display())

