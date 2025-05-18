"""
void put(int key, int value) Update the value of the key if the key exists. 
Otherwise, add the key-value pair to the cache. If the number of keys exceeds
the capacity from this operation, evict the least recently used key.
"""

from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity if capacity >= 0 else None
        
        

    def get(self, key: int) -> int:
        if key in self:
            self.move_to_end(key)
            return self[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        elif len(self) >= self.capacity:
            self.popitem(last=False)
        self[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)