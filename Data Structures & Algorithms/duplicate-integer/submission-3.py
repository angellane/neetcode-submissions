class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodup = set()

        for i in range(len(nums)):
            if nums[i] in nodup:
                return True
            nodup.add(nums[i])
        return False
        