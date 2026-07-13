# 1~5までの整数をランダムに生成する乱数生成器を使用し、1~7までの整数をランダムに生成するアルゴリズム

import random

# 1~5までの整数をランダムに生成する乱数生成器
def generate_random5():
    return random.randint(1, 5)

# generate_random5()のみを使って、generate_random7()を実装する
def generate_random7():

    # まずは25通りの状況を7個生み出す
    # 1〜5ではなく0~4を生成する乱数生成器の方がやりやすいので-1する
    numbers = []
    for i in range(7): # 1~25の乱数
        n = (generate_random5()-1) * 5 + (generate_random5()-1) + 1
        numbers.append(n)
    
    
    

        
def test():

    counts = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    TIME = 10000

    for i in range(TIME):
        
        number = generate_random7()
        if number not in counts:
            print(f"not correct generate_random7(), {number}")
            exit(1)
        else:
            counts[number] += 1
        
    print(f"試行回数：{TIME}回")
    print()
    for num in counts:
        print(f"{num} が {counts[num]} 個")

test()

    
