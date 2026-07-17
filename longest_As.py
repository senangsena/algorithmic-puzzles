# AとBからなる文字列がある
# "AAABAABBBA" -> 6
# 一個だけ、B->Aにできる
# その時に最もAが連続するように変更したとする
# その時の、Aが連続する長さを返す

# AAAAAAAAA -> 9

def longest_As(ab: str) -> int:

    start = 0
    end = 0

    count_b = 0

    max_len = 0

    while end < len(ab):

        if ab[end] == "A":
            end += 1
        else: # end == B
            if count_b == 0:
                count_b += 1
                end += 1
            else:
                # start を、Bの一個隣にする
                while True:

                    if ab[start] == "B":
                        start += 1
                        count_b = 0
                        break
                    else:
                        start += 1

        max_len = max(max_len, end - start)

    return max_len

print(longest_As("AAABAABBB"))
print(longest_As("AAA"))
print(longest_As("AAABBB"))
print(longest_As(""))                

