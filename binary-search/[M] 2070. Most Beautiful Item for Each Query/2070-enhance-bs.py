class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        m = {}
        res = []

        for i in items:
            if i[0] not in m:
                m[i[0]] = i[1]
            else:
                m[i[0]] = max(m[i[0]], i[1])
                
        keys = sorted(m.keys())

        for j in range(1,len(keys)):
            if m[keys[j-1]] > m[keys[j]]:
                m[keys[j]] = m[keys[j-1]]
    

        for q in queries:
            tmp_res = 0
            if q in m:
                tmp_res = m[q]
            else:
                if q > keys[0]:
                    # use binary search to find
                    l, r = 0, len(keys)
                    ind = 0
                    while l<r:
                        mid = l + (r-l)//2
                        
                        if keys[mid] < q:
                            # we should not use l to ind
                            # we should update ind to mid when keys[mid] < q is fulfilled
                            # due to in the last step, l will add 1 and not fullfilled keys[l]<q
                            ind = mid
                            l = mid + 1
                        else:
                            r = mid
           
                    tmp_res = m[keys[ind]]
                        
            res.append(tmp_res)
            
        return res