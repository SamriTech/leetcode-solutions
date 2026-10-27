class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        ans = set()
        for i in nums:
            if i in ans:
                return True
            
            ans.add(i)
        return False        