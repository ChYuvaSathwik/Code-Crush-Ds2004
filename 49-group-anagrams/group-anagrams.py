class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sathwik={}
        ok1=[]
        for i in strs:
            bro1=sorted(i)
            M=""
            for k in bro1:
                M=M+k
            if M in sathwik:
                sathwik[M].append(i)
            else:
                sathwik[M]=[i]
        for j in sathwik:
            ok1.append(sathwik[j])
        return ok1