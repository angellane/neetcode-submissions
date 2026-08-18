class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## initial attempt just to get something thrown out there, very wrong but something to come back to
        numsSort = sorted(nums)
        l,r = 0, len(numsSort) - 1
        res = []
        x = 0

        while l < r:
            if numsSort[l] != numsSort[r] and (numsSort[l] + numsSort[x] + numsSort[r]) < 0:
                l+=1
                numsSort[x] = numsSort[l +1]
            elif numsSort[l] != numsSort[r] and (numsSort[l] + numsSort[x] + numsSort[r]) > 0:
                r-=1
                numsSort[x] = numsSort[r-1]
            
        if sum(numsSort[l], numsSort[r], numsSort[x]) == 0:
            return [numsSort[l], numsSort[r], numsSort[x]]


        