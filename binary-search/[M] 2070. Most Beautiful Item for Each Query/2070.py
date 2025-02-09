class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m = {}
        res = []

        # calculate the maximum beauty for each item
        for i in items:
            if i[0] not in m:
                m[i[0]] = i[1]
            else:
                m[i[0]] = max(m[i[0]], i[1])
                
        # sort the keys from map
        keys = sorted(m.keys())

        # update the maximum beauty for each item
        # we update each maximum beauty based on previous beauty
        # which means the new map will store the maximum beauty including the previous keys.
        for j in range(1,len(keys)):
            if m[keys[j-1]] > m[keys[j]]:
                m[keys[j]] = m[keys[j-1]]
    

        for q in queries:
            tmp_res = 0
            if q in m:
                # if q in m, directly get the result
                tmp_res = m[q]
            else:
                if q > keys[0]:
                    # use binary search to find the larget key that is smaller than q
                    l, r = 0, len(keys)
                    while l<r:
                        mid = l + (r-l)//2
                        
                        if keys[mid] < q:
                            l = mid + 1
                        else:
                            r = mid - 1
                    
                    ind = 0
                    if l < len(keys) and keys[l] < q:
                        if l >= 0:
                            ind = l
                    elif keys[l-1] < q:
                        if l-1 >= 0:
                            ind = l-1
           
                    tmp_res = m[keys[ind]]
                        
            res.append(tmp_res)
            
        return res

# time complexity: O(nlogn + qlogn)
# space complexity: O(n)