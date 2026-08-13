class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sort = sorted(nums)
        l, r = 0, len(sort) - 1
        if sort:
            while l < r:
                if sort[l] + sort[r] == target:
                    return [l, r]
                if sort[l] + sort[r] < target:
                    l += 1
                else:
                    r -= 1
