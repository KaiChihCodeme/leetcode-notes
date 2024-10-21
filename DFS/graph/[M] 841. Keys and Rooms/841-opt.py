class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dfs = [0]
        seen = set()
        seen.add(0)
        
        while dfs:
            key = dfs.pop()
            for i in rooms[key]:
                if i not in seen:
                    dfs.append(i)
                    seen.add(i)
                    
                if len(seen) == len(rooms):
                    return True
                
        return len(seen) == len(rooms)

# Time complexity: O(N + E)
# Space complexity: O(N) for the stack and seen set