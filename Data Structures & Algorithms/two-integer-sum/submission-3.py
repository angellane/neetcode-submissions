class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #can solve with 2 pointers by moving up and down the list comparing elements
        # this is brute force
        for i in range(len(nums)):
            for j in range(i + len(nums)):
                if nums[i] != nums[j] and nums[i] + nums[j] == target:
                    return [i,j]
        return []
        