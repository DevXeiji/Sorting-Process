def partition(num, low, high):
    pivot = num[high]

    x = low - 1
    for y in range(low, high):
        if num[y] <= pivot:
            x = x + 1
            (num[x], num[y]) = (num[y], num[x])
    (num[x + 1], num[high]) = (num[high], num[x + 1])

def quickSort(num, low, high):
    if low < high:
        temp = partition(num, low, high)
        quickSort(num, low, temp - 1)
        quickSort(num, temp + 1, high)



num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
print(num)

