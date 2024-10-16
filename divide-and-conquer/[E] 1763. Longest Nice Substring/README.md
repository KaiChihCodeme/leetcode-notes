# 1763

I tried to implement many solution, but it can not fulfill the question. So, I refer to the other's solution due to I cannot find the appropriate relationnship.

## Brute-Force
I think the most important logic is, how to find a continuous lower and upper case. I saw lots of solutions use swapcase() to find the opposite letter to check if it is a nice sub-string. Because if it is, all sub-string should pass the swapcase() check.

So in brute force, we just need to gradually add range to find out all sub-string. Then return the max length one.

## Divide-and-conquer
