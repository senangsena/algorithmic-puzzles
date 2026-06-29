# 欠けている数のうち最も小さい、正の整数を返す

# [2, 4, -1. 0] -> 1
# [] -> 1
# [-1, -2, -3] -> 1
# None -> None 


def sort_s(nums: list[int]) -> int:

    nums.sort() # ここで時間計算量O(NlogN)

    positive_num = 1
    find_positive = False

    for i in range(len(nums)):
        if nums[i] < positive_num:
            continue

        elif nums[i] == positive_num:
            positive_num += 1
            find_positive = True
        else:
            return positive_num
        
    if find_positive:
        return positive_num
    else:
        return 1

def cyclic_sort(nums:list[int]) -> int: # [-1, 3, 2, 0, -3] -> [0, -1, 2, 3, -3] -> 

    index = 0

    while index < len(nums):

        if nums[index] != index and (0 <= nums[index]) and (nums[index] < len(nums)):
            if nums[nums[index]] != nums[index]:
                # 本来のあるべき位置と交換
                # nums[1] = 3, nums[3]= nums[3], nums[1] 3と0を交換　→ 0と-1を交換
                temp1 = nums[index]
                temp2 = nums[nums[index]]
                nums[nums[index]] = temp1
                nums[index] = temp2

                # 以下のようにするとうまくいかなかった。単純な交換ではなく、交換先がnums[index]によるため
                # nums[index], nums[nums[index]] = nums[nums[index]], nums[index]
                
            else: 
                index += 1 

        else: 
            index += 1

    for i in range(1, len(nums)):
        if nums[i] != i:
            return i
        
    # 最後までnums[i] == iが成立　→ 1, 2, ..., len(nums) - 1まである
    # nums[0] == len(nums)かもしれない

    if nums[0] == len(nums):
        return len(nums) + 1
    else:
        return len(nums)


print(sort_s([-1, 2, 4, 3, 0])) # 1
print(cyclic_sort([-1, 2, 4, 3, 0]))
print()
print(sort_s([1,2,3,4,5])) # 6
print(cyclic_sort([1,2,3,4,5]))
print()
print(sort_s([-3,1,2,3,4,])) # 5
print(cyclic_sort([-3,1,2,3,4])) 
print()