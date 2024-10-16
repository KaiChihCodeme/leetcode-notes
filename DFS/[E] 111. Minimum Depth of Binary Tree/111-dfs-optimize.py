# DFS       
def minDepth(self, root):
    if not root:
        return 0
    # res can be set as max_int
    res, stack = 9999, [(root, 1)]
    while stack:
        node, level = stack.pop()
        if node and not node.left and not node.right:
            res = min(res, level)
        if node:
            stack.append((node.left, level+1))
            stack.append((node.right, level+1))
    return res