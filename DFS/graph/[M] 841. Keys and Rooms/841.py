class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.seen = set()
        self.seen.add(0)
        key = 0
        
        self.dfs(rooms, key)
        
        return True if len(self.seen) == len(rooms) else False
    
        
    def dfs(self, rooms, key):
        for i in rooms[key]:
            if i not in self.seen:
                self.seen.add(i)
                key = i
                self.dfs(rooms, key)
            else:
                continue

# Time Complexity: O(N+E)
# Space Complexity: O(N)