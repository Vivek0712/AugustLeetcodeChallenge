class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hs = {}
        
        

    def add(self, key: int) -> None:
        hashvalue = hash(key)
        if hashvalue not in self.hs.keys():
            self.hs[hashvalue] = key
            
            

    def remove(self, key: int) -> None:
        hashvalue = hash(key)
        if hashvalue in self.hs.keys():
            self.hs.pop(hashvalue)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashvalue = hash(key)
        if hashvalue in self.hs.keys():
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)