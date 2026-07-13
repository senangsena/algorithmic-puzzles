# 回転数字配列のtarget探索
# 2分探索するが、初めにnumbers[0]を基準にする

def search_rotetelist(numbers: list[int], target: int) -> int:

    if not numbers or (target == None):
        return -1

    if numbers[0] <= target: # targetは境目よりも前にある
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[(left + right) // 2] == target:
                return (left + right) // 2
            elif numbers[(left + right) // 2] > target: # 必ず境目より前にいる

                right = (left + right) // 2 - 1
            else: # numbers[(left + right) // 2] < target　の時は、境目より前なのか後ろなのかで場合分け

                if numbers[(left + right) // 2] < numbers[0]: # 境目より後ろ -> rightを動かし視点を左に(前に)

                    right = (left + right) // 2 - 1
                else: # 境目より前 -> 見るところあっている
                    left = (left + right) // 2 + 1
        
        return -1

    else: # targetは境目よりも後ろにある
        left = 0
        right = len(numbers) - 1

        while left <= right:
            if numbers[(left + right) // 2] == target:
                return (left + right) // 2
            elif numbers[(left + right) // 2] < target: # 必ず境目より後ろにいる

                left = (left + right) // 2 + 1
            else: # numbers[(left + right) // 2] > target　の時は、境目より前なのか後ろなのかで場合分け

                if numbers[(left + right) // 2] >= numbers[0]: # 境目より前 -> leftを動かし視点を右に(後ろに)

                    left = (left + right) // 2 + 1
                else: # 境目より後ろ -> 見るところあっている
                    right = (left + right) // 2 - 1
        
        return -1
    
if __name__ == "__main__":

    assert search_rotetelist([], 1) == -1
    assert search_rotetelist([1,2,3], None) == -1

    assert search_rotetelist([1,2,3], 1) == 0
    assert search_rotetelist([1,2,3], 2) == 1
    assert search_rotetelist([1,2,3], 3) == 2
    assert search_rotetelist([1,2,3], 4) == -1

    assert search_rotetelist([4,5,1,2,3], 1) == 2
    assert search_rotetelist([4,5,1,2,3], 2) == 3
    assert search_rotetelist([4,5,1,2,3], 3) == 4
    assert search_rotetelist([4,5,1,2,3], 4) == 0
    assert search_rotetelist([4,5,1,2,3], 5) == 1

    assert search_rotetelist([10,45,46,0,1,4,6], 45) == 1
    assert search_rotetelist([79,1,2,3,4], 4) == 4

    print("OK!")

    




