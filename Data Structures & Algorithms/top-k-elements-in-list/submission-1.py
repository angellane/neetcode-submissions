from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if len(nums) == k:
            return list(set(nums))

        counts = Counter(nums)

        return [item for item, _ in counts.most_common(k)]
        