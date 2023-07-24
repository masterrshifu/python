def sumSubarray(A,N):

    prefixSum = []
    prefixSum.append(A[0])
    for i in range(1,N):
        prefixSum.append(prefixSum[i-1] + A[i])



    for s in range(0,N):
        for e in range(s,N):
            sum = 0

            if s == 0:
                sum = prefixSum[e]
            else:
                sum = prefixSum[e] - prefixSum[s-1]

            print(sum)


A = [1,2,3]
N = len(A)

sumSubarray(A,N)