
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1

        heap = []

        for num, count in counts.items():
            if len(heap) < k:
                heapq.heappush(heap, (count,num))
            else:
                heapq.heappushpop(heap, (count,num))

        ret = []
        for count,num in heap:
            ret.append(num)
        return ret
        
        