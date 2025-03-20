# Union Find Data Structure
Union Find (also known as Disjoint Set) is a data structure that keeps track of elements which are split into one or more disjoint sets. It has two main operations:
1. Find: Determines which set a particular element belongs to
2. Union: Joins two sets together by connecting two elements from different sets. 

The data structure is optimized using techniques like path compression in find operations and union by rank/size to maintain balanced trees.

Common applications of Union Find include:
- Finding connected components in a graph
- Detecting cycles in graphs

## In my language
Union Find主要是拿來比對兩個tree甚至graph的root是否相同（是否相連）、他們的parent的關係等
我們可以用Union把兩個tree接起來，並且把短的接上長的tree的root node
並可以用Find去找他們的root node
