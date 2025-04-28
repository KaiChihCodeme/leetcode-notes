class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        seen = set(supplies)
        dq = deque([(r, ing) for r, ing in zip(recipes, ingredients)])

        prev_size = len(seen) - 1
        while len(seen) > prev_size:
            prev_size = len(seen)
            for _ in range(len(dq)):
                r, ing = dq.popleft()
                
                flag = False
                for i in ing:
                    if i not in seen:
                        dq.append((r, ing))
                        flag = True
                        break
                if not flag:
                    ans.append(r)
                    seen.add(r)
        return ans

# time complexity: O(N * K) where N is the number of recipes and K is the average number of ingredients per recipe
# space complexity: O(N + S) where N is the number of recipes and S is the number of supplies