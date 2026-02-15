class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        ss = s[:k][::-1]
        return ss + s[k:]
