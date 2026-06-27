# 3色ソート問題
# 普通に考えたらソートすればいい　→ bubble sort だとO(N^2)
# 3色しかないなら、0を見つけたら先頭に寄せる、2見つけたら後ろに寄せるってやりたい
# 同時にやると干渉するので別にする

def sort_colors(nums: list[int]) -> list[int]:

    next_zero_index = 0
    next_two_index = len(nums) - 1

    for i in range(len(nums)):

        if nums[i] == 0:
            nums[i], nums[next_zero_index] = nums[next_zero_index], nums[i]
            next_zero_index += 1

    for i in range(len(nums)):

        if nums[len(nums) - 1 - i] == 2:
            nums[len(nums) - 1 - i], nums[next_two_index] = nums[next_two_index], nums[len(nums) - 1 - i]
            next_two_index -= 1
    
    return nums
              

print(sort_colors([1,2,1,0,0,0,1]))
print(sort_colors([2,1,0]))
print(sort_colors([1,2,0,1,0,0,1]))
print(sort_colors([0]))