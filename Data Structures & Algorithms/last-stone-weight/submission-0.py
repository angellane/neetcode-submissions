class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = stones
        heapq.heapify(heap)

        #now stones is a heap 

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, second - first)

        return heap[0]
            

        