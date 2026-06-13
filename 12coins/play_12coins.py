# 実際に謎解きができるプログラム
import random

class play12coins:

    def __init__(self):

        # 各コイン番号(id) -> 重さ のmapping
        self.weights = {}
        for i in range(12):
            self.weights[i + 1] = 10
        
        # ランダムに一つのコインの重さを変える
        self.oddcoinID = random.randint(1,12)
        self.weights[self.oddcoinID] = random.choice([9, 11])

        # 答えをまとめて記録しておく
        weight_to_ans = {9: "軽い", 11: "重い"}
        self.answers = [self.oddcoinID, weight_to_ans[self.weights[self.oddcoinID]]]

        # 天秤実行回数
        self.eval_count = 0

    # 天秤で重さを測る。
    # left  : 左の皿に乗せたいコイン番号リスト
    # right : 右の皿に乗せたいコイン番号リスト
    # 返り値は"つり合う" or "左が重い" or "右が重い"
    def tenbin(self, left: list[int], right: list[int]) -> str:

        left_weights = 0
        right_weights = 0

        for id in left:
            left_weights += self.weights[id]
        
        for id in right:
            right_weights += self.weights[id]

        if left_weights == right_weights:
            return "つりあう"
        elif left_weights < right_weights:
            return "右が重い"
        else:
            return "左が重い"

    # 与えられたリストが、1~12以外の数字が入ってないか確かめる  
    # 同一の数字が複数回使われていないか確かめる
    def isValidCoinID(self, coins_list : list[int]) -> bool:

        for id in coins_list:
            if id not in self.weights:
                return False
        
        # ソートした時連続した数字があるかどうかの判定で、同一の感じが複数回使われていないかの判定になる
        # こうするとmappingを使用せずにO(1)空間計算量で済む
        coins_list.sort()
        for i in range(len(coins_list) - 1):
            if coins_list[i] == coins_list[i + 1]:
                return False
            
        
        return True


    # 一回の天秤実行
    def evaluate(self):
        
        self.eval_count += 1
        print(f"{self.eval_count}回目の天秤⚖️")

        while True:
            # 入力読み込み
            try:
                print("左の皿 : ", end="")
                left = list(map(int, input().split()))
                
                print("右の皿 : ", end="")
                right = list(map(int, input().split()))
                print()
            except:
                clear_lines(2)
                print("⚠️入力できるのは半角の数字のみ！")
                continue

            # left, rightを結合して判定することで一回の関数呼び出しですむ
            # 両方に同じ番号のコインが乗ることを簡単に防げる
            if self.isValidCoinID(left + right):

                # 天秤にかけ結果をprint
                print(f"左:{left}と右:{right}を天秤にかけた結果は...{self.tenbin(left, right)}")
                print()
                break
            else:
                clear_lines(3)
                print("⚠️コインは1~12までの整数で、スペースを開けて入力してください。同じ番号のコインは複数枚ありません")

        
        return


    # 答えが正しいか確認する関数。
    def answer_check(self, ID : int, weight : str) -> bool:
        if self.answers == [ID, weight]:
            return True
        else:
            return False

# 直前のn行を消す関数
def clear_lines(n):
    for i in range(n):
        # 1行上に戻る + その行を消去する
        print('\033[F\033[K', end='')

if __name__ == "__main__":

    play = play12coins()
    

    print("12枚のコイン【1】〜【12】の中には、一枚だけ他のコインと重さが異なるコインが紛れています。")
    print("天秤を3回まで使って何番のコインが\"重い\"のか\"軽い\"のか当ててみよう:)")
    print()
    print("天秤の使いかた       例）[1, 4, 5] と [2, 7, 8]を比べたいとき")
    print("左の皿 : 1 4 5")
    print("右の皿 : 2 7 8")
    print()

    # 3回天秤評価の実行
    while play.eval_count < 3:
        play.evaluate()
    
    # 答えの読み込み. answer_IDとanswer_weightに答えを正規化して保存

    while True:
        id_error = False
        weight_error = False

        try:
            print("答えはなんでしょう？ 番号と{重い or 軽い}をスペースを開けて入力してください    例）1 重い")
            ans_id, ans_weight = input().split()
            print()
            ans_id = int(ans_id)
        except:
            clear_lines(3)
            print("⚠️不正な形式の入力です！     入力例）1 重い")
            continue

        # 入力の形が正しいか判定。正しければbreakし、answer_check()で答えを確認する
        if not play.isValidCoinID([ans_id]):
            print("コインの番号が不正。1〜12の中の整数で答えてください")
            id_error = True
        if ans_weight not in ["重い", "軽い"]:
            print("重さの入力が不正。\"重い\"または\"軽い\"で答えてください")
            weight_error = True

        if not (id_error or weight_error):
            break
    
    if play.answer_check(ans_id, ans_weight):
        print("正解😃!!")
    else:
        print(f"残念😔..答えは 『{play.answers[0]}番のコインが{play.answers[1]}』でした！")
    print("詳しい解き方はsolve12coins.pyで確認できます:)")
