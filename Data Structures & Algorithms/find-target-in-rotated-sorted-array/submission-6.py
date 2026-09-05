class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]: #this checks which half is sorted so here we know that the left half is sorted
                if nums[l] <= target <= nums[mid]: #so now we check if the target is in the left side, if it is then the right pointer is moved down and if not then the left pointer is moved up, indicating the target is in the right half
                    r = mid - 1
                else:
                    l = mid + 1
            else: #this is if the left is not the sorted side, so we check the right
                if nums[mid] <= target <= nums[r]: #if the target is inbetween the mid and the right boundary we can move the left up as we know that the target is in the right
                    l = mid + 1
                else: #we know the target isnt in the right, so we move the right pointer down to check the left
                    r = mid -1
        return -1

        #this cycle repeats until the mid pointer becomes the target, otherwise our target isnt present so we return -1

        