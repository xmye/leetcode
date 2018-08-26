# Question 1
def Combine(str1,str2):
    i,j = len(str1)-1,0
    count = 0
    while i >= 0 and j < len(str2):
        if str1[i] == str2[j]:
            count += 1
        i -= 1
        j += 1
    str3 = str1[:(len(str1)-count)] + str2[count:]

    return str3

# Question 2
def merge(left,right):
    arr = []
    i,j = 0,0
    while i< len(left) and j< len(right):
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i+=1
        if j == len(right):
            for k in left[i:]:
                arr.append(k)
        if i == len(left):
            for k in right[j:]:
                arr.append(k)
    return arr

def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) / 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return merge(left,right)

def findKCombinationArray(lst,k):
    L = []
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            L.append(min(lst[i],lst[j]))

    merl = merge_sort(L)
    return merl[k]


# Question 3
def maxProfit(prices,p):
    if prices == None or len(prices) < 2:
        return
    profit = 0
    minprice = prices[0]
    for price in prices:
        if price <= minprice:
            minprice = price
        elif price - minprice > p:
            profit += (price - minprice - p)
            print('profit',profit)
            minprice = price
    return profit

# Test
str3 = Combine("abcdef", "fedha")
print(str3)

price = [0, 2, 1, 8, 4, 9]
p = 2
profit = maxProfit(price,p)
print(profit)