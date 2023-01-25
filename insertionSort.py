def insertionSort(num):
    for x in range(1, len(num)):
        sort = num[x]
        while num[x-1] > sort and x>0:
            num[x], num[x-1] = num[x-1], num[x]
            x = x - 1

num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
insertionSort(num)
print(num)