# 235
thought: 
原本以為是一般的tree, 而且還以爲只需要回傳value (int) 就好，所以方向是錯的。
後來看solution才發現他是BST, 那就沒有那麼麻煩了，要找他們的LCA, 就只要min(p,q) < root < max(p,q)就可以解決
這題我覺得只要熟練BST的觀念就可以想到
但重點是題目要理解清楚