class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if target not in nums:
                return -1

        while l < r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        return m            
            
        