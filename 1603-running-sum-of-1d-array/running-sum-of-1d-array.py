class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sathwik=0
        P=[]
        for i in nums:
            sathwik=sathwik+i
            P.append(sathwik)
        return P
        