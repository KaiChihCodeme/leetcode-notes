# 930

https://www.youtube.com/watch?v=j4JDr4-jvo4

It's not a very straight-forward question and not easy to understand the logic of solution.

I have added the comment into code. However, I think I will come up with weird in the future because why we add res by `r - l + 1` ?

E.g.,
[1,0,1,0,1] goal=2
in our case, we will see the goal <= 2
nums[0] will have 1 possiblities [1]
nums[1] has 2 ([1,0], [0])
nums[2] has 3 ([1,0,1], [0,1], [1])
which is equal than r - l + 1.
