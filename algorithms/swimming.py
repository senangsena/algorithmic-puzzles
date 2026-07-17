# 初めて歩けた日（元の題）
#      ↓ 　↓
# 右から左に初めて泳げた記念すべき日の一個前の日

# 
def swimming(rows:int, cols:int, water: list[list[int]]):

    day = len(cols) # swimmingできる最初の日は最低限len(cols)

    # ここからはwalkingできるかを考える

