# 338

It's kind of tricky problem because we need to find out the relation of this problem.

In brute-force solution, we can easily figure out the solution for it.

And in DP solution, it's like this:
1 -> 01
2 -> 10
3 -> 11
4 -> 100

2//2 = 1, and add 0 to "1" result, it would be "10"
3//2 = 1, and add 1 to "1" result, it would be "11"
4//2 = 2, and add 0 to "10" result would be "100"

So, the relationship is:
If N//2 is even, then add 0 to the end of N//2, so cnt should not add 1
If N//2 is odd, then add 1 to the end of N//2, so cnt should add 1