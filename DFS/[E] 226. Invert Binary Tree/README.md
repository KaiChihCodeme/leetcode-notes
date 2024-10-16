# 226

# My Solution
In my solution, I tried to implement DFS to reach all of paths. Then swap them by adding to a new tree called new_t.

I can implement it by myself, but after reading others' solutions, I found my method is too complex and waste space.

I do not need to create a new tree to do the swap task, only to swap exist tree, for example:
![alt text](image.png)
2 will swap with 7, then their children will be swapped to left and right side! So, `(6, 9)` will be in left with `7`, then we just swap to `(9,6)` in the same way (add to stack if we use DFS).

The improved implementation can be found in `226-recursive-fs-bs.py`.