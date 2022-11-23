from heapq import heappush, heappop
class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        self.size = 0
        
    def addNum(self, num: int) -> None:
        heappush(self.minHeap, num)
        
        
        if self.minHeap and self.maxHeap and self.minHeap[0] < num:
            heappush(self.maxHeap, -heappop(self.minHeap))
        heappush(self.maxHeap, -num)
        while len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
            
        self.size += 1
            
    def findMedian(self) -> float:
        if self.size % 2:
            return -self.maxHeap[0]
        else:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()