class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        out = []
        n= len(boxes)
        for i in range(n):
            move = 0
            for j in range(n):
                if boxes[j] == "1":
                    move += abs(j-i)
            out.append(move) 
        return out    