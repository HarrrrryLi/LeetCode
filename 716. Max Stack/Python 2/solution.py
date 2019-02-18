class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.items.insert(0,x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        return max(self.items)
        

    def popMax(self):
        """
        :rtype: int
        """
        return self.items.pop(self.items.index(max(self.items)))
        
        
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()