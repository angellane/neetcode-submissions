class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                # map count to values where count is the index of the list, you can then move down the list checking if the value isnt empty, if it isnt take the value for everything until you have K values
#array for bucket sort and hashmap for counting occurences
# freq[c].append(n) - n occurs c number of times
        