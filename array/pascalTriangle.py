def pascalTriangle(k):
    res = []
    row = []
    row1 = []
    if k < 1:
        return
    row1.append(1)
    res.append(row1)
    if k == 1:
        return res
    for i in range(1,k):
        row.append(1)
        for j in range(1,i):
            row.append(res[i-1][j-1] + res[i-1][j])
        row.append(1)
        res.append(row)
        row = []
    return res

print(pascalTriangle(4))