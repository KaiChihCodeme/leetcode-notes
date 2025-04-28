# 102
每次太久沒寫會忘記level-order的標準寫法
但她的概念我會記得，不過要自己implement出來往往需要很多時間，並且解法也不是最佳解
因此他的標準寫法還是得要熟練到可以背起來

不過概念上就是:
- 用ans去存整個結果，使用queue去存下個level要iterate的elements
- 會用一個while迴圈去確認queue是否還有東西，有的話就會繼續，否則結束回傳ans
- 如果有東西，去initialize a res list, 去存現在這個level的element (因為正在iterate this level, 所以也趁機存現在的elements)
- iterate的方式是用for loop, 大小則是目前queue的大小。因為在此時，queue的大小剛好等於這個level的大小。等一下跑loop時，我們會把下個level的elements一樣存進這個queue, 所以我們要使用for loop來確保我們只看這個level, 並存入下個level到queue (這一點是我最常卡住的點，我會不知道要怎麼存這層跟下層的關係)
- 在for loop跑完代表這個level結束。將res存入大的ans裡