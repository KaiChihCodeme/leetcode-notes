# 124

這題我其實一開始看不太懂它到底是要加起來哪些東西，所以我一直不知道到底要怎麼進行。
但看了solution之後，發現他應該就是一條path的sum,加起來要最大的就是答案

因此我參考的這個解法，他就是透過recursion的方式，並且有些比較特殊的觀察，只要記住他的規律，就可以解出來。
1. 首先我們只需要去觀察left and right的gain就好。如果他們是負的，我們就沒有必要加上她，會讓我們得sum變少
2. 再來是我們會希望先到leaf node去做計算，這樣往回推才不會有漏算的地方（畢竟他是path, 要從leaf開始）。看到“回推”，那就是recursion了！
3. 再來就是我們剛剛提到，我們只在意左邊和右邊的gain, 因此要讓他去和0去做max, 如果negative就ignore.
4. `cur_sum` 的算法則是將目前節點.val去加上左右的gain, 就可以得到目前的sum了！
5. 再來就是去紀錄max ans
6. 這裡也是原先我很confuse的地方，就是為什麼recur的return value會是`node.val+max(gain_left, gain_right)`??? 其實就是因為，我們回傳回去是給上上層去參考的，但對於上上層來說，他的下下層我們不會考慮兩邊，只會考慮依邊，這樣才是path的路線。因此我們才會在這一層的左右去挑一個大的作為reference path去return給上上層。 （這邊之後如果忘記在寫啥，可以再多想一下什麼事上上層！）

ref: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram