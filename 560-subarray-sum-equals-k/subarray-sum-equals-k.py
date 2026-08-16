class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sathwik={}
        count1=0
        sathwik[0]=1
        prefix=0
        for i in nums:
            prefix=prefix+i
            L=prefix-k
            if L in sathwik:
                count1=count1+sathwik[L]
            
            sathwik[prefix]=sathwik.get(prefix,0)+1
        return count1