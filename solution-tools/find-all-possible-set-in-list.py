# if we want to find all possible subsets of a list, we can use this pattern:
# inp: [1,3,9,27]
# output: [[], [1], [3], [1, 3], [9], [1, 9], [3, 9], [1, 3, 9], [27], [1, 27], [3, 27], [1, 3, 27], [9, 27], [1, 9, 27], [3, 9, 27], [1, 3, 9, 27]]
# solution1: iterative approach
class solution1:
    def subsets(nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
            
        return result
    
    nums = [1,3,9,27]
    print(subsets(nums))
    
# solution 2: # recursive approach
class solution2:
    def subsets(nums):
        result = []
        def backtrack(start, path):
            if path:
                result.append(path)
                
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
                
        backtrack(0, [])
        return result

    nums = [1,3,9,27]
    print(subsets(nums))