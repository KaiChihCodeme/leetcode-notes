This question need to seperate odd and even nodes and return the answer linkedlist.

## My Solution
I try to process odd and even in different steps. And initial the new node, it's more crucial but not efficient.
And when I kick this question, I found I make a mistake that I do not use cur to iterate the linkedlist, and I use `ans = ans.next` to move the node which will overwrite the head, and make answer only remain the last step result.

As a result, I need to practice the concept of `head` and how to iterate by assign a new node pointer `cur` or whatever.

## Fine Solution
In the `solution.py`, it provides a very simple and easily implementation, only need to use two node `odd` and `even` to iterate the linkedlist. Then connect `head(odd)` with `even_head`, that would be the answer.