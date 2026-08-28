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
        # sets cannot contain lists, this is a different approach from the last one, where we used tuple to handle duplicate triplets and allow the numbers to be added to the set

        # Go for another approach using 2Pointers next, should be able to get it down to n^2 time

        

        