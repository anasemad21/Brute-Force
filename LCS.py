## Longest common seq
def LCS(sequance1, sequance2):
    row = len(sequance1)
    col = len(sequance2)
    count1 = 0
    count2 = 0
    matrix = [[0] * col] * row
    seq = ""
    for i in range(1, row):
        for j in range(1, col):
            if sequance1[count1] == sequance2[count2]:
                matrix[i][j] = matrix[i - 1][j - 1] + 1

            else:
                matrix[i][j] = max(matrix[i][j - 1], matrix[i - 1][j])
            count2 += 1
        seq += sequance1[count1]
        count2 = 0
        count1 += 1
    #print(seq)
    return matrix[-1][-1]


print(LCS("AACCTTGG", "ACACTGTGA"))
