
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        previous = node.prev
        following = node.next

        previous.next = following
        following.prev = previous

    def add_to_front(self, node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add_to_front(node)

        return node.value

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])

        node = Node(key, value)
        self.cache[key] = node
        self.add_to_front(node)

        if len(self.cache) > self.capacity:
            lru_node = self.tail.prev
            self.remove(lru_node)
            del self.cache[lru_node.key]


if __name__ == "__main__":
    lru = LRUCache(2)

    lru.put(1, 100)
    lru.put(2, 200)

    print(lru.get(1))  # 100

    lru.put(3, 300)    # Evicts key 2

    print(lru.get(2))  # -1
    print(lru.get(3))  # 300
    print(lru.get(1))  # 100
