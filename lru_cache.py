class ListNode:
    def __init__(self, k=0, v=0):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.map = {}   # key -> ListNode

        # sentinel nodes
        self.left = ListNode()   # dummy head (MRU side)
        self.right = ListNode()  # dummy tail (LRU side)
        self.left.next = self.right
        self.right.prev = self.left

    def _delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_front(self, node):
        node.prev = self.left
        node.next = self.left.next
        self.left.next.prev = node
        self.left.next = node

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        n = self.map[key]
        self._delete(n)
        self._add_front(n)   # move to front = recently used
        return n.v

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._delete(self.map[key])
        node = ListNode(key, value)
        self.map[key] = node
        self._add_front(node)

        if len(self.map) > self.cap:
            # remove LRU from back
            lru = self.right.prev
            self._delete(lru)
            del self.map[lru.k]
