class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        div = 0
        indiv = 0
        for i in range(n+1):
            if i%m == 0:
                div += i
            else:
                indiv += i
        return indiv - div