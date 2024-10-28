# 1277

## BF
Brute force can be imagine by me, but it is really lack of efficient.

## DP
The concept of DP is not difficult to understand.
![alt text](<Draft Book-123.jpg>)

start from (1,1) to calculate the possible squares in every place.
For example:
1 1
1 1 => should be 1+1 * 1 = 2, due to it will contain 1 and 2 squares

0 1
1 1 => it should be 0+1 * 1 = 1, due to it only contain 1 square

1 1
1 0 => it should be 1+1 * 0 = 0, it would not contain any square

and we will get this if the square is complete in n = 3:
1 1 1
1 2 2
1 2 3