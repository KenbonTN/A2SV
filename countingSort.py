def countingSort(arr):
    countArray = []
    for i in range(100):
        countArray.append(0)
    for i in range (len(arr)):
        countArray[arr[i]]+=1
    return (countArray)