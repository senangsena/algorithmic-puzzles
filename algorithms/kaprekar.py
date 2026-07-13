
def do_one_update(number: int) -> int:
    
    list_num = list(str(number))

    four_digits = []

    for numchar in list_num:
        four_digits.append(int(numchar)) # [1, 3, 4, 2]

    while len(four_digits) < 4: # 3桁以下のときは先頭に0を付け足す
        four_digits = [0] + four_digits 

    four_digits.sort()

    order = 1
    large = 0
    for num in four_digits:
        large += order*num # 1 + 10*2 = 4321
        order *= 10 # 1000

    order = 1000
    small = 0
    for num in four_digits:
        small += order*num # 0 + 1000 * 1
        order //= 10
    print(large, "-", small)
    # small = 1234, large = 4321

    dif = large - small

    return dif

def kaprekar(number: int) -> int:
    
    before = None # xx
    after = number # xxxx

    while before != after:
        before = after # 1234
        after = do_one_update(before) # xxxx

    return after



if __name__ == "__main__":
    
    print("Enter your favorite number(0001 - 9998) Numbers with all identical digits (e.g., 1111, 2222) are not allowed.")

    while True:

        val = input()

        if val != "end":

            if int(val)%1111 == 0:
                print("Numbers with all identical digits (e.g., 1111, 2222) are not allowed. Try again.")
                continue
            
            print(kaprekar(int(val)))

        else:
            break