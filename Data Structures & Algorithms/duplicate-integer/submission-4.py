class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set()

        for n in nums:
            if n in nodup:
                return True
            nodup.add(n)
        return False
        