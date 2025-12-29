# Last updated: 12/29/2025, 1:41:23 AM
class ParkingSystem:
    # Solution 1:
    # Time complexity: O(1)
    # Space complexity: O(1)

    def __init__(self, big: int, medium: int, small: int):
        self.space = [big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.space[carType - 1] -= 1
        return self.space[carType - 1] >= 0


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)