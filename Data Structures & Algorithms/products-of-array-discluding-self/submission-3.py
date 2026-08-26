class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product = product*nums[j]
            output[i] = product

        return output
                    
#The difference here and prev solution is that instead of adding a new list entry everytime we have already allocated len(num) indexes to the output array, since the list is full of integers and integers are not immutable we can change the value at specific indexes. 
#This is still not an efficient solution however and the time complexity is too big
