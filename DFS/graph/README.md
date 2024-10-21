# DFS in graph
If we would like to traverse all path from a graph, then choose DFS to do that.

## Template
```python
def dfs_q:
    # create a stack
    dfs = [0]
    # create a set to trace the seen nodes
    seen = set()
    seen.add(0)

    # while stack has value
    while dfs:
        cur = dfs.pop()
        for i in rooms[cur]:
            # if we did not reach this node
            if i not in seen:
                # then add it into stack, we will pop it later
                dfs.append(i)
                # we have seen this, add to set
                seen.add(i)

            ...
    # then seen will show the all nodes we have reached.

```