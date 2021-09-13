# Time complexity: O(1)
# Approach: Dictionary and Bidirection Linked list implementation.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = defaultdict(Node)
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def removeNode(self, d):
        dp, dn = d.prev, d.next
        d.next, d.prev = None, None
        dp.next, dn.prev = dn, dp
    
    def addNode(self, d):
        tmp = self.head.next
        self.head.next, tmp.prev = d, d
        d.prev, d.next = self.head, tmp

    def get(self, key: int) -> int:
        if key in self.cache:
            d = self.cache[key]
            val = d.val
            del self.cache[key]
            self.removeNode(d)
            self.addNode(Node(key, val))
            self.cache[key] = self.head.next
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            d = self.cache[key]
            del self.cache[key]
            self.removeNode(d)
        if len(self.cache)==self.cap:
            del self.cache[self.tail.prev.key]
            self.removeNode(self.tail.prev)
        self.addNode(Node(key, value))
        self.cache[key] = self.head.next


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)