# 1657
https://leetcode.com/problems/determine-if-two-strings-are-close/?envType=study-plan-v2&envId=leetcode-75

## My first Solution
I take some time to figure out the reletionship from the question. However, if I can find the relationship, it will easily to solve by implementing Hashmap.

In my thought, if length of two words are different, it must be `False`.
And I use two map to count the alphatbet and their counts. Because if all of alphabet and their counts are the same, it must be `True`.
(Here can use Collection.Counter, but i don't want to use library to solve this question)

E.g., word1 = "cabbba", word2 = "abbccc", then `counter_map={"a":2, "b":3, "c":1}, counter_map2={"a":1, "b":2, "c":3}`. Every character can be swap and follow the orginal counts, so if alphbet and counts is the same between two words, it must be `True` 

So, I check the keys must the same.
Moreover, I check the value counts must be the same. If j_list has been swap out, it would be `True`.

In complexity, I think my solution will be `O(N)`.

```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        counter_map = {}
        counter_map2 = {}
        for i in word1:
            if i not in counter_map:
                counter_map[i] = 1
            else:
                counter_map[i] += 1

        for j in word2:
            if j not in counter_map2:
                counter_map2[j] = 1
            else:
                counter_map2[j] += 1

        # validate keys
        if counter_map.keys() != counter_map2.keys():
            return False

        # validate # val
        j_list = list(counter_map2.values())
        for i in counter_map.values():
            if i in j_list:
                j_list.remove(i)
        
        return len(j_list)==0
```

## Refine
```python
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        unique1 = set(word1)
        unique2 = set(word2)

        if unique1 != unique2:
            return False
        
        occur1 = sorted([word1.count(i) for i in unique1])
        occur2 = sorted([word2.count(i) for i in unique2])
        
        if occur1 != occur2:
            return False
        else:
            return True
```
Lots of ppl use set to check keys. Then use count and sorted to verify the value counts.
Concept is similar to mine, but more simplify and efficiency. (But sorted will take more complexity about `O(Nlog(N))`)