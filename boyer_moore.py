# 過半数判定アルゴリズム
# mappingを使用しない、空間計算量O(1)の実装

print("please \"end\" at the end of the list")

answer = ""
count = 0
while(input() != "end"):
    if count == 0:
        answer = input()
        count = 1
    elif answer == input():
        count += 1
    else:
        count -= 1

print(f"{answer} is appeared over 50%")