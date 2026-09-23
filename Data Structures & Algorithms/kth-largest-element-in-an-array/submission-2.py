class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = nums
        heapq.heapify_max(maxHeap)

        while len(maxHeap) > k:
            heapq.heappop_max(maxHeap)
        
        return maxHeap[0]
        
#heapq.heappush_max(maxHeap, x)
#heapq.heappop_max(maxHeap)
#heapq.heappushpop_max(maxHeap, x)
#heapq.heapreplace_max(maxHeap, x) 
#Max Heap Notes