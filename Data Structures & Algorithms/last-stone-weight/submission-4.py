
#we for sure want to use a max heap for this problem 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        #now stones is a heap 

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if second > first:
                heapq.heappush(heap, first - second)

        
        stones.append(0)
        return abs(heap[0])


        #not passing some test cases
            

        