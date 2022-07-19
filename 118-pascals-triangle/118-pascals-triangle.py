class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Solution 1:
        # Time complexity: O(n^2)
        # Space complexity: O(1)
        
        # initialize the first row
        res = [[1]]
        # we can work from the second row to the end
        for i in range(1, numRows):
            # initialize the array filled with 1
            array = [1] * (i + 1)
            # exclude the index filled with 1
            for j in range(1, len(array) - 1):
                # add the value from the prev rows
                array[j] = res[-1][j - 1] + res[-1][j]
            # append the whole array to the result
            res.append(array)
        return res
                
                
            
            