# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/solutions/1646584/java-python-3-toplogical-sort-w-brief-explanation
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Construct directed graph and count the in-degrees
        ingredient_to_recipe, in_degree = defaultdict(set), Counter()
        for rcp, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ingredient_to_recipe[ing].add(rcp)
            in_degree[rcp] = len(ingredient)
        # Topological sort.    
        available, ans = deque(supplies), []
        while available:
            ing = available.popleft()
            for rcp in ingredient_to_recipe.pop(ing, set()):
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    available.append(rcp)
                    ans.append(rcp)
        return ans