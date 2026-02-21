class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if i<j and nums[i]==nums[j]:
                    count += 1
        return count
