class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num==1:
            return True
        elif num>=2 and num<=3:
            return False
        else:
            sathwik=False
            left=1
            right=num//2
            while left<=right:
                mid=(left+right)//2
                if mid*mid==num:
                    return True
                elif mid*mid>num:
                    right=mid-1
                elif mid*mid<num:
                    left=mid+1
            if not sathwik:
                return sathwik

