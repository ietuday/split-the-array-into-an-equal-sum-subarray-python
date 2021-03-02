def findPivot(arr):
    l=0
    r=len(arr)-1
    lsum=arr[l]
    rsum=arr[r]
    print("l", l)
    print("r", r)
    print("lsum", lsum)
    print("rsum", rsum)

    while l<r:
        if lsum==rsum and l+2==r:
            return l+1
            print("l---if",l)
        elif lsum<rsum:
            l += 1
            lsum+=arr[l]
            print("l --elif", l)
            print("lsum --elif", lsum)
        else:
            r -= 1
            rsum+=arr[r]
            print("else---r",r)
            print("else---rsum",rsum)

    return -1

print(findPivot([2, 4, 5, 1, 2, 3]))