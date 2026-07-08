class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        sorted_pairs = sorted(pairs, key= lambda x: x[0], reverse=True)
        for pos, spd in sorted_pairs:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)