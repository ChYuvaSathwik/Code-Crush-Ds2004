class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        else:
            sathwik=n
            seen=set()
            while sathwik>1:
                L=0
                for i in str(sathwik):
                    M=int(i)**2
                    L=L+M
                sathwik=L
                if sathwik==1:
                    return True
                elif sathwik in seen:
                    return False
                else:
                    seen.add(sathwik)