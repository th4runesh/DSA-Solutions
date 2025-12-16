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

    def remove_duplicates(self):
        current = self.head
        prev = None
        seen = set()
        while current:
            if current.data in seen:
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(10)
    ll.append(30)
    ll.append(20)
    print("Original Linked List:", ll.display())
    ll.remove_duplicates()
    print("Linked List after removing duplicates:", ll.display())
