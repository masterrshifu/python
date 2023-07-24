A = [2,3,4,3,4,2,2,3,4,6]


dict = {}
for i in range(len(A)):
    if A[i] in dict:
        dict[A[i]] = dict.get(A[i]) + 1
    else:
        dict[A[i]] = 1

print(dict[2])

