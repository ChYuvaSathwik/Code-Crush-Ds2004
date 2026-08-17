class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        found=True
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                s=mid
                found=False
                right=mid-1            
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        

        left1=0
        right1=len(nums)-1
        found1=True
        while left1<=right1:
            mid1=(left1+right1)//2
            if nums[mid1]==target:
                k=mid1
                left1=mid1+1
                found1=False

            elif nums[mid1]>target:
                right1=mid1-1
            else:
                left1=mid1+1
        

        if not found:
            if not found1:
                return [s,k]
        else:
            return [-1,-1]