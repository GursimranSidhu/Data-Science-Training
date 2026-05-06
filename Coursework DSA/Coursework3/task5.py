class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        
        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove node
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert node at front
    def insert(self, node):
        nxt = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nxt
        nxt.prev = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            # remove LRU (last node)
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]


if __name__ == "__main__":
    capacity = int(input("Enter capacity: "))
    lru = LRUCache(capacity)
    
    n = int(input("Enter number of operations: "))
    
    print("Enter operations (put key value / get key):")
    '''example input:
        put 1 1
        put 2 2
        get 1
        put 3 3
        get 2
        put 4 4
        get 1
        get 3
        get 4'''
    
    for _ in range(n):
        operation = input().split()
        
        if operation[0] == "put":
            key = int(operation[1])
            value = int(operation[2])
            lru.put(key, value)
            print("Put done")
        
        elif operation[0] == "get":
            key = int(operation[1])
            print("Output:", lru.get(key))