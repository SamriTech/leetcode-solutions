class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        perm = []
        for i in range(n):
            perm.append(nums[nums[i]])
        return perm
