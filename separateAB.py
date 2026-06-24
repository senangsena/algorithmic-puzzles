# AABBAB...のようにAとBが混ざった文字列を、AAA...AB...BBBのようにしたい
# Aー>BまたはBー>Aと変換できる時の最小変換回数
# はじめにAの数とBの数を数える。
# 左から見ていき、各境界線ごとに、それより左にあるBの数と右にあるAの数の和（変換回数）を考え最小値を更新
# T:O(N), S:O(1)

def separateAB(s: str) -> tuple[int, int]:

    right_a = 0
    for c in s:
        if c == "A":
            right_a += 1
    left_b = 0

    min_flips = right_a

    # どのindexの後に境界線を作るのか
    flip_after = -1 

    # s[i]の後に境界線がある時を考える
    for i in range(len(s)):

        # 境界線を移す作業

        if s[i] == "A":
            right_a -= 1
        elif s[i] == "B": 
            left_b += 1
        else:
            print(f"unknown type of char...{s[i]}")

        if min_flips > right_a + left_b:
            min_flips = right_a + left_b
            flip_after = i
        

    return min_flips, flip_after

if __name__ == "__main__":

    print("Input string with A/B: ", end = "")
    min_flips, flip_after = separateAB(input())
    print(f"minimum flip times for sort A/B ... {min_flips}")
    print(f"Separated between {flip_after} and {flip_after + 1}")




