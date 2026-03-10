class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        l=0
        r=n
        arr=[]
        while l<r and r<len(nums):
            arr.extend([nums[l],nums[r]])
            l+=1
            r+=1
        return arr


