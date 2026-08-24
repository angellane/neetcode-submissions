class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #We need to go through the list and see if 2 numbers add up to a target value
        # but we must return the indexes too so that would indicate enum

        hashMap = {}
            

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        