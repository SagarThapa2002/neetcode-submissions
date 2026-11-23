class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """each no of lengths need to be equal for anagrams of each other. """
        if len(s) != len(t):
            return False
        
        count_S, count_T = {} , {}
        for a , b in zip(s,t):
            count_S[a] = count_S.get(a,0) + 1
            count_T[b] = count_T.get(b,0) + 1

        return count_S == count_T
    