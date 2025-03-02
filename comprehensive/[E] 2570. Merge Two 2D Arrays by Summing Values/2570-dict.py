class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m = {}

        for i in nums1:
            m[i[0]] = i[1]

        for j in nums2:
            if j[0] in m:
                m[j[0]] += j[1]
            else:
                m[j[0]] = j[1]

        # convert to list
        m = dict(sorted(m.items()))
        res = []
        for k,v in m.items():
            res.append([k,v])

        return res

# time complexity: O(nlogn)
# space complexity: O(n) 