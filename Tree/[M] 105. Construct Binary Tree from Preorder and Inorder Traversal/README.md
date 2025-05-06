# 105

這題我看了蠻久的，我覺得沒要到非常好想出他的solution以及觀察出pre-order nad in-order兩者相關的規律
但看完solution後，還是會有一點點的感覺，他的解法其實就是：
1. 把inorder是否為空作為control condition
2. 如果不為空，我們可以找到preorder的第一個一定就會是父節點，然而我們需要找到這個節點在inorder的哪邊，他就會是mid
3. 找到這個parent之後，我們把它組成一個tree node as x
4. 再來就是去recursion. x的左邊一樣給他preorder, 但inorder就只會有[:mid], 因為以inorder來說，他的左邊就是mid (parent)的左邊
5. 而右邊則會是 [mid+1:], 理由和上面一樣
6. 以這個思路就可以得到答案了，其實方法不難，但我很常會想不到implement的方法，建議可以多回來看一下這題！