class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = sorted((nums[i], nums[j], nums[k]))

                        if triplet not in output:
                            output.append(triplet)

        return list(output)

        #brute force solution - run time of doom and despair
        # since we are only dealing with 3 elements and they wont increase as nums increases we arent adding nlogn time, it remains n^3
        # 

        

        