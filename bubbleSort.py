def bubbleSort(num):
    for x in range(len(num)-1,0,-1):
        for y in range(x):
            if num[y]>num[y+1]:
                temp = num[y]
                num[y] = num[y+1]
                num[y+1] = temp

num = [7, 26, 86, 88, 73, 59, 19, 18, 44, 46]
bubbleSort(num)
print(num)