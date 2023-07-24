A = [-3,6,2,3,7,2,-1]

RM = []

for i in range(len(A)):
    RM.append(0)


N = len(A)

RM[N-1] = A[N-1]
print(RM)

for i in range(N-2,-1,-1):
    RM[i] = max(RM[i+1],A[i])

print(RM)