class TimeMap:
    # Solution 1:
    # Time complexity: O(logn)
    # Space complexity: O(n)
    
    def __init__(self):
        # use defaultdict to avoid edge case
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # for each key append the pair value
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # return "" if key is not in the dictionary
        if key not in self.dict:
            return ""
        # use the key to find the corresponding array
        array = self.dict[key]
        l, r = 0, len(array) - 1
        res = ""
        
        while l <= r:
            m = (l + r) // 2
            time = array[m][1]
            # if time is smaller than the timestamp,
            # which means the value is valid, update
            # the res variable
            if time <= timestamp:
                res = array[m][0]
                l = m + 1
            else:
                r = m - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)