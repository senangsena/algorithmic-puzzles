# 階段のコストの問題 (DP)
# [10, 15, 20] -> start -> 1(15) -> end なので15
# [1, 100, 1, 1, 100, 1, 1, 100, 1] -> 6 (100は踏みたくないよね)

def stairs_cost(costs: list[int]) -> int:

    # ゴール設定。
    costs += [0]


    # 各段に行くまでに必要な最小コスト
    # 1段目と2段目はそのコスト自身が入る
    min_costs = costs[:2] + [0] * (len(costs) - 2)

    print(costs)

    for i in range(2, len(costs)):

        # i段目に行くには、i-1 から一段上がるか i-2　から2段上がるか
        min_costs[i] = min(min_costs[i - 1], min_costs[i - 2]) + costs[i]

    return min_costs[-1]

print(stairs_cost([10, 15, 20]))
print(stairs_cost([1, 100, 1, 1, 100, 1, 1, 100, 1]))