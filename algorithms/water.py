# 水槽の問題

# 方針
# 両端から見ていき、低い法の壁を内側に移動させていく。
# （変わって改善する可能性あるのは低い方だけだから）
# （高いほうを変えてもっと高くなっても低い方が変わらないと意味ないよね）

# 計算量
# 全通り試すと、n-1 + n-2 + ... 2 + 1 = O(n^2)
# この方法なら O(n)!!

def water(heights: list[int]) -> int:

    # 左右の壁のindex
    left = 0
    right = len(heights) - 1

    max_water_amount = 0

    while left != right:

        water_amount = (right - left) * min(heights[right], heights[left])

        if max_water_amount < water_amount:
            max_water_amount = water_amount
        
        if heights[right] > heights[left]:
            left += 1
        else:
            right -= 1

    return max_water_amount

print(water([1, 8, 6, 2, 5, 4, 8, 3, 7]))