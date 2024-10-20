class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # because we need a max heap, so we need to store -ct
        rst, arr = '', [(-a, 'a'), (-b, 'b'), (-c, 'c')]
        heapq.heapify(arr)
        
        while True:
            # take the max count char
            ct, char = heapq.heappop(arr)
            # if the max one cnt is 0, break
            if ct == 0: break
            
            # if result has value and the last one is same to here, it means this letter is used twice
            if rst and rst[-1] == char:
                # just pop the second max one
                ct1, char1 = heapq.heappop(arr)
                # if second max is 0, min will be 0, so we need to break
                if ct1 == 0: break
                rst += char1
                ct1 += 1
                # push back the second max one and the max one
                heapq.heappush(arr, (ct, char))
                heapq.heappush(arr, (ct1, char1))
            else:
                # if the max one is not same to the last one, we can use it, and directly use it twice if it >= 2
                rst += char * min(-ct, 2)
                ct += min(-ct, 2)
                heapq.heappush(arr, (ct, char))
        return rst