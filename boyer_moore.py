# 過半数判定アルゴリズム
# mappingを使用しない、空間計算量O(1)の実装

print("please \"end\" at the end of the list")

answer = ""
count = 0

while True:

    val = input()
    
    if val == "end":
        break
    
    if count == 0:
        answer = val
        count = 1
    elif answer == val:
        count += 1
    else:
        count -= 1

print(f"{answer} is appeared over 50%")