
def findIndex(A,N):


    sL = 0
    sR = 0

    for i in range(N):

        sL = 0
        sR = 0

        
        for j in range(i):
            sL = sL + A[j]

        for j in range(i+1,N):
            sR = sR + A[j] 

        if sL == sR:
            return True

    
    return False


A = [1,2,3,4,8,10]
N = len(A)

print(findIndex(A,N))