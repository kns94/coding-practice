class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ms = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.ms.setdefault(key, 0)
        self.ms[key] = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        
        psum = []
        for k, v in self.ms.iteritems():
            if len(k) >= len(prefix):
                if k[:len(prefix)] == prefix:
                    psum += [self.ms[k]]
        return sum(psum)

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert("apple", 3)
print obj.sum("ap")
obj.insert("app", 2)
print obj.sum("ap")