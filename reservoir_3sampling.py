# 等確率保証アルゴリズム拡張版
# 選ぶデータの数が3つ

import random

def reservoir_3sampling():

    ans1 = "" 
    ans2 = ""
    ans3 = "" 

    count = 0

    while True:

        val = input()

        if val == "end":
            break

        count += 1

        if count == 1:
            ans1 = val
        elif count == 2:
            ans2 = val
        elif count == 3:
            ans3 = val
        else:
            # n = 4の時は、1/4の確率でans1更新　→ 1/4の確率で、ans2更新　→ ...
            # n = kの時は、1/kの確率でans1更新　→ 1/kの確率で、ans2更新　→ ...
            probability = random.randint(1, count)
            if probability == 1:
                ans1 = val
            elif probability == 2:
                ans2 = val
            elif probability == 3:
                ans3 = val
    
    return ans1, ans2, ans3, count

answer1, answer2, answer3, n = reservoir_3sampling()
if n > 0:
    print(f"\"{answer1}\", \"{answer2}\", \"{answer3}\" are selected by 3 / {n} probability.")
else:
    print("No Data.")