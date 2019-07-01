class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = [[] for _ in range(1024)]

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.remove(key)
        self.map[key & 1023].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        values = [x[1] for x in self.map[key & 1023] if x[0] == key]
        return -1 if len(values) == 0 else values[0]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.map[key & 1023] = [x for x in self.map[key & 1023] if x[0] != key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
