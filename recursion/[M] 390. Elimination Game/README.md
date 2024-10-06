# 390. Elimination Game
Label: Recursion

## First solution
I used a directly way to implement by using recursion as `390-reach-memory.py`. However, I used a lot of array to store the new list, so it reached the memory limit.

## Fined Solution
This solution referred to other's solution. It's kind of tricky and math. 
The logic defined as the following:
1. `if n == 1` then return 1 as stop condition
2. if is backward, no matter the length of n, it will always the same. E.g., we have n = 9, the final one always be `8`
```
[1,2,3,4,5,6,7,8,9] -> [2,4,6,8]
[1,2,3,4,5,6,7,8] -> [2,4,6,8]
```
3. if is not backward, the final number depends on length of n:
```
[1,2,3,4,5,6,7,8,9] -> [2,4,6,8]
[1,2,3,4,5,6,7,8] -> [1,3,5,7]
```
4. Here use this relationship to constructure the logic of each recursion:
```
n=9: [1,2,3,4,5,6,7,8,9] -> backward [2,4,6,8] -> n will be 8, and the next n is 8//2=4
n=4: [1,2,3,4] -> not backward [1,3], which n%2==0, so 2*[1,2]=[2,4]-1=[1,3], which means 2*n-1 wil be the rule. then n//2=2
n=2: [1,2] -> backward [2], new n is 2//2=1
n=1: reach stop condition return 1
n=2 bottom up: rule is 2 * 1 = 2
n=4 bottom up: rule is 2 * 2 - 1 = 3
n=9 bottom up: rule is 2 * 3 = 6 
```
By the above rule, we can find when we are in backward, we can use `2 * process(n//2, False)` to use recursion to bottom up the result.
And if is not backward, we separate two rules. One is in even, rule would be `2 * process(n//2, True) - 1`. Another is in odd, rule would be `2 * process(n//2, True)`.

As a result, we can get the answer from this rule and bottom up the sub-issue, and get the result we want.