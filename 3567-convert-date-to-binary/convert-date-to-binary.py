class Solution:
    def convertDateToBinary(self, date: str) -> str:
        s = date.split('-')
        out = []
        for i in s:
            out.append(bin(int(i))[2:])
        return "-".join(out)
