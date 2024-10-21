class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # the classic template for graph DFS
        seen = set()
        ans = 0
        # we need to go through every node, because the graph might not be connected.
        # we just need to expore the connected path, then they will be counted as 1 province.
        # then we go to next node, if node has been seen, we skip it. Otherwise, we explore the connected path.
        # Until we have reached all the nodes
        for i in range(len(isConnected)):
            # must not be seen then we go through, otherwise we skip it.
            if i not in seen:
                # from the current node to explore
                stack = [i]
                seen.add(i)

                while stack:
                    cur = stack.pop()
                    # go thorugh the connected path from current node
                    for ind, j in enumerate(isConnected[cur]):
                            # if j == 1, means there is a connection between cur and ind not in seen, then this node has been connected
                            # we just add to stack and mark it as seen
                            if j == 1 and ind not in seen:
                                stack.append(ind)
                                seen.add(ind)
                # in each loop we can find the connected path, then calculate as 1 province
                ans += 1

        return ans
        
# Time complexity: O(N^2)
# Space complexity: O(N)