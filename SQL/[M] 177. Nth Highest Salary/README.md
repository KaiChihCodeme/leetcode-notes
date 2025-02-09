# 177

In this question, the most important concept is (LIMIT and OFFSET).

## LIMIT
LIMIT is like (index, cnt). So `LIMIT 1` will only return 1 result based on `order by DESC`.
And if we set to `LIMIT 1,3`, it will return index 1, and after it with count 3. (if all data is `5,4,3,2,1`, it will return `4,3,2`.

## OFFSET
We can ignore number of data by using OFFSET. E.g., if offset set to 2, and data is `5,4,3,2,1`, limit is 1, it will return `3` (ignore 5 and 4).
