class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):
            row = [1]

            for x in range(i):
                row.append(( row[-1] * (i-x) ) // (x+1))
            output.append(row)

        return output