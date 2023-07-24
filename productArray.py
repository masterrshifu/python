

# #brute force approach




# product = 1

# for i in range(len(A)):
#     product = product*A[i]


# for i in range(len(A)):
#     A[i] = (int)(product/A[i])


# print(A)

#optimized approach

A = [1,2,3,4,5]

prefProd = []
suffProd = []

N = len(A)

prefProd.append(A[0])

for i in range(1,N):
    prefProd.append(prefProd[i-1]*A[i])


for i in range(N):
    suffProd.append(1)

suffProd[N-1] = A[N-1]

for i in range(N-2,-1,-1):
    suffProd[i] = suffProd[i+1] * A[i]








for i in range(N):
    if i==0:
        A[i] = suffProd[i+1]
    elif i == N-1:
        A[i] = prefProd[i-1]
    else:
        A[i] = suffProd[i+1]*prefProd[i-1]

print(A)