# 111

## My solution
In my first thought, the recursion come to my mind when I figured out the solution. So, I tried to find all of depth in this tree, then tried to implemnent the DFS and bottom-up concept to find the minimum depth in every possible path.

If we cannnot find any left, right child node, it means we reach the leaf node, so just return depth, when we bottom up, we will get the minimum depth.

A important experience is, I have suffered from how to pass the depth and min_depth, and how to return the required value, I think it may because of lack of familar with recursion. So just keep practicing the recursion-related problems!

## DFS-classic
Due to we need to reach all of the tree nodes, so we can decide to use BFS or DFS. Depends on how to implement.

In DFS, we usually use stack to store the required information. In this example, we use `tuple` to store multiple infromation `(node.left, level+1)` into stack, so we can reach them from DFS paths! Just need to implement how to calculate the result as `res=min(res, level)`. (which reached the leaf node should calculate minimum depth).

## DFS + BFS
DFS only separate the left and right child tries, and we used BFS to find minDepth from each tree.

It's a classic implementation in BFS, used queue to store the required information just similiar with DFS, but reach all paths with different way.