# 全体の3分の1より多く出た数字を見つける
# 常にそれまで出てきた数字の中で回数多いtop2を保存しておきたい。
# そもそも最も多く登場した数を調べるには？

def mapping_s():

    count = {}
    n = 0

    while True:

        val = input()

        if val == "end":

            border = n / 3

            for num in count:

                if count[num] > border:
                    print(num)
            
            print("finish")
            break

        val = int(val)
        n += 1

        if val in count:
            count[val] += 1
        else:
            count[val] = 1


def majority2():

    answer1 = -1
    answer2 = -1

    while True:

        

mapping_s()

            

