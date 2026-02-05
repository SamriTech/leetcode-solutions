class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        sum = 0
        for i in nums:
            sum += i
        y = sum % k
        if y == 0:
            return 0
        else:
            return y
        
        