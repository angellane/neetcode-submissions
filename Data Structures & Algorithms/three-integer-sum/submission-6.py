class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #optimal idea: work through the sorted list of nums and set 2 pointers at the end and next variable, check the triple and if too small l+=1 and too big r-=1. 
        #you also have to make sure you arent adding the same triple to the list again before returning the answer. You do this by incrementing / decrementing a pointer after the loop iteration has executed. 

        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: #this ensure's the 'anchor' value is not a duplicate upon next iteration
                continue 
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l+=1
                elif threeSum > 0:
                    r-=1
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l - 1] and l < r:
                        l+=1
        return res
 
         