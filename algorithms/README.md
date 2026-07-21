# algorithms

その他


## 都市のワープ (Teleporter) `teleporter.py`
*Follow the teleporters exactly K times, where K can be astronomically large.*

* N個の町があり、町 i にはワープ装置があって必ず町 A_i へ飛ぶ。
* 町1からスタートし、ワープをちょうど K 回繰り返したとき、最後にいる町はどこ？
* ただし K は最大で 10^18 回。

Ex) N = 4, K = 5, A = (3, 2, 4, 1) -> 町4 （1→3→4→1→3→4）

* 素朴に K 回シミュレーションすると **O(K)** で全く終わらない。
* 目標: **O(N)** 

---

## 移動する子どもたち (Gathering Children) `gathering.py`
*Find where every child stands after a huge number of L/R moves.*

* `L` と `R` だけからなる文字列が与えられ、各マスに子どもが1人ずつ立っている。
* 1回の操作で、`R` のマスの子は右へ1つ、`L` のマスの子は左へ1つ動く。
* k回移動した後に各マスにいる子どもの人数を求める。

Ex) "RRLRL", k = 2 -> [0, 1, 2, 1, 1] ([1,1,1,1,1] -> [0,2,1,1,1] -> [0,1,2,1,1])

* 目標: **O(N)**  (kの大きさによらない計算量で求めたい)

---

## 反転を伴う文字列操作 (String Formation) `string_formation.py`
*Process a string through append-to-either-end and whole-string-reverse queries.*


* 文字列 S に対し、Q個のクエリを順に処理する。クエリは2種類:
    * 文字列全体を **反転** する
    * 文字列の **先頭または末尾** に1文字追加する
* すべて処理した後の最終的な文字列を出力する（Q は最大 2×10^5）。

Ex) S = "a"、[先頭に "p" → 反転 → 末尾に "c" → 反転] => "cpa"

* 反転のたびに実際に文字列をひっくり返すと1回で **O(|S|)**、最悪 **O(Q・|S|)** で間に合わない。
* 目標: **O(|S| + Q)**

---

## 連続部分列の最大和 `largest_subarray.py`
*Find the contiguous subarray with the largest sum*  
流れてくる数字を読み、和が最大になる連続部分列を見つけるアルゴリズム  
`Ex：[-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6`

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯

全ての連続部分和を計算してもできるが時間計算量O(N^2), 空間計算量O(N)  

<br>

## 循環検出アルゴリズム (Cycle Detection Algorithm)
*Detect whether a linked list contains a loop using O(1) memory.*  
連結リストの中にループがあるかを探したい。  

普通に考えると...　今まで通ったノードを全て記憶し、そのうちどれかに戻ったらループ発見　→ 空間計算量**O(N)** 😕  
    　**これをO(1)でするには？**  

<br>

## カプレカ数のブラックホール `kaprekar.py`
*Repeat "largest minus smallest digit rearrangement" and watch every 4-digit number fall into one black hole.*

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
*Sort an array containing only 0s, 1s, and 2s.*

0, 1, 2のみでできた配列をソートする

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 


## 最大の水量を蓄える容器 (Container With Most Water) `water.py`
*Pick the two walls that trap the most water between them.*

* 水槽にたくさん壁が立っている
* この中から2つの壁を選んでその間に水を溜めた時、溜められる水の量の最大値は？

**[rule]**   
`water = index_differences × lowest_height(二つの壁のうち低いほう)`   

ex)  
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49 

## 2つの整数和問題　(2sum)
*Find every pair of numbers that adds up to a given target.*
整数のリストがあり、その中の任意の異なる2つの整数がある数になる。その二つの整数の組み合わせを全て見つけたい。  

全パターンを網羅するとO(N^2)...
これをO(N)にするには？(Time complexity)

<br>

## 次の順列 (Next Permutation) `rotate.py`
*Rearrange numbers into the lexicographically next greater permutation in-place.*
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
*Find the shortest contiguous run whose sum is at least the target.*

流れてくる数字を読み、target(定数)以上を和に持つ、最も長さの短い連続部分列の長さを特定するには？  
`Ex: [1, 2, 1, 1, 1, 3, 4, 2] -> 2 (len([3, 4]) = 2 だから)`
* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯 <- これでは不可能らしい by Gemini

<br>

## 重複しない最長部分文字列問題　`longest_unisubarray.py`
*Find the length of the longest substring without repeating characters.*

## 回転数字配列のtarget探索 `search_rotatelist.py`
*Search for a target in a sorted array that has been rotated once.*
* 昇順に並んだ数字配列を一回回転する  

* 回転とは？  
    [1, 2, 3, 4, 5, 6] -> [3, 4, 5, 6, 1, 2]

* target: intが与えられ、target in roteted_numbersならindexを、not なら-1を返す

<br>
## ヒストグラムの最大長方形 (Largest Rectangle in Histogram) `histogram.py`
*Find the largest rectangle that fits entirely under the skyline of bars.*

* 幅1の棒が隙間なく並び、それぞれの高さが配列で与えられる。
* これらの棒の中に収まる **面積が最大の長方形** の面積を求める（長方形は複数の棒にまたがってよいが、必ず棒の高さ以下）。

Ex) heights = [2, 1, 5, 6, 2, 3] -> 10 （高さ5と6の2本で 5×2 = 10）

* 時間計算量(Time)      　O(N) （全ペアの組を試すと O(N^2)）

<br>

## 最長連続整数列 (Longest Consecutive Sequence) `longest_consecutive.py`
*How long is the longest run of consecutive integers hidden in the array?*

* 順不同の整数配列が与えられる。値が連続する（例: 4,5,6,7）ように **並びを無視して** 拾えるとき、その最長の長さを求める。

Ex) [100, 4, 200, 1, 3, 2] -> 4 （1, 2, 3, 4 が連続するため）

* 時間計算量(Time)      　**O(N)** 🤯 （ソートすると O(N log N) になってしまう）

<br>

## ソート未完成の最短区間 (Shortest Unsorted Subarray) `shortest_unsorted.py`
*Find the shortest slice you could sort to make the whole array sorted.*

* 整数配列が与えられる。**ある連続した1区間だけ** を昇順に並べ替えれば、配列全体が昇順になる。
* その区間の **最短の長さ** を求める（すでに全体が昇順なら 0）。

Ex) [2, 6, 4, 8, 10, 9, 15] -> 5 （[6, 4, 8, 10, 9] を並べ替えれば全体が昇順）

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　O(1)

---

