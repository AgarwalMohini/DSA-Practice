def findDuplicate(arr):
    # Write your code here
    seen=set()
    l=[]
    for num in arr:
        if num in seen and num not in l:
            l.append(num)
        seen.add(num)
    return "".join(map(str,l))
    pass
