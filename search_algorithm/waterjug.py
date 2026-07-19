# 水差し替え問題をBFSで実装
# キューに状態Stateを入れる

from collections import deque
import math

class State:

    def __init__(self, waterinA, waterinB):
        self.waterA = waterinA
        self.waterB = waterinB
        self.before_action = None # "pour_AtoB" "pour_BtoA" or "empty_A" or "fill_A" or "empty_B" or "fill_B"
        self.parent = None

class Problem:

    def __init__(self, sizeA, sizeB, goal_amount_of_water):
        self.sizeA = sizeA
        self.sizeB = sizeB
        self.goal = goal_amount_of_water

    def generate_child(self, state:State):

        children = []
        # Fill
        if state.waterA != self.sizeA:
            fillA = State(self.sizeA, state.waterB)
            fillA.before_action = "fill_A"
            children.append(fillA)
        if state.waterB != self.sizeB:
            fillB = State(state.waterA, self.sizeB)
            fillB.before_action = "fill_B"  
            children.append(fillB)

        # Empty
        if state.waterA != 0:
            emptyA = State(0, state.waterB)
            emptyA.before_action = "empty_A"
            children.append(emptyA)
        if state.waterB != 0:
            emptyB = State(state.waterA, 0)
            emptyB.before_action = "empty_B"
            children.append(emptyB)

        # Pour
        if state.waterB != self.sizeB and state.waterA != 0: # A->B
            pourAtoB = State(max(0, state.waterA - (self.sizeB - state.waterB)), min(self.sizeB, state.waterA + state.waterB))
            pourAtoB.before_action = "pourAtoB"
            children.append(pourAtoB)
        if state.waterA != self.sizeA and state.waterB != 0: # B->A
            pourBtoA = State(min(self.sizeA, state.waterB + state.waterA), max(0, state.waterB - (self.sizeA - state.waterA)))
            pourBtoA.before_action = "pourBtoA"  
            children.append(pourBtoA)

        for node in children:
            node.parent = state

        return children
    
    # 初期状態を設定して問題を解く
    # first_stateX...JugXにもともと入っている水量
    def solve(self, first_stateA, first_stateB):
        
        start = State(first_stateA, first_stateB)

        # queue を deque　で再現（enqueue: append, dequeue: popleft)
        q = deque()
        q.append(start)

        # 水量のペアを保存する
        visited = set()
        visited.add((start.waterA, start.waterB))

        while True:
            state = q.popleft()

            if state.waterA + state.waterB == self.goal:
                current = state
                ans = []
                while current.parent:
                    ans.append((current.waterA, current.waterB, current.before_action))
                    current = current.parent
                ans.append((start.waterA, start.waterB, start.before_action))
                return ans[::-1]
                
            children = self.generate_child(state)

            for child in children:
                if (child.waterA, child.waterB) not in visited:
                    q.append(child)
                    visited.add((child.waterA, child.waterB))
    

if __name__ == "__main__":
    
    while True:
        print("Input size of first jug:", end="")
        _sizeA = int(input())
        print("Input size of second jug:", end="")
        _sizeB = int(input())
        print("Input the goal amount:", end="")
        _goal = int(input())

        if _goal > _sizeA + _sizeB:
            print("[goal cant over sum of two jugs sizes]")
        elif _goal % math.gcd(_sizeA, _sizeB) != 0: # 2つの量の足し引きで作れる数は、2つの量の最大公約数の倍数のみ
            print("[Unvalid Setting...到達不可能なGOALです]")
        else:
            break
    
    p = Problem(sizeA=_sizeA, sizeB=_sizeB, goal_amount_of_water=_goal)
    """
    print("Setting complete. . . Input first state")
    print("Input amount of first jug:", end="")
    _firstA = int(input())
    print("Input amount of second jug:", end="")
    _firstB = int(input())
    """

    ans = p.solve(0,0)

    for s in ans:
        print(s)



