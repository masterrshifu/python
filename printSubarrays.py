def printSubarray(A, s, e):
    for i in range(s, e+1):
        print(A[i], end = " ")
    print()

def printAllSubarrays(A,N):

    for s in range(N):
        for e in range(s,N):
            printSubarray(A,s,e)

        


A = [1,2,3]
N = len(A)

printAllSubarrays(A,N)