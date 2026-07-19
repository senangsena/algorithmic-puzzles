# 表と裏が、均等に出ないコインを使い、正確に50%を測ろう！
# 偏りがあるならそれも含めてシステムに組み込めばいい話
# Work with what you've got / Work with the bias ^ ^*


import random

# コインを投げる作業、表ならTrue, 裏ならFalseを返す
def coin() -> bool:
    n = random.randint(1,5) # 1~5の整数乱数を生成
    return n < 3 # 40%の確率(n = 1,2)で表(True)、60％の確率(n = 3,4,5)で裏(False)
    
# AとBが戦うとする.
# 勝った方を返す
def fight_winner() -> str:

    while True:
        tos1 = coin()
        tos2 = coin()

        if tos1 and not tos2:
            return "A"
        elif not tos1 and tos2:
            return "B"

if __name__ == "__main__":

    # test
    count = {"A":0, "B":0}
    for i in range(10000):
        val = fight_winner()
        count[val] += 1

    print("10000回中")
    print(f"A の勝ち：{count['A']} 回！")
    print(f"B の勝ち：{count['B']} 回！")

