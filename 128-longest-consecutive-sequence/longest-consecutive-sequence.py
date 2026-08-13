class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        else:
            sathwik=float("-inf")
            bro1=0
            praneeth=0
            set1=set(nums)
            for i in set1:
                if i-1 not in set1:
                    bro1=bro1+1
                    jas=True
                    praneeth=i+1
                    while jas:
                        if praneeth in set1:
                            bro1=bro1+1
                            praneeth=praneeth+1
                        else:
                            if sathwik<bro1:
                                sathwik=bro1
                                jas=False
                                bro1=0
                            else:
                                jas=False
                                bro1=0
            return sathwik
