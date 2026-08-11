class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        sathwik={}
        T=False
        for i in range(len(nums)):
            if nums[i] in sathwik:
                if sathwik[nums[i]]!=i:
                    M=abs(sathwik[nums[i]]-i)
                    if M<=k:
                        T=True
                        break
                    else:
                        del sathwik[nums[i]]
                        sathwik[nums[i]]=i
            else:
                sathwik[nums[i]]=i
        if T:
            return T
        else:
            return T
        