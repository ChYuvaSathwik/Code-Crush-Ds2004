class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            balu=True
            sathwik={}
            praneeth={}
            for i in range(len(s)):
                if s[i] not in sathwik:
                    sathwik[s[i]]=t[i]
                    if t[i] not in praneeth:
                        praneeth[t[i]]=s[i]
                    else:
                        if praneeth[t[i]]!=s[i]:
                            balu=False
                            break
                        else:
                            balu=True
                else:
                    if sathwik[s[i]]!=t[i]:
                        balu=False
                        break
                    else:
                        balu=True
            if balu:
                return balu
            else:
                return balu