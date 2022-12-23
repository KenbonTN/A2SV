def insertionSort1(n, arr):
    x = arr[n-1]
    for i in range(n-1,-1,-1):
        if i>0 and x < arr[i-1]:
            arr[i]=arr[i-1]
            print(*arr)
        else: 
            arr[i]=x
            print(*arr)
            break