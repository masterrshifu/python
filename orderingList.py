A = [0,0,0,1,1,0,1,0,1,1]



N = len(A)

l = 0

r = N-1


while(l<=r):

    if(A[l] == 0):
        l+=1

    elif(A[r] == 1):
        r-=1
    else:
        A[l], A[r] = A[r],A[l]    #swapping the values

print(A)