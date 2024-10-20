# 1405

I cannot solve this problem. In the begining, I use logic condition to solve it, but it has a very complext logic, so it is not easy to implement.

## straightforward logic solution
I refer to other's solution, it provided a clear solution with condition, which is kind of similar to my thoughts, but I just cannot implement it.

It use sum to control the counting of loop, and use current index to store the string to avoid appear over 3 times.

And it's important that we always write the letter which has the max number, and we need to write it twice. Until the max is done, we need to start to fulfill another letter.

Another important points are, the first, we need to figure out how to write other letter while the max is done. So it control by if one of letter has twice, then write the current one. The second, we need to decide when to set the index to the 0. Once we write A, we only need to record cur_a, and set cur_b, cur_c to 0. so it will go to write other letter every round.

like this:
```
Input
a = 2
b = 2
c = 1

Output
"ababc"
```

## Heap
I forgot how to use heap to find the max one. But the key concept in this question is, find the max one always! And that is I have done.

And just use max heap to get the max one, and implement the logic to prevent third continous char. If we encounter it, then find the second one and write it.

The stop condition is impoartant as well. The stop condition will be when max one count is 0, and the second max one is 0 (that means 2, 3 count is 0)