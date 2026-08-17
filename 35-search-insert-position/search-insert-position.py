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
                break
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        
        if found:
            return s
        else:
            sathwik=0
            M=False
            for i in nums:
                if target>i:
                    sathwik=sathwik+1
                else:
                    M=True
                    break
            if M:
                return sathwik
            else:
                return sathwik
            