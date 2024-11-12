# Binary Search

## l, r
l usauly set to `0` as left index, and r will set to `len(list)` (for `while l < r`) or `len(list)-1` (for `while l <= r`) as right index.
middle will be caculate as `l + (r-l) // 2` to avoid int overflow.

## [l, r)
`open left, close right`
`包含左邊界，不包含右邊界`
- if we want to find target, we can use binary search. Once the target has been found, directly break the while loop.
- And if we want to find a specific condition, such as find the first negative number in a sorted array. We can use binary search to do this. We just set 0 as target, even target cannot be found, the left index also can be the answer of the first negative index.

refer to: `1351-bs-best`
```python
l, r = 0, len(i)
while l < r:
    m = l + (r-l) // 2

    # should >= 0 to move left index, because we only need to find out the first negative num
    if i[m] >= 0:
        l = m + 1
    else:
        r = m
```

## [l, r]
`open left, open right`
`左右邊界都包含`

```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] >= target:
            r = m - 1
        else:
            l = m + 1
    return l
```

Find target:
```python
def binary_search(arr, target):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2
        if arr[m] == target:
            return m  # 找到目標值，返回其索引
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1  # 如果沒有找到目標值，返回 -1
```


## Difference

- 迴圈條件：

`while l < r`：當左邊界小於右邊界時進行迴圈。這種寫法在迴圈結束時，l 和 r 會相等，並且指向第一個大於或等於目標值的位置。
`while l <= r`：當左邊界小於等於右邊界時進行迴圈。這種寫法在迴圈結束時，l 會指向第一個大於目標值的位置，而 r 會指向最後一個小於目標值的位置。

- 邊界更新：

`while l < r`：
當 `arr[m] >= target` 時，更新 `r = m`，因為我們要找的是第一個大於或等於目標值的位置。
當 `arr[m] < target` 時，更新 `l = m + 1`，因為我們要排除掉 m 位置。

`while l <= r`：
當 `arr[m] >= target` 時，更新 `r = m - 1`，因為我們要找的是第一個大於或等於目標值的位置。
當 `arr[m] < target` 時，更新 `l = m + 1`，因為我們要排除掉 m 位置。

- 初始右邊界：

`while l < r`：右邊界設置為 len(arr)，因為右邊界不包含在搜索範圍內。
`while l <= r`：右邊界設置為 len(arr) - 1，因為右邊界包含在搜索範圍內。


- 適用場景
`while l < r`：適用於需要找第一個大於或等於目標值的位置，或者需要確保搜索範圍不包含右邊界的情況。
`while l <= r`：適用於需要找目標值的具體位置，或者需要確保搜索範圍包含右邊界的情況。 （search target in a list）