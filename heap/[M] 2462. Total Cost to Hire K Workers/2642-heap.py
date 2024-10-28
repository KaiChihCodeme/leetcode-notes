import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        i = 0
        j = len(costs) - 1
        heap1 = []
        heap2 = []

        while k > 0:
            # use two heaps to store the smallest candidates from the front and the end
            while len(heap1) < candidates and i <= j:
                heapq.heappush(heap1, costs[i])
                i += 1

            while len(heap2) < candidates and i <= j:
                heapq.heappush(heap2, costs[j])
                j -= 1

            # get the smallest candidate from the front and the end
            t1 = heap1[0] if heap1 else float('inf')
            t2 = heap2[0] if heap2 else float('inf')

            # choose the smaller one then pop, and the next loop will fill the heap until the size is candidates
            # t1 <= t2 due to we pop the smaller one first
            if t1 <= t2:
                res += t1
                heapq.heappop(heap1)
            else:
                res += t2
                heapq.heappop(heap2)

            k -= 1

        return res

# time complexity: O(nlogn)
# space complexity: O(n)