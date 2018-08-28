
def compressStr(str):
    i,count = 0,1
    comstr = []

    while i < len(str)-1:
        if str[i] == str[i+1]:
            count += 1
        else:
            comstr.append(str[i])
            comstr.append(count)
            count = 1
        i += 1

    comstr.append(str[len(str)-1])
    comstr.append(count)

    return comstr

arr = "aaaaccbbbbaaaa"
print("initial array:\n",arr)
# compressStr(arr)
print("result array:\n",compressStr(arr))