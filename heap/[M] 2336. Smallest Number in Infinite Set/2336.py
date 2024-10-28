import heapq
class SmallestInfiniteSet:

    def __init__(self):
        inp = [i for i in range(1, 1001)]
        self.heap = inp
        self.s = set()

    def popSmallest(self) -> int:
        if self.heap:
            out = heapq.heappop(self.heap)
            self.s.add(out)
            return out
        return None
    # time complexity: O(logn)
    # space complexity: O(n)
        

    def addBack(self, num: int) -> None:
        if num in self.s:
            heapq.heappush(self.heap, num)
            self.s.remove(num)
    # time complexity: O(logn)
    # space complexity: O(1)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)