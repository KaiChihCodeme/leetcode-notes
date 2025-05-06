class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        ans = []
        for ind, i in enumerate(numbers):
            dic[i] = ind
            
        for ind,i in enumerate(numbers):
            if target-i in dic:
                ans.append(ind+1)
                ans.append(dic[target-i]+1)
                break
                
        return sorted(ans)

# time complexity: O(Nlog(n))
# space complexity: O(N)