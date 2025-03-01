# 1749
This brute-force is easy to figure out. But not easy to optimize in my view.

## DP
I came up with create a dp array, and always find max abs in every steps with nums[i]. But this is not working at all due to sometimes minimum may bigger than maximum sum while abs sum them.

So we need to have two sum -> max and min two dp to find the maximum abs sum.

## Prefix sum
It's not easy to me and I need to understand prefix sum!
solution: https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/solutions/1052527/java-c-python-o-1-space
diagram:
https://www.notion.so/Leetcode-1749-56f6c5e455104d4f85975d1fce12e539