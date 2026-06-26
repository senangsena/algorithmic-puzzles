# 最長単調増加部分列の問題

# O(N^2)の計算量の解き方
def increasing_sub(nums: list[int]) -> int: # [1, 10, 2, 9, 3, 8, 4]

    assert len(nums) > 0

    # i番目にはnums[i]までの最長単調増加部分列の長さが入る
    longest_lengths = [1] + [0] * (len(nums) - 1) # [1, 0, 0...]

    for i in range (1, len(nums)):

        for j in range(0, i):
            if nums[j] < nums[i] and (longest_lengths[i] < longest_lengths[j] + 1):
                longest_lengths[i] = longest_lengths[j] + 1

    return max(longest_lengths)

# O(NlogN)の解き方

print(increasing_sub([0, 1, 2, 3])) # 4
print(increasing_sub([3,2,1])) # 1
print(increasing_sub([1, 10, 2, 9, 3, 8, 4])) # 4


