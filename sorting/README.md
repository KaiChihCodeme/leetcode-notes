# Sorting
## A common solution
為了去找有沒有重疊，我們可以再透過sorting之後，去iterate每個max_end, 去看他與下一個的最小值是否重疊，就可以得出結論。 （前提是適用在two-dimension array）
ex:
```python
section = 0
max_end = interval[0][1]

# if there is no overlap, it can be a valid rectangle
for start, end in interval:
    if max_end <= start:
        section += 1
    max_end = max(end, max_end)
```