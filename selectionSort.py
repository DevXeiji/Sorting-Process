def selectionSort(num):
    for x in range(10):
        pos = x
        for y in range(x,9):
            if num[y] < num[pos]:
                pos = y

        print(num)


num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
selectionSort(num)
print(num)
