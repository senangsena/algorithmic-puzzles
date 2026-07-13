# algorithms

その他

## 連続部分列の最大和 `largest_subarray.py`
*Find the contiguous subarray with the largest sum*  
流れてくる数字を読み、和が最大になる連続部分列を見つけるアルゴリズム  
`Ex：[-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6`

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯

全ての連続部分和を計算してもできるが時間計算量O(N^2), 空間計算量O(N)  

<br>

## 循環検出アルゴリズム (Cycle Detection Algorithm)
連結リストの中にループがあるかを探したい。  

普通に考えると...　今まで通ったノードを全て記憶し、そのうちどれかに戻ったらループ発見　→ 空間計算量**O(N)** 😕  
    　**これをO(1)でするには？**  

<br>

## カプレカ数のブラックホール `kaprekar.py`

* 4桁の数字がある（「1111」などのゾロ目以外）
* その数字の各桁を並べ替えてできる「最大の数（降順）」から「最小の数（昇順）」を引きます。
* 出てきた答えに対して、再び同じ操作を繰り返します。

どんな4桁の数字から始めても、何度か繰り返すと必ず**特定の数字**に辿り着きます。それはいくつ？


## 📈 連続部分配列の最大積 (Maximum Product Subarray) `find_maxproduct.py`
*Find the contiguous subarray with the largest product. Beware of negative numbers turning into giants!*  

* 自然数がランダムに混ざった整数の配列が与えられる（例: [2, 3, -2, 4, -1]）。
* この配列の中で、「連続する」部分配列の要素をすべて掛け合わせたとき、その積が最大になる値を返してください。  


Ex) [2, 3, -2, 4, -1] -> 48 (全てを掛け合わせると 48 になり、これが最大)  

* Time: O(N)
* Space: O(1)

## 3色ソート問題 `sort_colors.py`

0, 1, 2のみでできた配列をソートする

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 


## 最大の水量を蓄える容器 (Container With Most Water) `water.py`

* 水槽にたくさん壁が立っている
* この中から2つの壁を選んでその間に水を溜めた時、溜められる水の量の最大値は？

**[rule]**   
`water = index_differences × lowest_height(二つの壁のうち低いほう)`   

ex)  
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 

## 2つの整数和問題　(2sum)
整数のリストがあり、その中の任意の異なる2つの整数がある数になる。その二つの整数の組み合わせを全て見つけたい。  

全パターンを網羅するとO(N^2)...
これをO(N)にするには？(Time complexity)

<br>

## 次の順列 (Next Permutation) `rotate.py`
Rearrange numbers into the lexicographically next greater permutation in-place.
* ある配列の並び替えで、辞書順で次に大きい並びを返す
* 次に大きい一つだけ返す

[1, 2, 3] -> [1, 3 ,2] -> [2, 1, 3] -> [2, 3, 1] -> [3, 1, 2] -> [3, 2, 1] -> [1, 2, 3] ...  
なので  
ex) [1, 3, 2] -> [2, 1, 3]

* 時間計算量　O(N)
* 空間計算量　O(1)

## 未知の最小正整数 (First Missing Positive) `first_missing_positive.py`
*Find the smallest missing positive integer in an unsorted array.*

+ ランダムな整数（負の数や0、極端に大きい数も含まれる）が格納された配列が与えられる。  

+ この配列に 含まれていない「最も小さい正の整数（1, 2, 3...）」 を特定するアルゴリズム。  

Ex1: [3, 4, -1, 1] -> 2    
(※1は存在し、次に小さい正の整数2が欠落しているため)   
Ex2: [7, 8, 9, 11, 12] -> 1  (※1が含まれていないため)
* 時間計算量(Time)      O(N)

* 空間計算量(Space)    O(1) 🤯

## 最短部分列長問題

流れてくる数字を読み、target(定数)以上を和に持つ、最も長さの短い連続部分列の長さを特定するには？  
`Ex: [1, 2, 1, 1, 1, 3, 4, 2] -> 2 (len([3, 4]) = 2 だから)`
* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯 <- これでは不可能らしい by Gemini

<br>

## 重複しない最長部分文字列問題　`longest_unisubarray.py`

## 回転数字配列のtarget探索 `search_rotatelist.py`
* 昇順に並んだ数字配列を一回回転する  

* 回転とは？  
    [1, 2, 3, 4, 5, 6] -> [3, 4, 5, 6, 1, 2]

* target: intが与えられ、target in roteted_numbersならindexを、not なら-1を返す