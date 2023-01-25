def selectionSort():
    for x in range(10):
        pos = x
        for y in range(x,11):
            if nums[y] < nums[pos]:
                pos = y