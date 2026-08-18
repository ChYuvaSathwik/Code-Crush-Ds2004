class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left=0
        right=len(nums)-1
        if len(nums)==1:
            return 0
        elif len(nums)==2:
            if nums[0]>nums[1]:
                return 0
            else:
                return 1
        while left<=right:
            mid=(left+right)//2
            if mid==0:
                if len(nums)>=2 and nums[mid]>nums[mid+1]:
                    return mid
                else:
                    left=mid+1
            elif mid==len(nums)-1:
                if len(nums)>=2 and nums[mid]>nums[mid-1]:
                    return mid
                else:
                    right=mid-1
            elif nums[mid]>nums[mid+1] and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid]>nums[mid+1]:
                right=mid-1
            elif nums[mid]>nums[mid-1]:
                left=mid+1
            else:
                left=mid+1
            



