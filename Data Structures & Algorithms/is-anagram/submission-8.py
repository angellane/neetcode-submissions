class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case, if not same length return false
        #init 2 hashmap, mapping c to freq
        #loop till length of s
        #counting each value and putting them into the hashmap 
        # then at the end if the counts of keys to values dont match then return false

        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
            
        