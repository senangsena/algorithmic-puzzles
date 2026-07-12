# 重複しない最長部分文字列
# 2ポインタで、left, rightを動かしていく

def longest_unisubarray(numbers: list[int]) -> int: # aa

    left = 0 # a
    right = 1 # a

    seen = set([numbers[0]]) # numbers[0]は読んだことにする

    if len(numbers) == 0:
        return 0
    elif len(numbers) == 1:
        return 1
    

    current = 0 # 今見ているindex
    max_length = 1

    while right < len(numbers): # 1 < 2

        if numbers[right] in seen: # 

            # leftを重複しない範囲まで動かす
            while True:
                if numbers[left] == numbers[right]:
                    left += 1
                    right += 1
                    break
                else:
                    seen.remove(numbers[left])
                    left += 1

            # この時点でnumbers[left]は重複した文字の一個次をさしている

        else:
            seen.add(numbers[right])
            # maxの更新
            if max_length < right - left + 1: # 0<3
                max_length = right - left + 1 # 3

            right += 1

    return max_length

assert longest_unisubarray("a") == 1
assert longest_unisubarray("aa") == 1
assert longest_unisubarray("abc") == 3
assert longest_unisubarray("abca") == 3
assert longest_unisubarray("abccba") == 3
assert longest_unisubarray("abcabcbb") == 3


        


    
    

