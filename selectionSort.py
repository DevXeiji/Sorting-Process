def selectionSort(num):
    for x in range(9):
        pos = x
        for y in range(x,10):
            if num[y] < num[pos]:
                pos = y

        temp = num[x]
        num[x] = num[pos]
        num[pos] = temp
        print(num)


num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
selectionSort(num)
