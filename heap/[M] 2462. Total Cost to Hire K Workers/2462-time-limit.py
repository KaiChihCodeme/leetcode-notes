import heapq
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        res = 0
        while k > 0 and costs:
            l = len(costs)

            front = costs[:candidates]
            mid = []
            end = []
            if l-candidates < candidates:
                end = costs[candidates:]
            else:
                mid = costs[candidates:l-candidates]
                end = costs[l-candidates:]

            # min's time complexity is O(n)
            f_min = min(front)
            e_min = min(end) if end else float('inf')
            if f_min > e_min:
                res += e_min
                end.remove(e_min)
            else:
                res += f_min
                front.remove(f_min)

            costs = front + mid + end
            k -= 1

        return res
            
# time complexity: O(n^2)
# space complexity: O(n)