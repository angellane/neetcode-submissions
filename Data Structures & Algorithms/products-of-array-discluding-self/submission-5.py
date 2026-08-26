class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []
        for i in range(len(nums)):
            product = 1
            l,r = 0, len(nums) -1

            while l < i:
                product *= nums[l]
                l+=1

            while r > i:
                product *= nums[r]
                r-=1
            output.append(product)
        return output

        

                    
        