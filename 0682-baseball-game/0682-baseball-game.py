class Solution:
    def calPoints(self, operations: List[str]) -> int:
        lis = []
        for i in operations:
            if i == 'C':
                lis.pop()
            elif i == 'D':
                a = 2 * lis[-1]
                lis.append(a)
            elif i == '+':
                b = lis[-1] + lis[-2]
                lis.append(b)
            else:
                lis.append(int(i))

        adution = sum(lis)
        return adution
