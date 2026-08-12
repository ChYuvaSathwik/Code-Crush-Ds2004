class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(s)!=len(pattern):
            return False
        else:
            balu=True
            sathwik={}
            praneeth={}
            for i in range(len(pattern)):
                if pattern[i] not in sathwik:
                    sathwik[pattern[i]]=s[i]
                    if s[i] not in praneeth:
                        praneeth[s[i]]=pattern[i]
                    else:
                        if praneeth[s[i]]!=pattern[i]:
                            balu=False
                            break
                        else:
                            balu=True
                else:
                    if sathwik[pattern[i]]!=s[i]:
                        balu=False
                        break
                    else:
                        balu=True
            if balu:
                return True
            else:
                return False