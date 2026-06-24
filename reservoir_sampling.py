# 等確率保証アルゴリズムの実装

import random

def reservoir_sampling() -> tuple[str, int]:

    ans = ""
    count = 0

    while True:

        val = input()

        if val == "end":
            break

        count += 1

        # 1/countの確率で更新
        probability = random.randint(1, count)
        if probability == 1:
            ans = val

    return ans, count


answer, n = reservoir_sampling()
if n > 0:
    print(f"\"{answer}\" is selected with 1 / {n} probability")
else:
    print("No Data.")


