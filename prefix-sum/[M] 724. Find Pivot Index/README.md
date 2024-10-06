# 724. Find Pivot Index

prefix-sum reference: [HERE](https://medium.com/%E6%8A%80%E8%A1%93%E7%AD%86%E8%A8%98/%E6%BC%94%E7%AE%97%E6%B3%95%E7%AD%86%E8%A8%98%E7%B3%BB%E5%88%97-prefix-sum-ed325ffb2906)

Prefix sum 又可以稱為 cumulative sum 或是 inclusive scan，核心的概念其實蠻直覺簡單，就是將陣列中每個元素的位置上，儲存該位置之前所有元素、或是特定條件下的總和。這樣一來，當我們需要計算任意區間的總和時，只需透過減法操作即可快速得到結果。

舉例來說，假設我們有一個陣列 arr = [2, 4, 6, 8, 10]，我們可以建立一個對應的前綴和陣列 prefixSum，其每個位置上的值為 arr 中對應位置之前所有元素的總和。

```py
arr = [2, 4, 6, 8, 10]

# prefix_sum[i] 表示 arr[0] 到 arr[i] 的總和
prefix_sum = [2, 6, 12, 20, 30]

# get sum from 0 to 3
res = prefix_sum[3] - prefix_sum[0]
```