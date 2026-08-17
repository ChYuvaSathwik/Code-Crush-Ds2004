class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        found=False
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                s=mid
                found=True
                return s
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        if not found:
            return left