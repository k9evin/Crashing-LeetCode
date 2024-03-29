# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        # 不直接用 nestedList 的引用，是因为不能确定它的底层实现
        # 必须保证是 LinkedList，否则下面的 addFirst 会很低效
        self.list = deque(nestedList)

    def next(self) -> int:
        # hasNext 方法保证了第一个元素一定是整数类型
        return self.list.popleft().getInteger()

    def hasNext(self) -> bool:
        # 循环拆分列表元素，直到列表第一个元素是整数类型
        while self.list and not self.list[0].isInteger():
            # 当列表开头第一个元素是列表类型时，进入循环
            first = self.list.popleft().getList()
            # 将第一个列表打平并按顺序添加到开头
            for i in range(len(first)-1, -1, -1):
                self.list.appendleft(first[i])
        return bool(self.list)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())