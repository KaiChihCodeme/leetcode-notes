# 649

https://leetcode.com/problems/dota2-senate/solutions/3483399/simple-diagram-explanation
Refer to this solution, it can accurately solve the problem by implemting two queue.

Why did it add `n` to the last? Due to we eliminate opposite, but we will be eliminate and the priority will be the last, due to we are not able to eliminate the remaining opposite anymore. So by adding the `n` to the queue, we can provides the relationship of priority accurately.