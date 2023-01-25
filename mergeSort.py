def mergeSort(num):
    if len(num) > 1:
        temp = len(num)//2
        LFT = num[:temp]
        RGT = num[temp:]

        mergeSort(LFT)
        mergeSort(RGT)