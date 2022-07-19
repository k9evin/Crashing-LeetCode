class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Solution 1:
        # Time complexity: O(nlogn)
        # Space complexity: O(1)
        
        # sort the array base on the units
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        capacity = 0
        
        for box, unit in boxTypes:
            if truckSize >= box:
                capacity += box * unit
                truckSize -= box
            else:
                capacity += truckSize * unit
                break
        
        return capacity
                