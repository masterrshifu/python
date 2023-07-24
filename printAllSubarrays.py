A = [2,3,-1]

B = 5

prefixSum = []
prefixSum.append(A[0])

for i in range(1,len(A)):
    prefixSum.append(prefixSum[i-1] + A[i])

sum = 0
maxSum = 0

for i in range(len(A)):
    for j in range(i,len(A)):
        if(i==0):
            sum = prefixSum[j]
        else:
            sum = prefixSum[j] - prefixSum[i-1]

        if(sum > maxSum and sum <= B):
            maxSum = sum
    


print(maxSum)