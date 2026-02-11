class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        out = []
        for i in order:
            if i in friends:
                out.append(i)
        return out