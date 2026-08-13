class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set()
        p=[]
        for i in nums1:
            if i in nums2 and i not in set1:
                p.append(i)
                set1.add(i)
        return p

