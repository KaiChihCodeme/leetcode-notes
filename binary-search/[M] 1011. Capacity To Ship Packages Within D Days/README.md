# 1011

## My Solution
I solved this question by brute force. Follow the question's relationship, I can use iteraly loop to calculate capcity from max(weights). if current capacity - temp_sum - current weight > 0, that means capacity is available for accepting more weights. if == 0, count+=1 and reset the temp. If < 0, that's means capacity is not enough, so count+=1 and temp reset to current weight.

## Binary Search
Due to I tried to use brute force to find out the capacity from max(weights) to nowhere. So it will take O(N^2) to find the answer.

However, if we use binary search to find out the capacity, which will decrease time complexity from O(N^2) to O(NlogN). But how to? After referred to other's solution, the capacity will between max(weights) to sum(weights) => sum(weights) can ship all of weights at one day! So we just need to find out the capacity from max(weights) to sum(weights) by binary search, and define the logic about how to calculate the minimum days in this capacity, then we are able to find the correct capacity.