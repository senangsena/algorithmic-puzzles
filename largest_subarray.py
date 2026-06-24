# 連続部分和の最大値を求める

def find_maximum_sum():

    maximum = float('-inf')
    candidate = 0

    while True:

        val = input()

        if val == "end":
            break

        val = int(val) # ex) 1, -4 , 10 -> 10


        # candidateが負 → その後の数字列に関わらず、candidateは不要な部分なのでvalでリセット
        candidate = max(val, candidate + val)

        if candidate > maximum: # 1 > 0
            maximum = candidate # max = 1 -> 10

    return maximum

print(find_maximum_sum())
        
