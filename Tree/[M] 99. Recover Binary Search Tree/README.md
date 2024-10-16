# 99

I cannot solve this problem in my first saw. But after referring to other's solution, I realize that INORDER in BST will be sorted. So we just need to go through tree by inorder, and we will find two nodes are wild. Then just swap them!

And how to? just record the previous node, and the current node to traverse the wrong nodes, then we will get the answer.