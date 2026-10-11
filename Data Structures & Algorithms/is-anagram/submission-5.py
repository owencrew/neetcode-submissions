class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charS = {}
        charT = {}

        for i in s:
            if i in charS:
                charS[i] += 1
            else:
                charS[i] = 1
        
        for i in t:
            if i in charT:
                charT[i] += 1
            else:
                charT[i] = 1

        return charS == charT