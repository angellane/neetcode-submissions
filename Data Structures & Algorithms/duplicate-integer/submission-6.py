class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()

        for n in nums:
            if n not in hashSet:
                hashSet.add(n)
            elif n in hashSet:
                return True
        return False
        

        # need to check through every value and if it is not in set, add it.
        # if it is already in set return false else true
        