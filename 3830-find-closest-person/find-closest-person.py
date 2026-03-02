class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        one = abs(z-x)
        two = abs(z-y)
        if one > two:
            return 2
        elif one < two:
            return 1
        else:
            return 0