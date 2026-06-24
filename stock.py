# 株の売買アルゴリズム
# [1, 5, 2, ]

def stock():

    # min_stock: 今まで見た中の、最小値
    # max_stock: min_stockが登場したより後に、出てきた中の最大値
    min_stock = -1
    max_stock = -1

    best_score = 0 # 現在までの最も高い利益

    while True:

        val = input()

        if val == "end":
            break

        val = int(val)
        
        if min_stock < 0:
            min_stock = val
            max_stock = val
        else:
            if val < min_stock:
                min_stock = val
                max_stock = val # min_stockが登場したより後に、max_stockが登場しないといけないから

                
            elif val > max_stock:
                max_stock = val

                if max_stock - min_stock > best_score:
                    best_score = max_stock - min_stock

    return best_score

print(stock())

