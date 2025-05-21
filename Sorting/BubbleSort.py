def bubbleSort(arr: [int], size: int):
    # Your code goes here.
    for i in range(len(arr)):
        flag=False
        for j in range(0,len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                flag=True
        if flag==False:
            break
    pass
