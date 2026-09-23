class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
        

        #kth smallest: nums[k - 1]
        #kth largest: nums[len(nums) - k]