import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, priority, item):
        # Using heapq, lower numbers = higher priority
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        return [item for priority, item in self.queue]

if __name__ == "__main__":
    pq = PriorityQueue()
    pq.enqueue(3, "Task 3")
    pq.enqueue(1, "Task 1")
    pq.enqueue(2, "Task 2")
    print("Priority Queue Items:", pq.display())
    pq.dequeue()
    print("Queue after dequeue:", pq.display())
