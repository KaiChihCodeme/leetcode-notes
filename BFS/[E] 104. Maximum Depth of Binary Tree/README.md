# 104
Thought: 這題蠻直覺，我會覺得用BFS去掃過一次，因為還是得要每個node都去iterate. 因此使用BFS, 並把depth資訊傳遞下去，往下層就+1，即可得到最深深度。

Challenge: edge case: "[]" 沒有考慮到。