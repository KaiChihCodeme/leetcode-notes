# 1448

This question is not so hard to implement. This question need to be traversed and find the maximum based on before nodes.
So just use DFS to traverse and always memory the maximum in every base paths.

Second times to do this:
第二次的解法基本上和第一次完全一樣。
不過有幾個比較卡的地方：
1. 一開始我以為是比root大就可以+1, 但其實是要在那個path最大。想了一下才想到可以用tuple將當下最大值帶入
2. 後來發現我只有在>時+1, 但只要>=就應該+1
3. 改進之後，發現root是負數時我會錯。原因是因為我在init時把max定成0, 但因為+1判斷條件是>=, 所以init用root.val就可以了，也能避免負數時判斷錯誤。