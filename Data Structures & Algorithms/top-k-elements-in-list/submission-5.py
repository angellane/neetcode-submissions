class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        MostCommons = counter.most_common(k)
        listt = []

        for x in range(k):
            New = MostCommons[x][0]
            listt.append(New)
        return listt
        