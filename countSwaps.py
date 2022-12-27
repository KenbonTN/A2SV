def countSwaps(a):
    count = 0
    for j in range(len(a)-1):
        for i in range(len(a)-1):
            if(a[i+1]<a[i]):
                (a[i+1],a[i]) = (a[i],a[i+1])
                count+=1
    print("Array is sorted in " +str(count)+" swaps.")
    print("First Element: "+ str(a[0]))  
    print("Last Element: "+ str(a[len(a)-1]))