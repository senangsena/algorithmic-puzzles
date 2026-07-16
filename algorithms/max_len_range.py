"""
[10,1,2,4,7,2] , 4 -> 4(2,4,7,2)

方針1 max, minを覚えておく
"""

def cal_min(l: list[int], start:int, end:int) -> int: # start~end で最も小さいのを返す O(N)

    min_val = l[start]
    index = start
    ans = 0

    while index < end + 1:
        if min_val > l[index]:
            min_val = l[index]
            ans = index

        index += 1

    return ans

def cal_max(l: list[int], start:int, end:int) -> int: # start~end で最も大きいのを返す O(N)

    max_val = l[start]
    index = start

    ans = 0

    while index < end + 1:
        if max_val < l[index]:
            max_val = l[index]
            ans = index

        index += 1

    return ans

def max_len_range(numbers: list[int], limit: int)-> int: # [10,1,2,3,2,1], 4

    start = 0  # 10
    end = 0 # 1

    max_len = 0

    current_max_index = 0 
    current_min_index = 0
    
    while end < len(numbers): # 0 < 6

 
        if numbers[current_max_index] - numbers[current_min_index] > limit: # 0 > 4

            if numbers[end] > current_max_index: # 上振れでlimit超過　→ minを動かす
                start = min(current_min_index + 1, len(numbers) - 1)
                current_min_index = cal_min(numbers, start, end)
                
            else: # 下振れでlimit超過　→ maxを動かす
                start = min(current_max_index + 1, len(numbers) - 1)
                current_max_index = cal_max(numbers, start, end)

        else:
            if max_len < end - start: # 0 < 1
                max_len = end - start  
            
        if end < len(numbers) and numbers[end] < numbers[current_min_index]:
            current_min_index = end
        if end < len(numbers) and numbers[end] > numbers[current_max_index]:
            current_max_index = end

        end += 1     
    
        
    return max_len + 1

print(max_len_range([10,1,2,3,2,1], 2))

# new * googler = noogler
