class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sortedS,sortedt = sorted(s), sorted(t)

        if sortedS == sortedt:
            return True
        return False
        
        