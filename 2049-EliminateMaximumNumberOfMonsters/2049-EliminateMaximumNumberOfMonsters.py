# Last updated: 12/29/2025, 1:40:49 AM
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = []
        count = 1

        for i in range(len(dist)):
            time.append(dist[i] / speed[i])

        time.sort()
        
        for i in range(1, len(time)):
            if time[i] > i:
                count += 1
            else:
                break

        return count
        
        

