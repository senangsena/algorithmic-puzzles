# 12coins問題の解き方がわかるプログラム
# 自分で設定した設定に合わせて、プログラムが問題を解きます
# 解く過程・思考の方法も出力

class Solve12coins:

    def __init__(self, default_weight: int, oddcoins_weight: int, oddcoins_id: int):
        
        # ID -> weight のmapping
        self.weights = {}
        for id in range(1, 13):
            if id == oddcoins_id:
                self.weights[id] = oddcoins_weight
            else:
                self.weights[id] = default_weight
        
        self.normal_coin = 1 if oddcoins_id != 1 else 2 # 確実に正常なコインの番号を保持しておく用

    # 天秤
    def tenbin(self, left: list[int], right: list[int]) -> str:
        left_weights = sum(self.weights[id] for id in left)
        right_weights = sum(self.weights[id] for id in right)

        if left_weights == right_weights:
            return "つりあう"
        elif left_weights < right_weights:
            return "右が重い"
        else:
            return "左が重い"

    def solve(self):
        print("🔍 12枚のコイン問題 推理開始!")

        # 1回目の天秤使用
        print("【1回目の天秤】")
        print("まずは [1, 2, 3, 4] と [5, 6, 7, 8] を比較")
        fst_result = self.tenbin([1, 2, 3, 4], [5, 6, 7, 8])
        print(f"⚖️ 結果 ... {fst_result}\n")

        # 1回目の結果からの分岐
        if fst_result == "つりあう":
            print("💡 考察: つりあったということは、[1〜8]は全て通常のコインであるとわかる")
            print("ということは ...?    残りの [9, 10, 11, 12] の中に偽物がある！")
            self._solve_balanced()
        
        elif fst_result == "左が重い":
            print("💡 考察: [1,2,3,4]のどれかが重い、もしくは[5,6,7,8]のどれかが軽いと絞り込める")
            print("ということは ...?    残りの [9, 10, 11, 12] は通常のコインだと確定する！😃（これを上手く使いたい）")
            # H(重い可能性があるグループ), L(軽い可能性があるグループ)
            self._solve_unbalanced(H=[1, 2, 3, 4], L=[5, 6, 7, 8])
            
        else: # 右が重い
            print("💡 考察: [5,6,7,8]のどれかが重い、もしくは[1,2,3,4]のどれかが軽いと絞り込める")
            print("ということは ...?    残りの [9, 10, 11, 12] は通常のコインだと確定する！😃（これを上手く使いたい）")
            self._solve_unbalanced(H=[5, 6, 7, 8], L=[1, 2, 3, 4])


 # 分岐A：1回目が「つりあった」場合のロジック
    # ==========================================
    def _solve_balanced(self):
        print("\n【2回目の天秤】")
        print("単純に2:2で量っても絞り込まれない")
        print("ということは ...?    すでに正しい重さを持つとわかったコイン(1番)を使用する！")
        print("疑わしい4枚のうち1枚(12)を取り除き、残りの3枚のうち1枚(9)と通常(1)をセットにして、残り2枚(10, 11)と比べる")
        print("左の皿: [9, 1(通常)]  vs  右の皿: [10, 11]")
        
        snd_result = self.tenbin([9, 1], [10, 11])
        print(f"⚖️ 結果 ... {snd_result}\n")

        if snd_result == "つりあう":
            print("💡 考察: つりあったということは、[9, 10, 11]も通常のコインであるとわかる")
            print("ということは ...?    最初に取り除いた【12番】が偽物で確定する！😃")
            print("\n【3回目の天秤】")
            print("12番が重いか軽いかを知るために、通常の1番と比べる")
            trd_result = self.tenbin([12], [1])
            print(f"⚖️ 結果 ... {trd_result}\n")
            weight_str = "重い" if trd_result == "左が重い" else "軽い"
            self._announce_answer(12, weight_str)

        else:
            print("💡 考察: つりあわなかったということは、[9, 10, 11]の中に偽物がある")
            print("\n【3回目の天秤】")
            print("右の皿に乗せた“残り2つ” [10] と [11] を比べる")
            trd_result = self.tenbin([10], [11])
            print(f"⚖️ 結果 ... {trd_result}\n")

            if trd_result == "つりあう":
                print("💡 考察: [10]と[11]がつりあった")
                print("ということは ...?    偽物は残った【9番】であるとわかる！")
                weight_str = "重い" if snd_result == "左が重い" else "軽い"
                self._announce_answer(9, weight_str)
            else:
                print("💡 考察: [10]と[11]が傾いたなら、このどちらかが偽物である")
                print("ということは ...?    2回目の天秤で、右の皿[10, 11]側がどう傾いていたかで判断できる！")
                if snd_result == "右が重い":
                    ans = 10 if trd_result == "左が重い" else 11
                    self._announce_answer(ans, "重い")
                else: # 2回目で右が軽かった
                    ans = 10 if trd_result == "右が重い" else 11
                    self._announce_answer(ans, "軽い")


    # ==========================================
    # 分岐B：1回目が「傾いた」場合のロジック
    # ==========================================
    def _solve_unbalanced(self, H: list[int], L: list[int]):
        normal = 9 # 1回目で量っていない9番は確実に正常
        
        h_kept, h_replaced, h_swapped, h_removed = H[0], H[1], H[2], H[3]
        l_kept1, l_kept2, l_swapped, l_removed = L[0], L[1], L[2], L[3]

        print("\n【2回目の天秤】")
        print("ここから、あと2回で答えを出すには ...?")
        print("天秤が表す出力は3通り。この3通りが全て別々の状況を指すように、以下のような工夫をする\n")
        print(f"1. 1個ずつ取り除く -> 重い候補から{h_removed}、軽い候補から{l_removed}を除外する")
        print(f"2. 1個ずつ左右を交換する -> 重い候補{h_swapped} と 軽い候補{l_swapped} を入れ替える　→ こうすることで、「傾きが変わる」という新しい分岐を作れる！！")
        print(f"3. 重い候補からもう1つ{h_replaced}を取り、通常のコイン({normal})と入れ替える　→ こうすることで、8つのコインが4/2/2と偏って分かれていたものを3/3/2にすることができる！\n")
        print("🌟こうすることで、8枚のコインを、[取り除いた3つ / 交換した2つ / 場所を変えていない3つ] の3グループに偏りなくいい感じに分けられる！🌟")
        print(f"\n左の皿: [{h_kept}, {l_swapped}, {normal}]")
        print(f"右の皿: [{l_kept1}, {l_kept2}, {h_swapped}]")
        
        snd_result = self.tenbin([h_kept, l_swapped, normal], [l_kept1, l_kept2, h_swapped])
        print(f"⚖️ 結果 ... {snd_result}\n")

        if snd_result == "つりあう":
            print("💡 考察: つりあったということは、皿に乗っているものは全て通常のコインであるとわかる")
            print(f"ということは ...?    偽物は、皿から除外した [{h_removed}, {l_removed}] か、通常と入れ替えた [{h_replaced}] のどれか！😃")
            print("\n【3回目の天秤】")
            print(f"通常と交換した {h_replaced}(重保) と、除外したうち重い方の {h_removed}(重保) を比べる")
            
            trd_result = self.tenbin([h_replaced], [h_removed])
            print(f"⚖️ 結果 ... {trd_result}\n")
            
            if trd_result == "つりあう":
                print(f"💡 考察: ここでつりあった")
                print(f"ということは ...?    残る候補の {l_removed} が偽物である！")
                self._announce_answer(l_removed, "軽い")
            elif trd_result == "左が重い":
                self._announce_answer(h_replaced, "重い")
            else:
                self._announce_answer(h_removed, "重い")

        elif snd_result == "右が重い":
            print("💡 考察: 1回目から「傾きが変わった（重いグループ側が軽くなった）」とわかる")
            print(f"ということは ...?    原因は左右を交換した [{h_swapped}] か [{l_swapped}] のどちらか！😃")
            print("\n【3回目の天秤】")
            print(f"そのうちの1つ {h_swapped} と、通常のコイン {normal} を比べる")
            
            trd_result = self.tenbin([h_swapped], [normal])
            print(f"⚖️ 結果 ... {trd_result}\n")
            
            if trd_result == "つりあう":
                print(f"💡 考察: つりあった")
                print(f"ということは ...?    もう片方の {l_swapped} が偽物である！")
                self._announce_answer(l_swapped, "軽い")
            else:
                self._announce_answer(h_swapped, "重い")

        else: # snd_result == "左が重い"
            print("💡 考察: 1回目から「傾きが同じ（重いグループ側が重いまま）」とわかる")
            print(f"ということは ...?    位置を動かさなかった [{h_kept}], [{l_kept1}], [{l_kept2}] のどれかが偽物！😃")
            print("\n【3回目の天秤】")
            print(f"同じ「軽い候補」グループの {l_kept1} と {l_kept2} を比べる")
            
            trd_result = self.tenbin([l_kept1], [l_kept2])
            print(f"⚖️ 結果 ... {trd_result}\n")
            
            if trd_result == "つりあう":
                print(f"💡 考察: 軽い候補がつりあった")
                print(f"ということは ...?    残った重い候補の {h_kept} が偽物である！")
                self._announce_answer(h_kept, "重い")
            elif trd_result == "右が重い":
                print("💡 考察: 左の皿が軽いということは、左の皿に乗せた方が偽物である")
                self._announce_answer(l_kept1, "軽い")
            else:
                print("💡 考察: 右の皿が軽いということは、右の皿に乗せた方が偽物である")
                self._announce_answer(l_kept2, "軽い")

    def _announce_answer(self, id: int, weight: str):
        print("=======================================================")
        print(f"答え: 偽物は【 {id}番 】のコインで、他より【 {weight} 】！")
        print("=======================================================\n")
        print(
            "この問題を解くかぎ🔑：いかに各状況で天秤が表す3分岐を有効に使えるか?\n"
            "この考え方が効く工夫👀✨\n①左右の皿から一つ入れ替えるという発想。こうすることで「傾きが変わる」という新たな状況(分岐）を作ることができる！\n" \
            "②このままでは3つの分岐をどう考えても成立できない時に　→ 正解とわかっているコインを一つ加えあえて個数を増やすと、3分岐を表現できる！\n" \
            )

# 実行部分（自由に設定を変更して試せます）
if __name__ == "__main__":
    
    print("【問題設定】半角数字で入力してね:)")
    
    while True:
        try:
            print("通常の重さ: ", end="")
            default_weight = int(input())
            
            print("偽物の重さ: ", end="")
            oddcoins_weight = int(input())
            
            # 重さが同じだとパズルが成立しないので確認
            if default_weight == oddcoins_weight:
                print("⚠️ 通常の重さと偽物の重さは、異なる数字にしてください！\n")
                continue
            
            print("偽物の番号(1〜12): ", end="")
            oddcoins_id = int(input())
            
            # コインの番号は1〜12のみ
            if not (1 <= oddcoins_id <= 12):
                print("⚠️ 偽物の番号は 1 〜 12 の範囲で指定してください！\n")
                continue
            
            # 全てのエラーチェックをパスしたらループを抜ける
            break
            
        except ValueError:
            # 入力エラー（文字や小数など）のキャッチ
            print("⚠️ 不正な入力です！半角の整数を入力してください。\n")

    print(f"\n設定: (通常:{default_weight}g / 偽物:{oddcoins_weight}g / 番号:{oddcoins_id}番)")
    print("それでは、プログラムに解かせてみましょう...\n")

    problem = Solve12coins(default_weight, oddcoins_weight, oddcoins_id)

    # プログラムに解かせる
    problem.solve()