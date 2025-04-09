class Solution:
    def isPalindrome(self, s: str) -> bool:
        S=s.lower()
        P=""
        for letter in S:
            if ("A" <= letter <= "Z") or ("a" <= letter <= "z") or ("0" <= letter <= "9"):
                P=P+letter
        Praneeth=True
        Sathwik=len(P)-1
        for i in range(len(P)):
            if P[i]!=P[Sathwik]:
                Praneeth=False
                return Praneeth
                break
            Sathwik=Sathwik-1
        return Praneeth
       """ left=0
        right=len(P)-1
        while left < right:
            if P[left]!=P[right]:
                Praneeth=False
                return Praneeth
                break
            right=right-1
        return Praneeth"""

                


        
        