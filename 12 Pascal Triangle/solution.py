class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        val = 1
        for i in range(rowIndex):
            val = int(val*(rowIndex-i)/(i+1))
            res.append(val)
        return res
        