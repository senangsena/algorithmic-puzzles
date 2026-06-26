<h1 align="center">Logic Puzzles & Algorithms</h1>

前提知識の要らない、純粋なひらめきで解くアルゴリズム問題  
それをコードで実装してみたり...
```
algorithmic-creativity/
├── README.md       <- ⭐️
├── STREAM/         <- ストリーム系
│   ├── README.md
│   └── ...
├── algorithms/     <-　その他
│   ├── README.md
│   └── ...
│ 
└── 12coins/       
    └── ...
```


以下、個人的なお気に入り**Top 10**✨  (My favorites) 

<br>

## 12枚のコインの問題　(12 Coins Problem)  　 `./12coins`
*Find the 1 fake coin out of 12 using a scale just 3 times. Is it heavier or lighter?*

12枚のコインのうち一枚のみ重さが異なる。天秤を3回のみ使用して重さの異なるコインはどれか・他より重いのか軽いのかも特定するアルゴリズム

* 偽物のコインが他より重いのか軽いのかわかっていないところが面白い 単純に1/2ずつ絞っていくのではいけない

* 考えられる状況は、偽物コインの番号12通り ｘ 重い軽いの2通り = **24**通り < 天秤3回で表せる状況は 3^3 = **27**通り　なので理論的には解けるはず 

ただしこの条件で考えるには**ほぼ毎回の天秤で3分岐を有効に使う**必要がある -> どんな工夫ができるか

```
└── 12coins/
    ├── README.md
    ├── 12coins_explanation.md  <- 解説
    ├── play_12coins.py         <- 実際に遊んでみる
    └── solve12coins.py         <- プログラムに解かせる
```

<br>

## 過半数判定アルゴリズム (Majority Vote Algorithm) `boyer_moore.py`
*Find the majority element in O(1) space.*

数字（自然数）がN個、どんどん流れてくる。全ての数字が流れ終わった時点で、過半数登場した数字があることは保証されている。この時どの数字が過半数現れたかを、以下の計算量で特定する。
* 時間計算量(Time) 　　   O(N)
* 空間計算量(Space) 　  **O(1)** 🤯
  
つまり過去に登場した数字と登場回数のmappingは作れないということ!

<br>

## 等確率保証アルゴリズム (Reservoir Sampling🎲) `reservoir_sampling.py`
N個の異なるデータが流れてくる。Nがいくつかはデータを全て読み終わった後に初めてわかる。データは巨大なため、どこかに全て保存しておくことはできない。  

この時、これらのデータから **完全にランダムなデータ** を選ぶ(つまりNがいくつであっても、N個のデータのうち一つを1/Nの確率で選ぶ)にはどんなアルゴリズムを使用すればいい？?  

例：

``` 
nab;eotrfa
eorif
gavoeru
anbero
noevar
end
"noevar" is selected with 1 / 5 probability
```

<br>

## 等確率保証アルゴリズム拡張 (Reservoir Sampling🎲) `reservoir_3sampling.py`

等確率保証アルゴリズムの拡張。1つではなく3つのデータを等確率で選びたい時どうする？


## 株の最大利益 (Best Time to Buy and Sell Stock) `stock.py`
*Maximize profit by choosing a single day to buy and a single day to sell.*  

* ある銘柄の日々の価格（自然数）が、1日目から順に流れてくる。
* 「一度だけ株を買い、その後（未来）の日に一度だけ株を売る」ことができる。
* この時、得られる 最大の利益 を計算するアルゴリズム（利益が出ない場合は0とする）。  

`Ex: 7 -> 1 -> 5 -> 3 -> 6 -> 4 -> end  => 5 (価格1で買い、価格6で売るため)`
* 時間計算量(Time)      O(N)
* 空間計算量(Space)    O(1) 🤯  

過去の価格履歴を全てリストに保存しておくことはできない。

## AB文字列分断の最短変換問題　(Minimum Flips to Make a String Monotone)   `separateAB.py`
*Sort 2 types of items in-place.*

A,BがランダムにN個混ざった文字列の各文字を、A -> B または B -> Aに変換できるとき、AA...AB...BBのようにA,Bを分断させるのに必要な最短変換回数を
* 時間計算量(Time) 　　   O(N)
* 空間計算量(Space) 　  **O(1)** 🤯
で計算する

<br>

## 2つの卵と100階建てのビル (Egg Dropping Problem) `100eggs.md`
* 二つの卵と100階建てのビルがある。ある階から下の階では卵は割れず、ある階より上の階からは卵が割れる。  
* この境目が何階なのかを特定したい時、最悪試行回数をなるべく少なくしたい時どのような戦略を立てればいい？？

⭐︎ 最悪試行回数が最小になる時 ＝　どのような条件に対しても同一の最悪試行回数で特定できる時

<br>

## 連続部分列の最大和
*Find the contiguous subarray with the largest sum*  
流れてくる数字を読み、和が最大になる連続部分列を見つけるアルゴリズム  
`Ex：[-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6`

* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯

全ての連続部分和を計算してもできるが時間計算量O(N^2), 空間計算量O(N)  

<br>

## 最短部分列長問題

流れてくる数字を読み、target(定数)以上を和に持つ、最も長さの短い連続部分列の長さを特定するには？  
`Ex: [1, 2, 1, 1, 1, 3, 4, 2] -> 2 (len([3, 4]) = 2 だから)`
* 時間計算量(Time)      　O(N)
* 空間計算量(Space)     　**O(1)** 🤯 <- これでは不可能らしい by Gemini

<br>


## 循環検出アルゴリズム (Cycle Detection Algorithm)
連結リストの中にループがあるかを探したい。  

普通に考えると...　今まで通ったノードを全て記憶し、そのうちどれかに戻ったらループ発見　→ 空間計算量**O(N)** 😕  
    　**これをO(1)でするには？**  

<br>

階段の出力
PS C:\Users\dev-STR\Desktop\sena> python .\stairs_cost.py

15
6

