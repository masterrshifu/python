def balancingElement(arr, N):
    sL = 0
    for i in range(0,(int)(N/2)):
        sL += arr[i]

    sR = 0
    for i in range((int)(N/2),N):
        sR += arr[i]

    if sL > sR:
        return sL-sR
    elif sR > sL:
        return sR - sL
    else:
        return 0


list = [1,2,1,4,3,-2]

print(balancingElement(list,len(list)))