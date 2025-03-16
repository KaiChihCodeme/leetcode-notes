# 2560
House Robber series always steal non-continuous house.

In the previous question I have resolved: 198. House Robber, It want to find the maximum amount of money you can rob. So we use DP to solve this problem as max-min problem.

And in this case, we want to find a minumium capacity to stole houses, which is a min-max problem and need to use binary search to solve this problem.

## Min-Max Problem
A min-max problem involves finding the minimum value that satisfies a maximum constraint, or vice versa. In this case, we need to find the minimum capacity (capability to rob) that allows us to rob at least k houses, where the capacity represents the maximum value we can steal from any single house.

## Max-Min Problem
A max-min problem involves finding the maximum value that satisfies a minimum constraint. For example, in the original House Robber problem, we needed to find the maximum amount of money we could steal while satisfying the constraint of not robbing adjacent houses.

## Possible Algorithms
- Binary Search
- Dynamic Programming
- Greedy Algorithm