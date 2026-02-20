from collections import Counter 
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        n = Counter(nums)
        out = []
        for i , j in n.items():
            if j == 2:
                out.append(i)
        return out




        