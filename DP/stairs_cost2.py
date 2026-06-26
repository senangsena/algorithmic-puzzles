# 階段のコストの問題
# [10, 15, 20] -> start -> 1(15) -> end なので15
# [1, 100, 1, 1, 100, 1, 1, 100, 1] -> 6 (100は踏みたくないよね)

# 方針
# 飛べる中で、スコアが小さいほうに飛ぶ→たいていはうまくいくが、
# コストが単調増加だと、全ステップ踏むことになる。
# 2段進んだほうがたくさん進めるにきまってる。
# 大事なのは、2段ではなく、1段しか進まないことを選ぶ理由 
# -> 2段目 > 1 + 3段目の時！！つまり2段目をどうしても飛ばしたいとき

def stairs_cost(costs: list[int]) -> int: # 10, 15, 20

    #  現在地(startのindexは0の一個前なので-1にする)
    index = -1

    # 使ったコスト
    total_costs = 0

    # goalに飛ばすために、costsの後ろに0つける
    costs += [0, 0, 0]

    while index < len(costs) - 3:
        
        if costs[index + 2] > costs[index + 1] + costs[index + 3]:
            total_costs += costs[index + 1] + costs[index + 3]
            index += 3
        else:
            total_costs += costs[index + 2]
            index += 2

    return total_costs


print(stairs_cost([10, 15, 20]))
print(stairs_cost([1, 100, 1, 1, 100, 1, 1, 100, 1]))