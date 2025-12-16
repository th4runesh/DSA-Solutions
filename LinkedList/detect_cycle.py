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
            return new_node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        return new_node

    def has_cycle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    ll = SinglyLinkedList()
    n1 = ll.append(10)
    n2 = ll.append(20)
    n3 = ll.append(30)
    n3.next = n1  # Creating cycle
    print("Cycle Detected?" , ll.has_cycle())
