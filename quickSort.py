def partition(num, low, high):
    pivot = num[high]

    x = low - 1
    for y in range(low, high):
        if num[y] <= pivot:
            x = x + 1
            (num[x], num[y]) = (num[y], num[x])
    (num[x + 1], num[high]) = (num[high], num[x + 1])

num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
print(num)




#def quickSort():
